
from typing import Optional
from aiohttp import web
from aiohttp.web import FileField
from aiohttp.web_request import Request
from .plugins import DummyPermissions as PermissionsProxy
from beacon.logs.logs import LOG
from beacon.auth.__main__ import authentication
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from beacon.connections.mongo.datasets import get_list_of_datasets

@log_with_args(level)
async def authorization(self, request):
    try:
        auth = request.headers.get('Authorization')
        if not auth or not auth.lower().startswith('bearer '):
            raise web.HTTPUnauthorized()
        list_visa_datasets=[]
        access_token = auth[7:].strip() # 7 = len('Bearer ')
        user, list_visa_datasets = await authentication(self, access_token)
        if user is None:
            user = 'public'
        elif user == 'public':
            username = 'public'
        else:
            username = user.get('preferred_username')
    except Exception:
        list_visa_datasets = []
        username = 'public'
        return username, list_visa_datasets
    return username, list_visa_datasets

@log_with_args(level)
async def get_datasets_list(self, request: Request, authorized_datasets):
    try:
        specific_datasets_unauthorized = []
        search_and_authorized_datasets = []
        try:
            specific_datasets = qparams.query.request_parameters['datasets']
        except Exception as e:
            specific_datasets = []
        # Get response
        if specific_datasets != []:
            for element in authorized_datasets:
                if element in specific_datasets:
                    search_and_authorized_datasets.append(element)
            for elemento in specific_datasets:
                if elemento not in search_and_authorized_datasets:
                    specific_datasets_unauthorized.append(elemento)
            beacon_datasets = get_list_of_datasets(self)
            response_datasets = [ r['id'] for r in beacon_datasets if r['id'] in search_and_authorized_datasets]

        else:
            beacon_datasets = get_list_of_datasets(self)
            specific_datasets = [ r['id'] for r in beacon_datasets if r['id'] not in authorized_datasets]
            response_datasets = [ r['id'] for r in beacon_datasets if r['id'] in authorized_datasets]
            specific_datasets_unauthorized.append(specific_datasets)
    except Exception:
        raise
    return response_datasets

def dataset_permissions(func):
    @log_with_args(level)
    async def permission(self, post_data, request: Request, qparams, entry_type, entry_id):
        try:
            if post_data is not None:
                v = post_data.get('datasets')
            else:
                v = None
            if v is None:
                requested_datasets = []
            elif isinstance(v, list):
                requested_datasets = v
            elif isinstance(v, FileField):
                requested_datasets = []
            else:
                requested_datasets = v.split(sep=',')
            
            username, list_visa_datasets = await authorization(self, request)
                
            datasets = await PermissionsProxy.get(self, username=username, requested_datasets=requested_datasets)
            dict_returned={}
            dict_returned['username']=username
            authorized_datasets=list(datasets)
            for visa_dataset in list_visa_datasets:
                authorized_datasets.append(visa_dataset)
            response_datasets= await get_datasets_list(self, request, authorized_datasets)
            return await func(self, post_data, request, qparams, entry_type, entry_id, response_datasets)
        except Exception:
            raise
    return permission

