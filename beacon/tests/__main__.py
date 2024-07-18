
from aiohttp.test_utils import TestClient, TestServer, loop_context
from aiohttp import web
from beacon.__main__ import ControlView, InfoView
import json
import unittest
from beacon.permissions.tests import TestAuthZ
from beacon.validator.tests import TestValidator
from beacon.auth.tests import TestAuthN

def create_app():
    app = web.Application()
    #app.on_startup.append(initialize)
    app.add_routes([web.get('/control', ControlView)])
    app.add_routes([web.get('/info', InfoView)])
    return app

TestAuthN

TestAuthZ

TestValidator

class TestMain(unittest.TestCase):
    def test_main_check_control_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_control_endpoint_is_working():
                resp = await client.get("/control")
                assert resp.status == 200
                text = await resp.text()
                assert json.dumps({'resp': 'hello world'}) == text
            loop.run_until_complete(test_check_control_endpoint_is_working())
            loop.run_until_complete(client.close())

if __name__ == '__main__':
    unittest.main()


