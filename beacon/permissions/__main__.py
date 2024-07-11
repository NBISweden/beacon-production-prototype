from typing import Optional
from aiohttp import web
from aiohttp.web import FileField
from aiohttp.web_request import Request
from .plugins import DummyPermissions as PermissionsProxy
from beacon.auth.__main__ import bearer_required
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level

@log_with_args(level=level)
@bearer_required
async def permission(request: Request, username: Optional[str], list_visa_datasets: Optional [list]):

    if request.headers.get('Content-Type') == 'application/json':
        post_data = await request.json()
    else:
        post_data = await request.post()

    v = post_data.get('datasets')
    if v is None:
        requested_datasets = []
    elif isinstance(v, list):
        requested_datasets = v
    elif isinstance(v, FileField):
        requested_datasets = []
    else:
        requested_datasets = v.split(sep=',')
        
    datasets = await PermissionsProxy.get(username, requested_datasets=requested_datasets)
    dict_returned={}
    dict_returned['username']=username
    datasets=list(datasets)
    for visa_dataset in list_visa_datasets:
        datasets.append(visa_dataset)
    dict_returned['datasets']=list(datasets)

    return web.json_response(dict_returned)