from aiohttp.test_utils import TestClient, TestServer, loop_context
from beacon.__main__ import ControlView
import unittest
import glob
import os
import jwt
from aiohttp import web
from beacon.auth.__main__ import fetch_idp, validate_access_token
from aiohttp.test_utils import make_mocked_request
from dotenv import load_dotenv


mock_access_token = ''
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
                load_dotenv("beacon/auth/idp_providers/test.env", override=True)
                IDP_ISSUER = os.getenv('ISSUER')
                IDP_CLIENT_ID = os.getenv('CLIENT_ID')
                IDP_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
                IDP_USER_INFO = os.getenv('USER_INFO')
                IDP_INTROSPECTION = os.getenv('INTROSPECTION')
                IDP_JWKS_URL = os.getenv('JWKS_URL')
                assert IDP_ISSUER == idp_issuer
                assert IDP_CLIENT_ID == idp_client_id
                assert IDP_CLIENT_SECRET == idp_client_secret
                assert IDP_USER_INFO == user_info
                assert IDP_INTROSPECTION == idp_introspection
                assert IDP_JWKS_URL == idp_jwks_url
            loop.run_until_complete(test_fetch_idp())
            loop.run_until_complete(client.close())
    def test_auth_validate_access_token(self):
        with loop_context() as loop:
            app = create_test_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_validate_access_token():
                load_dotenv("beacon/auth/idp_providers/test.env", override=True)
                IDP_ISSUER = os.getenv('ISSUER')
                IDP_CLIENT_ID = os.getenv('CLIENT_ID')
                IDP_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
                IDP_USER_INFO = os.getenv('USER_INFO')
                IDP_INTROSPECTION = os.getenv('INTROSPECTION')
                IDP_JWKS_URL = os.getenv('JWKS_URL')
                try:
                    header = jwt.get_unverified_header(mock_access_token)
                    algorithm=header["alg"]
                    decoded = jwt.decode(mock_access_token, options={"verify_signature": False})
                    issuer = decoded['iss']
                    aud = decoded['aud']
                except Exception:
                    raise web.HTTPUnauthorized()
                access_token_validation = validate_access_token(self, mock_access_token, IDP_ISSUER, IDP_JWKS_URL, algorithm, aud)
                assert access_token_validation == True
            loop.run_until_complete(test_validate_access_token())
            loop.run_until_complete(client.close())

if __name__ == '__main__':
    unittest.main()