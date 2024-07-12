from aiohttp.test_utils import TestClient, TestServer, loop_context
from beacon.logs.logs import log_with_args
from beacon.tests.__main__ import create_app
from beacon.validator.validator import info_check
import logging
import json
import unittest

class TestValidator(unittest.TestCase):
    def test_validator_validate_info(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            @log_with_args(level=logging.DEBUG)
            async def test_validate_info():
                resp = info_check("http://localhost:5070/info")
                return resp
            loop.run_until_complete(test_validate_info())
            loop.run_until_complete(client.close())

if __name__ == '__main__':
    unittest.main()