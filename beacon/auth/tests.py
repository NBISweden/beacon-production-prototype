from aiohttp.test_utils import TestClient, TestServer, loop_context
from beacon.__main__ import ControlView
import unittest
import glob
import os
import jwt
from aiohttp import web
from beacon.auth.__main__ import fetch_idp
from aiohttp.test_utils import make_mocked_request
from dotenv import load_dotenv


mock_access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJreS1tUXNxZ0ZYeHdSUVRfRUhuQlJJUGpmbVhfRXZuUTVEbzZWUTJCazdZIn0.eyJleHAiOjE3MjEyOTUzNjcsImlhdCI6MTcyMTI5NTA2NywianRpIjoiOGE2OTA1YjItNzcyZi00MTQxLWE1NDMtNGFiZDM3OGYyNzk5IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDg1L2F1dGgvcmVhbG1zL0JlYWNvbiIsImF1ZCI6ImJlYWNvbiIsInN1YiI6IjQ3ZWZmMWIxLTc2MjEtNDU3MC1hMGJiLTAxYTcxOWZiYTBhMiIsInR5cCI6IkJlYXJlciIsImF6cCI6ImJlYWNvbiIsInNlc3Npb25fc3RhdGUiOiIzNmRhNWRlZi1kYzMzLTRlZGItYWM2Yi1kOWI3YWJiNjEwYzciLCJhY3IiOiIxIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtaWNyb3Byb2ZpbGUtand0Iiwic2lkIjoiMzZkYTVkZWYtZGMzMy00ZWRiLWFjNmItZDliN2FiYjYxMGM3IiwidXBuIjoiamFuZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6IkphbmUgU21pdGgiLCJncm91cHMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXSwicHJlZmVycmVkX3VzZXJuYW1lIjoiamFuZSIsImdpdmVuX25hbWUiOiJKYW5lIiwiZmFtaWx5X25hbWUiOiJTbWl0aCIsImVtYWlsIjoiamFuZS5zbWl0aEBiZWFjb24uZ2E0Z2gifQ.O2ZlForYB_s_1xotLp4_5uAJjMzJc0nbeahSjYE9aMlpy0Cc_F5lkdoOYUKeFVZXmeafPPXhOFxGjcASzG8AJ-0JjIt278kn45a2oyCnucM9kVE7dmTnMOZv8so74Kw0WzrZ6GgWXKyLb7JcN9X7pP3vLCqAPxupielMU5IWGwaoxOxfsvu6hd8Q7uMdc_CVxZxkCcsxYaSZ2KT6Fqwp7qtio2BQFP6o_6FMlAgumO4vHaFamXPA_kNvOtA9P7vf81aF2HTg0cCf42cmvAgFtNl-D8D8l_pLN3BkCx9rmvQG8HoxEUqYOVWXDspxRssgupe1Q9cRjrNhGuq7xDKrAA'
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
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._id = 'test'
    def test_auth_fetch_idp(self):
        with loop_context() as loop:
            app = create_test_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_fetch_idp():
                idp_issuer, user_info, idp_client_id, idp_client_secret, idp_introspection, idp_jwks_url, algorithm, aud = fetch_idp(self, mock_access_token)
                assert 'http://localhost:8085/auth/realms/Beacon' == idp_issuer
            loop.run_until_complete(test_fetch_idp())
            loop.run_until_complete(client.close())

if __name__ == '__main__':
    unittest.main()