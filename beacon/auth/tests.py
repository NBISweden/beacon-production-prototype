from aiohttp.test_utils import TestClient, TestServer, loop_context
from beacon.logs.logs import log_with_args
from beacon.tests.__main__ import create_app
import logging
import json
import unittest

#dummy test anonymous
#dummy test login
#add test coverage
#audit --> agafar informació molt específica que ens interessa guardar per sempre (de quins individuals ha obtingut resultats positius)

class TestApp(unittest.TestCase):
    def test_auth_verify_public_datasets(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            @log_with_args(level=logging.DEBUG)
            async def test_verify_public_datasets():
                resp = await client.post('/control', headers={'Auhtorization': 'Bearer access_token'})
                assert resp.status == 200
                text = await resp.text()
                assert json.dumps({'status': 2}) == text
            loop.run_until_complete(test_verify_public_datasets())
            loop.run_until_complete(client.close())