from aiohttp.test_utils import TestClient, TestServer, loop_context
from beacon.logs.logs import log_with_args
from beacon.__main__ import ControlView
import logging
import unittest
from aiohttp import web
from aiohttp.web import FileField
from aiohttp.web_request import Request
from .plugins import DummyPermissions as PermissionsProxy
from aiohttp.test_utils import make_mocked_request


#dummy test anonymous
#dummy test login
#add test coverage
#audit --> agafar informació molt específica que ens interessa guardar per sempre (de quins individuals ha obtingut resultats positius)

async def test_public_permission(request: Request):
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
    username = 'public'
    list_visa_datasets=[]
    datasets = await PermissionsProxy.get(self=PermissionsProxy, username=username, requested_datasets=requested_datasets)
    dict_returned={}
    dict_returned['username']=username
    datasets=list(datasets)
    for visa_dataset in list_visa_datasets:
        datasets.append(visa_dataset)
    dict_returned['datasets']=list(datasets)

    return datasets

async def test_permission(request: Request):
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
    username = 'dummy_user'
    list_visa_datasets=[]
    datasets = await PermissionsProxy.get(self=PermissionsProxy, username=username, requested_datasets=requested_datasets)
    dict_returned={}
    dict_returned['username']=username
    datasets=list(datasets)
    for visa_dataset in list_visa_datasets:
        datasets.append(visa_dataset)
    dict_returned['datasets']=list(datasets)

    return datasets

def create_test_app():
    app = web.Application()
    #app.on_startup.append(initialize)
    app.add_routes([web.get('/control', ControlView)])
    return app

class TestAuthZ(unittest.TestCase):
    def test_authZ_verify_public_datasets(self):
        with loop_context() as loop:
            app = create_test_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_verify_public_datasets():
                req = make_mocked_request('GET', '/', headers={'token': 'x'})
                datasets = await test_public_permission(req)
                tc = unittest.TestCase()
                tc.assertSetEqual(set(['CINECA_synthetic_cohort_EUROPE_UK1', 'CINECA_dataset', 'coadread_tcga_pan_can_atlas_2018', 'rd-connect_dataset']),set(datasets))
            loop.run_until_complete(test_verify_public_datasets())
            loop.run_until_complete(client.close())
    def test_authZ_verify_registered_datasets(self):
        with loop_context() as loop:
            app = create_test_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_verify_registered_datasets():
                req = make_mocked_request('GET', '/', headers={'token': 'x'})
                datasets = await test_permission(req)
                tc = unittest.TestCase()
                tc.assertSetEqual(set(['CINECA_synthetic_cohort_EUROPE_UK1', 'CINECA_dataset', 'coadread_tcga_pan_can_atlas_2018', 'AV_Dataset', 'rd-connect_dataset']),set(datasets))
            loop.run_until_complete(test_verify_registered_datasets())
            loop.run_until_complete(client.close())
    def test_authZ_bearer_required(self):
        with loop_context() as loop:
            app = create_test_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_bearer_required():
                req = make_mocked_request('GET', '/', headers={'Authorization': 'Bearer '})
                auth = req.headers.get('Authorization')
                if not auth or not auth.lower().startswith('bearer '):
                    raise web.HTTPUnauthorized()
                assert auth[0:7] == 'Bearer '
            loop.run_until_complete(test_bearer_required())
            loop.run_until_complete(client.close())

if __name__ == '__main__':
    unittest.main()