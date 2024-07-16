'''


from aiohttp.test_utils import TestClient, TestServer, loop_context
from aiohttp import web
from beacon.__main__ import control, info
from beacon.logs.logs import log_with_args
import logging
import json
import unittest
from beacon.validator.validator import info_check, load_json_from_url
import os

def create_app():
    app = web.Application()
    #app.on_startup.append(initialize)
    app.add_routes([web.get('/control', control)])
    app.add_routes([web.get('/info', info)])
    return app

# loop_context is provided as a utility. You can use any
# asyncio.BaseEventLoop class in its place.

class TestApp(unittest.TestCase):
    def test_main_check_control_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            @log_with_args(level=logging.DEBUG)
            async def test_check_control_endpoint_is_working():
                resp = await client.get("/control")
                assert resp.status == 200
                text = await resp.text()
                assert json.dumps({'resp': 'hello world'}) == text
            loop.run_until_complete(test_check_control_endpoint_is_working())
            loop.run_until_complete(client.close())

class TestInfo(unittest.TestCase):
    def test_info_validate_info_schema(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            @log_with_args(level=logging.DEBUG)
            async def test_validate_info():
                resp = info_check("http://localhost:5070/info")
                assert []==resp
            loop.run_until_complete(test_validate_info())
            loop.run_until_complete(client.close())

class TestApp2(unittest.TestCase):
    def test_main_check_control_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            @log_with_args(level=logging.DEBUG)
            async def test_check_control_endpoint_is_working():
                resp = await client.get("/control")
                assert resp.status == 200
                text = await resp.text()
                assert json.dumps({'status': 2}) == text
            loop.run_until_complete(test_check_control_endpoint_is_working())
            loop.run_until_complete(client.close())


class TestValidator(unittest.TestCase):
    def test_validator_load_json_from_url(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            @log_with_args(level=logging.DEBUG)
            async def test_load_json_from_url():
                resp = load_json_from_url('http://localhost:5070/control')
                assert {'resp': 'hello world'} == resp
            loop.run_until_complete(test_load_json_from_url())
            loop.run_until_complete(client.close())
    def test_validator_catching_errors_load_json_from_url(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            @log_with_args(level=logging.DEBUG)
            async def test_catching_errors_load_json_from_url():
                resp = load_json_from_url('http://localhost:5070/contro')
                assert resp.status == 404
            loop.run_until_complete(test_catching_errors_load_json_from_url())
            loop.run_until_complete(client.close())

if __name__ == '__main__':
    unittest.main()


'''