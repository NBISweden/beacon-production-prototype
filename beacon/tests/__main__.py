import imp
from aiohttp.test_utils import TestClient, TestServer, loop_context
from aiohttp import request
from aiohttp import web
from beacon.__main__ import success, failure
from beacon.logs.logs import log_with_args
import logging
import json
import unittest

def create_app():
    app = web.Application()
    #app.on_startup.append(initialize)
    app.add_routes([web.get('/success', success)])
    app.add_routes([web.get('/failure', failure)])
    return app

# loop_context is provided as a utility. You can use any
# asyncio.BaseEventLoop class in its place.
# test_ + nom del mòdul + nom rebel·lador del que fa el test (objectiu del test)
# control test en comptes de success, deixar 1 positiu
class TestApp(unittest.TestCase):
    def test_api_success(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            @log_with_args(level=logging.DEBUG)
            async def test_get_route():
                resp = await client.get("/success")
                assert resp.status == 200
                text = await resp.text()
                assert json.dumps({'status': 2}) == text
            loop.run_until_complete(test_get_route())
            loop.run_until_complete(client.close())
    def test_api_failure(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())

            @log_with_args(level=logging.DEBUG)
            async def test_get_route():
                resp = await client.get("/failure")
                assert resp.status == 500

            loop.run_until_complete(test_get_route())
            loop.run_until_complete(client.close())
    def test_api_assert_failure(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())

            @log_with_args(level=logging.DEBUG)
            async def test_get_route():
                resp = await client.get("/success")
                assert resp.status == 200
                text = await resp.text()
                assert json.dumps({'status': 3}) == text

            loop.run_until_complete(test_get_route())
            loop.run_until_complete(client.close())

if __name__ == '__main__':
    unittest.main()