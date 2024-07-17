from aiohttp.test_utils import TestClient, TestServer, loop_context
from beacon.__main__ import ControlView
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

def create_test_app():
    app = web.Application()
    #app.on_startup.append(initialize)
    app.add_routes([web.get('/control', ControlView)])
    return app

class TestAuthN(unittest.TestCase):
    def test_auth_bearer_required(self):
        with loop_context() as loop:
            app = create_test_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_bearer_required():
                req = make_mocked_request('GET', '/', headers={'Authorization': 'Bearer '})
                datasets = await test_permission(req)
                tc = unittest.TestCase()
                tc.assertSetEqual(set(['CINECA_synthetic_cohort_EUROPE_UK1', 'CINECA_dataset', 'coadread_tcga_pan_can_atlas_2018', 'AV_Dataset', 'rd-connect_dataset']),set(datasets))
            loop.run_until_complete(test_bearer_required())
            loop.run_until_complete(client.close())

if __name__ == '__main__':
    unittest.main()