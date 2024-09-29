
from aiohttp.test_utils import TestClient, TestServer, loop_context
from aiohttp import web
from beacon.__main__ import Collection, Resultset, Info, ServiceInfo, Map, Configuration, FilteringTerms, EntryTypes
import json
import unittest
from beacon.permissions.tests import TestAuthZ
from beacon.validator.tests import TestValidator
from beacon.auth.tests import TestAuthN
#from beacon.request.tests import TestRequest
from beacon.tests.wrong_service_info import service_info_wrong
from aiohttp.test_utils import make_mocked_request
from beacon.response.catalog import build_beacon_error_response
from bson import json_util
from beacon.logs.logs import LOG
from beacon.connections.mongo.filters import cross_query
from unittest.mock import MagicMock

def create_app():
    app = web.Application()
    #app.on_startup.append(initialize)
    app.add_routes([web.view('/api', Info)])
    app.add_routes([web.view('/api/info', Info)])
    app.add_routes([web.view('/api/entry_types', EntryTypes)])
    app.add_routes([web.view('/api/service-info', ServiceInfo)])
    app.add_routes([web.view('/api/configuration', Configuration)])
    app.add_routes([web.view('/api/map', Map)])
    app.add_routes([web.view('/api/filtering_terms', FilteringTerms)])
    app.add_routes([web.view('/api/datasets', Collection)])
    app.add_routes([web.view('/api/datasets/{id}', Collection)])
    app.add_routes([web.view('/api/datasets/{id}/g_variants', Resultset)])
    app.add_routes([web.view('/api/datasets/{id}/biosamples', Resultset)])
    app.add_routes([web.view('/api/datasets/{id}/analyses', Resultset)])
    app.add_routes([web.view('/api/datasets/{id}/runs', Resultset)])
    app.add_routes([web.view('/api/datasets/{id}/individuals', Resultset)])
    app.add_routes([web.view('/api/cohorts', Collection)])
    app.add_routes([web.view('/api/cohorts/{id}', Collection)])
    app.add_routes([web.view('/api/cohorts/{id}/individuals', Resultset)])
    app.add_routes([web.view('/api/cohorts/{id}/g_variants', Resultset)])
    app.add_routes([web.view('/api/cohorts/{id}/biosamples', Resultset)])
    app.add_routes([web.view('/api/cohorts/{id}/analyses', Resultset)])
    app.add_routes([web.view('/api/cohorts/{id}/runs', Resultset)])
    app.add_routes([web.view('/api/g_variants', Resultset)])
    app.add_routes([web.view('/api/g_variants/{id}', Resultset)])
    app.add_routes([web.view('/api/g_variants/{id}/analyses', Resultset)])
    app.add_routes([web.view('/api/g_variants/{id}/biosamples', Resultset)])
    app.add_routes([web.view('/api/g_variants/{id}/individuals', Resultset)])
    app.add_routes([web.view('/api/g_variants/{id}/runs', Resultset)])
    app.add_routes([web.view('/api/individuals', Resultset)])
    app.add_routes([web.view('/api/individuals/{id}', Resultset)])
    app.add_routes([web.view('/api/individuals/{id}/g_variants', Resultset)])
    app.add_routes([web.view('/api/individuals/{id}/biosamples', Resultset)])
    app.add_routes([web.view('/api/analyses', Resultset)])
    app.add_routes([web.view('/api/analyses/{id}', Resultset)])
    app.add_routes([web.view('/api/analyses/{id}/g_variants', Resultset)])
    app.add_routes([web.view('/api/biosamples', Resultset)])
    app.add_routes([web.view('/api/biosamples/{id}', Resultset)])
    app.add_routes([web.view('/api/biosamples/{id}/g_variants', Resultset)])
    app.add_routes([web.view('/api/biosamples/{id}/analyses', Resultset)])
    app.add_routes([web.view('/api/biosamples/{id}/runs', Resultset)])
    app.add_routes([web.view('/api/runs', Resultset)])
    app.add_routes([web.view('/api/runs/{id}', Resultset)])
    app.add_routes([web.view('/api/runs/{id}/analyses', Resultset)])
    app.add_routes([web.view('/api/runs/{id}/g_variants', Resultset)])
    return app

class TestMain(unittest.TestCase):
    def test_main_check_slash_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_slash_endpoint_is_working():
                resp = await client.get("/api")
                assert resp.status == 200
            loop.run_until_complete(test_check_slash_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_slash_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_slash_endpoint_is_working():
                resp = await client.post("/api")
                assert resp.status == 200
            loop.run_until_complete(test_check_post_slash_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_info_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_info_endpoint_is_working():
                resp = await client.get("/api/info")
                assert resp.status == 200
            loop.run_until_complete(test_check_info_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_info_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_info_endpoint_is_working():
                resp = await client.post("/api/info")
                assert resp.status == 200
            loop.run_until_complete(test_check_post_info_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_service_info_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_service_info_endpoint_is_working():
                resp = await client.get("/api/service-info")
                assert resp.status == 200
            loop.run_until_complete(test_check_service_info_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_service_info_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_service_info_endpoint_is_working():
                resp = await client.post("/api/service-info")
                assert resp.status == 200
            loop.run_until_complete(test_check_post_service_info_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_entry_types_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_entry_types_endpoint_is_working():
                resp = await client.get("/api/entry_types")
                assert resp.status == 200
            loop.run_until_complete(test_check_entry_types_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_entry_types_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_entry_types_endpoint_is_working():
                resp = await client.post("/api/entry_types")
                assert resp.status == 200
            loop.run_until_complete(test_check_post_entry_types_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_configuration_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_configuration_endpoint_is_working():
                resp = await client.get("/api/configuration")
                assert resp.status == 200
            loop.run_until_complete(test_check_configuration_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_configuration_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_configuration_endpoint_is_working():
                resp = await client.post("/api/configuration")
                assert resp.status == 200
            loop.run_until_complete(test_check_post_configuration_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_map_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_map_endpoint_is_working():
                resp = await client.get("/api/map")
                assert resp.status == 200
            loop.run_until_complete(test_check_map_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_map_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_map_endpoint_is_working():
                resp = await client.post("/api/map")
                assert resp.status == 200
            loop.run_until_complete(test_check_post_map_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_filtering_terms_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_filtering_terms_endpoint_is_working():
                resp = await client.get("/api/filtering_terms")
                assert resp.status == 200
            loop.run_until_complete(test_check_filtering_terms_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_filtering_terms_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_filtering_terms_endpoint_is_working():
                resp = await client.post("/api/filtering_terms")
                assert resp.status == 200
            loop.run_until_complete(test_check_post_filtering_terms_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_datasets_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_datasets_endpoint_is_working():
                resp = await client.get("/api/datasets")
                assert resp.status == 200
            loop.run_until_complete(test_check_datasets_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_datasets_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_datasets_endpoint_is_working():
                resp = await client.post("/api/datasets")
                assert resp.status == 200
            loop.run_until_complete(test_check_post_datasets_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_g_variants_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_g_variants_endpoint_is_working():
                resp = await client.get("/api/g_variants")
                assert resp.status == 200
            loop.run_until_complete(test_check_g_variants_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_analyses_with_limit_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_analyses_with_limit_endpoint_is_working():
                resp = await client.get("/api/analyses?limit=200")
                assert resp.status == 200
            loop.run_until_complete(test_check_analyses_with_limit_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_analyses_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_analyses_endpoint_is_working():
                resp = await client.get("/api/analyses")
                assert resp.status == 200
            loop.run_until_complete(test_check_analyses_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_analyses_with_id_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_analyses_with_id_endpoint_is_working():
                resp = await client.get("/api/analyses/UK1_analysisId_2")
                assert resp.status == 200
            loop.run_until_complete(test_check_analyses_with_id_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_analyses_g_variants_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_analyses_g_variants_endpoint_is_working():
                resp = await client.get("/api/analyses/UK1_analysisId_2/g_variants")
                assert resp.status == 200
            loop.run_until_complete(test_check_analyses_g_variants_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_biosamples_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_biosamples_endpoint_is_working():
                resp = await client.get("/api/biosamples")
                assert resp.status == 200
            loop.run_until_complete(test_check_biosamples_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_biosamples_with_limit_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_biosamples_with_limit_endpoint_is_working():
                resp = await client.get("/api/biosamples?limit=200")
                assert resp.status == 200
            loop.run_until_complete(test_check_biosamples_with_limit_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_biosamples_with_id_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_biosamples_with_id_endpoint_is_working():
                resp = await client.get("/api/biosamples/HG00097")
                assert resp.status == 200
            loop.run_until_complete(test_check_biosamples_with_id_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_biosamples_g_variants_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_biosamples_g_variants_endpoint_is_working():
                resp = await client.get("/api/biosamples/HG00097/g_variants")
                assert resp.status == 200
            loop.run_until_complete(test_check_biosamples_g_variants_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_biosamples_runs_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_biosamples_runs_endpoint_is_working():
                resp = await client.get("/api/biosamples/HG00097/runs")
                assert resp.status == 200
            loop.run_until_complete(test_check_biosamples_runs_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_biosamples_analyses_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_biosamples_analyses_endpoint_is_working():
                resp = await client.get("/api/biosamples/HG00097/analyses")
                assert resp.status == 200
            loop.run_until_complete(test_check_biosamples_analyses_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_individuals_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_individuals_endpoint_is_working():
                resp = await client.get("/api/individuals")
                assert resp.status == 200
            loop.run_until_complete(test_check_individuals_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_individuals_with_limit_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_individuals_with_limit_endpoint_is_working():
                resp = await client.get("/api/individuals?limit=200")
                assert resp.status == 200
            loop.run_until_complete(test_check_individuals_with_limit_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_individuals_with_id_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_individuals_with_id_endpoint_is_working():
                resp = await client.get("/api/individuals/HG00097")
                assert resp.status == 200
            loop.run_until_complete(test_check_individuals_with_id_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_individuals_g_variants_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_individuals_g_variants_endpoint_is_working():
                resp = await client.get("/api/individuals/HG00097/g_variants")
                assert resp.status == 200
            loop.run_until_complete(test_check_individuals_g_variants_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_individuals_biosamples_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_individuals_biosamples_endpoint_is_working():
                resp = await client.get("/api/individuals/HG00097/biosamples")
                assert resp.status == 200
            loop.run_until_complete(test_check_individuals_biosamples_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_runs_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_runs_endpoint_is_working():
                resp = await client.get("/api/runs")
                assert resp.status == 200
            loop.run_until_complete(test_check_runs_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_runs_with_limit_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_runs_with_limit_endpoint_is_working():
                resp = await client.get("/api/runs?limit=200")
                assert resp.status == 200
            loop.run_until_complete(test_check_runs_with_limit_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_runs_with_id_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_runs_with_id_endpoint_is_working():
                resp = await client.get("/api/runs/SRR00000002")
                assert resp.status == 200
            loop.run_until_complete(test_check_runs_with_id_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_runs_g_variants_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_runs_g_variants_endpoint_is_working():
                resp = await client.get("/api/runs/SRR00000002/g_variants")
                assert resp.status == 200
            loop.run_until_complete(test_check_runs_g_variants_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_runs_analyses_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_runs_analyses_endpoint_is_working():
                resp = await client.get("/api/runs/SRR00000002/analyses")
                assert resp.status == 200
            loop.run_until_complete(test_check_runs_analyses_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cohorts_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cohorts_endpoint_is_working():
                resp = await client.get("/api/cohorts")
                assert resp.status == 200
            loop.run_until_complete(test_check_cohorts_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cohorts_with_limit_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cohorts_with_limit_endpoint_is_working():
                resp = await client.get("/api/cohorts?limit=200")
                assert resp.status == 200
            loop.run_until_complete(test_check_cohorts_with_limit_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cohorts_with_id_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cohorts_with_id_endpoint_is_working():
                resp = await client.get("/api/cohorts/CINECA_synthetic_cohort_UK1")
                assert resp.status == 200
            loop.run_until_complete(test_check_cohorts_with_id_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cohorts_runs_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cohorts_runs_endpoint_is_working():
                resp = await client.get("/api/cohorts/CINECA_synthetic_cohort_UK1/runs")
                assert resp.status == 200
            loop.run_until_complete(test_check_cohorts_runs_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cohorts_biosamples_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cohorts_biosamples_endpoint_is_working():
                resp = await client.get("/api/cohorts/CINECA_synthetic_cohort_UK1/biosamples")
                assert resp.status == 200
            loop.run_until_complete(test_check_cohorts_biosamples_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cohorts_analyses_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cohorts_analyses_endpoint_is_working():
                resp = await client.get("/api/cohorts/CINECA_synthetic_cohort_UK1/analyses")
                assert resp.status == 200
            loop.run_until_complete(test_check_cohorts_analyses_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cohorts_individuals_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cohorts_inividuals_endpoint_is_working():
                resp = await client.get("/api/cohorts/CINECA_synthetic_cohort_UK1/individuals")
                assert resp.status == 200
            loop.run_until_complete(test_check_cohorts_inividuals_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cohorts_g_variants_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cohorts_g_variants_endpoint_is_working():
                resp = await client.get("/api/cohorts/CINECA_synthetic_cohort_UK1/g_variants")
                assert resp.status == 200
            loop.run_until_complete(test_check_cohorts_g_variants_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_datasets_with_limit_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_datasets_with_limit_endpoint_is_working():
                resp = await client.get("/api/datasets?limit=200")
                assert resp.status == 200
            loop.run_until_complete(test_check_datasets_with_limit_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_datasets_with_id_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_datasets_with_id_endpoint_is_working():
                resp = await client.get("/api/datasets/CINECA_synthetic_cohort_EUROPE_UK1")
                assert resp.status == 200
            loop.run_until_complete(test_check_datasets_with_id_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_datasets_runs_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_datasets_runs_endpoint_is_working():
                resp = await client.get("/api/datasets/CINECA_synthetic_cohort_EUROPE_UK1/runs")
                assert resp.status == 200
            loop.run_until_complete(test_check_datasets_runs_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_datasets_g_variants_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_datasets_g_variants_endpoint_is_working():
                resp = await client.get("/api/datasets/CINECA_synthetic_cohort_EUROPE_UK1/g_variants")
                assert resp.status == 200
            loop.run_until_complete(test_check_datasets_g_variants_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_datasets_biosamples_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_datasets_biosamples_endpoint_is_working():
                resp = await client.get("/api/datasets/CINECA_synthetic_cohort_EUROPE_UK1/biosamples")
                assert resp.status == 200
            loop.run_until_complete(test_check_datasets_biosamples_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_datasets_analyses_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_datasets_analyses_endpoint_is_working():
                resp = await client.get("/api/datasets/CINECA_synthetic_cohort_EUROPE_UK1/analyses")
                assert resp.status == 200
            loop.run_until_complete(test_check_datasets_analyses_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_datasets_individuals_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_datasets_inividuals_endpoint_is_working():
                resp = await client.get("/api/datasets/CINECA_synthetic_cohort_EUROPE_UK1/individuals")
                assert resp.status == 200
            loop.run_until_complete(test_check_datasets_inividuals_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_g_variants_with_limit_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_g_variants_with_limit_endpoint_is_working():
                resp = await client.get("/api/g_variants?limit=200")
                assert resp.status == 200
            loop.run_until_complete(test_check_g_variants_with_limit_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_g_variants_with_id_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_g_variants_with_id_endpoint_is_working():
                resp = await client.get("/api/g_variants/da5a95e4-bc26-11ee-b6b0-0242ac170002:A:G")
                assert resp.status == 200
            loop.run_until_complete(test_check_g_variants_with_id_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_g_variants_runs_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_g_variants_runs_endpoint_is_working():
                resp = await client.get("/api/g_variants/da5a95e4-bc26-11ee-b6b0-0242ac170002:A:G/runs")
                assert resp.status == 200
            loop.run_until_complete(test_check_g_variants_runs_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_g_variants_biosamples_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_g_variants_biosamples_endpoint_is_working():
                resp = await client.get("/api/g_variants/da5a95e4-bc26-11ee-b6b0-0242ac170002:A:G/biosamples")
                assert resp.status == 200
            loop.run_until_complete(test_check_g_variants_biosamples_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_g_variants_analyses_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_g_variants_analyses_endpoint_is_working():
                resp = await client.get("/api/g_variants/da5a95e4-bc26-11ee-b6b0-0242ac170002:A:G/analyses")
                assert resp.status == 200
            loop.run_until_complete(test_check_g_variants_analyses_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_g_variants_individuals_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_g_variants_inividuals_endpoint_is_working():
                resp = await client.get("/api/g_variants/da5a95e4-bc26-11ee-b6b0-0242ac170002:A:G/individuals")
                assert resp.status == 200
            loop.run_until_complete(test_check_g_variants_inividuals_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_g_variants_endpoint_NONE_resultSetResponse_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_g_variants_endpoint_NONE_resultSetResponse_is_working():
                resp = await client.get("/api/g_variants?includeResultsetResponses=NONE")
                assert resp.status == 200
            loop.run_until_complete(test_check_g_variants_endpoint_NONE_resultSetResponse_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_g_variants_endpoint_with_parameters_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_g_variants_endpoint_with_parameters_is_working():
                resp = await client.get("/api/g_variants?start=16050074&end=16050075&alternateBases=A&referenceBases=G&referenceName=22")
                assert resp.status == 200
            loop.run_until_complete(test_check_g_variants_endpoint_with_parameters_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_cross_query_individuals_g_variants_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_cross_query_g_variants_individuals_is_working():
                resp = await client.post("/api/g_variants", json={"meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
            {"id":"NCIT:C42331", "scope":"individual"}],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
                })
                assert resp.status == 200
            loop.run_until_complete(test_check_post_cross_query_g_variants_individuals_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_cross_query_individuals_biosamples_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_cross_query_biosamples_individuals_is_working():
                resp = await client.post("/api/biosamples", json={"meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
            {"id":"NCIT:C42331", "scope":"individual"}],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
                })
                eo=await resp.text()
                LOG.debug('ordinary')
                LOG.debug(eo)
                assert resp.status == 200
            loop.run_until_complete(test_check_post_cross_query_biosamples_individuals_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_cross_query_individuals_g_variants_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_individuals_g_variants_is_working():
                resp = await client.post("/api/g_variants", json={"meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
            {"id":"GENO:GENO_0000458", "scope":"genomicVariation"}],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
            })

                assert resp.status == 200
            loop.run_until_complete(test_check_post_individuals_g_variants_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_request_parameters_fail(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_request_parameters_fail():
                resp = await client.get("/api/g_variants?star=12448")
                assert resp.status == 400
            loop.run_until_complete(test_check_request_parameters_fail())
            loop.run_until_complete(client.close())
    def test_main_check_wrong_combination_request_parameters(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_wrong_combination_request_parameters():
                resp = await client.get("/api/g_variants?start=12448")
                assert resp.status == 400
            loop.run_until_complete(test_wrong_combination_request_parameters())
            loop.run_until_complete(client.close())
    def test_main_check_datasets_g_variants_endpoint_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_datasets_g_variants_endpoint_is_working():
                resp = await client.get("/api/g_variants?datasets=CINECA_synthetic_cohort_EUROPE_UK1")
                assert resp.status == 200
            loop.run_until_complete(test_check_datasets_g_variants_endpoint_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'ethnicity.id': 'NCIT:C42331'}]}, 'individual', 'biosamples', {})
                assert resp == {'$or': [{'individualId': 'HG00096'}, {'individualId': 'HG00109'}, {'individualId': 'HG00154'}, {'individualId': 'HG00179'}, {'individualId': 'HG00187'}, {'individualId': 'HG00274'}, {'individualId': 'HG00277'}, {'individualId': 'HG00344'}, {'individualId': 'HG00382'}, {'individualId': 'HG00383'}, {'individualId': 'HG00458'}, {'individualId': 'HG00556'}, {'individualId': 'HG00557'}, {'individualId': 'HG00613'}, {'individualId': 'HG00614'}, {'individualId': 'HG00629'}, {'individualId': 'HG00580'}, {'individualId': 'HG00654'}, {'individualId': 'HG00671'}, {'individualId': 'HG00641'}, {'individualId': 'HG00743'}, {'individualId': 'HG01063'}, {'individualId': 'HG01098'}, {'individualId': 'HG01139'}, {'individualId': 'HG01183'}, {'individualId': 'HG01341'}, {'individualId': 'HG01374'}, {'individualId': 'HG01465'}, {'individualId': 'HG01489'}, {'individualId': 'HG01507'}, {'individualId': 'HG01586'}, {'individualId': 'HG01673'}, {'individualId': 'HG01675'}, {'individualId': 'HG01765'}, {'individualId': 'HG01802'}, {'individualId': 'HG01806'}, {'individualId': 'HG01844'}, {'individualId': 'HG01795'}, {'individualId': 'HG01869'}, {'individualId': 'HG01965'}, {'individualId': 'HG02054'}, {'individualId': 'HG02073'}, {'individualId': 'HG02090'}, {'individualId': 'HG02143'}, {'individualId': 'HG02230'}, {'individualId': 'HG02274'}, {'individualId': 'HG02266'}, {'individualId': 'HG02309'}, {'individualId': 'HG02323'}, {'individualId': 'HG02334'}, {'individualId': 'HG02190'}, {'individualId': 'HG02470'}, {'individualId': 'HG02479'}, {'individualId': 'HG02484'}, {'individualId': 'HG02485'}, {'individualId': 'HG02601'}, {'individualId': 'HG02624'}, {'individualId': 'HG02687'}, {'individualId': 'HG02700'}, {'individualId': 'HG02786'}, {'individualId': 'HG02769'}, {'individualId': 'HG02839'}, {'individualId': 'HG02977'}, {'individualId': 'HG03040'}, {'individualId': 'HG03091'}, {'individualId': 'HG03074'}, {'individualId': 'HG03118'}, {'individualId': 'HG03166'}, {'individualId': 'HG03238'}, {'individualId': 'HG03240'}, {'individualId': 'HG03343'}, {'individualId': 'HG03548'}, {'individualId': 'HG03575'}, {'individualId': 'HG03685'}, {'individualId': 'HG03691'}, {'individualId': 'HG03731'}, {'individualId': 'HG03760'}, {'individualId': 'HG03796'}, {'individualId': 'HG03786'}, {'individualId': 'HG03870'}, {'individualId': 'HG03873'}, {'individualId': 'HG03896'}, {'individualId': 'HG03898'}, {'individualId': 'HG03941'}, {'individualId': 'HG04014'}, {'individualId': 'HG04140'}, {'individualId': 'HG04159'}, {'individualId': 'HG04206'}, {'individualId': 'NA11831'}, {'individualId': 'NA12234'}, {'individualId': 'NA12341'}, {'individualId': 'NA12347'}, {'individualId': 'NA12718'}, {'individualId': 'NA12874'}, {'individualId': 'NA18563'}, {'individualId': 'NA18582'}, {'individualId': 'NA18609'}, {'individualId': 'NA18626'}, {'individualId': 'NA18643'}, {'individualId': 'NA18631'}, {'individualId': 'NA18861'}, {'individualId': 'NA18951'}, {'individualId': 'NA18978'}, {'individualId': 'NA18986'}, {'individualId': 'NA18993'}, {'individualId': 'NA19149'}, {'individualId': 'NA19223'}, {'individualId': 'NA19225'}, {'individualId': 'NA19332'}, {'individualId': 'NA19438'}, {'individualId': 'NA19719'}, {'individualId': 'NA19759'}, {'individualId': 'NA19916'}, {'individualId': 'NA20512'}, {'individualId': 'NA20538'}, {'individualId': 'NA20756'}, {'individualId': 'NA20772'}, {'individualId': 'NA20806'}, {'individualId': 'NA20870'}]}
            loop.run_until_complete(test_check_cross_query_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_2_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_2_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'caseLevelData.zygosity.id': 'GENO:GENO_0000458'}]}, 'genomicVariation', 'g_variants', {})
                assert resp == {'$or': [{'caseLevelData.zygosity.id': 'GENO:GENO_0000458'}]}
            loop.run_until_complete(test_check_cross_query_2_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_3_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_3_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'ethnicity.id': 'NCIT:C42331'}]}, 'individual', 'g_variants', {})
                assert resp == {'$or': [{'caseLevelData.biosampleId': 'HG00096'}, {'caseLevelData.biosampleId': 'HG00109'}, {'caseLevelData.biosampleId': 'HG00154'}, {'caseLevelData.biosampleId': 'HG00179'}, {'caseLevelData.biosampleId': 'HG00187'}, {'caseLevelData.biosampleId': 'HG00274'}, {'caseLevelData.biosampleId': 'HG00277'}, {'caseLevelData.biosampleId': 'HG00344'}, {'caseLevelData.biosampleId': 'HG00382'}, {'caseLevelData.biosampleId': 'HG00383'}, {'caseLevelData.biosampleId': 'HG00458'}, {'caseLevelData.biosampleId': 'HG00557'}, {'caseLevelData.biosampleId': 'HG00556'}, {'caseLevelData.biosampleId': 'HG00580'}, {'caseLevelData.biosampleId': 'HG00613'}, {'caseLevelData.biosampleId': 'HG00614'}, {'caseLevelData.biosampleId': 'HG00641'}, {'caseLevelData.biosampleId': 'HG00654'}, {'caseLevelData.biosampleId': 'HG00671'}, {'caseLevelData.biosampleId': 'HG00629'}, {'caseLevelData.biosampleId': 'HG00743'}, {'caseLevelData.biosampleId': 'HG01063'}, {'caseLevelData.biosampleId': 'HG01098'}, {'caseLevelData.biosampleId': 'HG01139'}, {'caseLevelData.biosampleId': 'HG01183'}, {'caseLevelData.biosampleId': 'HG01341'}, {'caseLevelData.biosampleId': 'HG01374'}, {'caseLevelData.biosampleId': 'HG01465'}, {'caseLevelData.biosampleId': 'HG01507'}, {'caseLevelData.biosampleId': 'HG01489'}, {'caseLevelData.biosampleId': 'HG01586'}, {'caseLevelData.biosampleId': 'HG01673'}, {'caseLevelData.biosampleId': 'HG01675'}, {'caseLevelData.biosampleId': 'HG01765'}, {'caseLevelData.biosampleId': 'HG01795'}, {'caseLevelData.biosampleId': 'HG01802'}, {'caseLevelData.biosampleId': 'HG01806'}, {'caseLevelData.biosampleId': 'HG01844'}, {'caseLevelData.biosampleId': 'HG01869'}, {'caseLevelData.biosampleId': 'HG01965'}, {'caseLevelData.biosampleId': 'HG02054'}, {'caseLevelData.biosampleId': 'HG02073'}, {'caseLevelData.biosampleId': 'HG02090'}, {'caseLevelData.biosampleId': 'HG02143'}, {'caseLevelData.biosampleId': 'HG02190'}, {'caseLevelData.biosampleId': 'HG02230'}, {'caseLevelData.biosampleId': 'HG02266'}, {'caseLevelData.biosampleId': 'HG02274'}, {'caseLevelData.biosampleId': 'HG02323'}, {'caseLevelData.biosampleId': 'HG02309'}, {'caseLevelData.biosampleId': 'HG02334'}, {'caseLevelData.biosampleId': 'HG02470'}, {'caseLevelData.biosampleId': 'HG02479'}, {'caseLevelData.biosampleId': 'HG02484'}, {'caseLevelData.biosampleId': 'HG02485'}, {'caseLevelData.biosampleId': 'HG02601'}, {'caseLevelData.biosampleId': 'HG02624'}, {'caseLevelData.biosampleId': 'HG02687'}, {'caseLevelData.biosampleId': 'HG02700'}, {'caseLevelData.biosampleId': 'HG02786'}, {'caseLevelData.biosampleId': 'HG02769'}, {'caseLevelData.biosampleId': 'HG02839'}, {'caseLevelData.biosampleId': 'HG02977'}, {'caseLevelData.biosampleId': 'HG03040'}, {'caseLevelData.biosampleId': 'HG03091'}, {'caseLevelData.biosampleId': 'HG03074'}, {'caseLevelData.biosampleId': 'HG03118'}, {'caseLevelData.biosampleId': 'HG03166'}, {'caseLevelData.biosampleId': 'HG03238'}, {'caseLevelData.biosampleId': 'HG03240'}, {'caseLevelData.biosampleId': 'HG03343'}, {'caseLevelData.biosampleId': 'HG03548'}, {'caseLevelData.biosampleId': 'HG03575'}, {'caseLevelData.biosampleId': 'HG03691'}, {'caseLevelData.biosampleId': 'HG03685'}, {'caseLevelData.biosampleId': 'HG03731'}, {'caseLevelData.biosampleId': 'HG03760'}, {'caseLevelData.biosampleId': 'HG03786'}, {'caseLevelData.biosampleId': 'HG03796'}, {'caseLevelData.biosampleId': 'HG03873'}, {'caseLevelData.biosampleId': 'HG03896'}, {'caseLevelData.biosampleId': 'HG03898'}, {'caseLevelData.biosampleId': 'HG03870'}, {'caseLevelData.biosampleId': 'HG03941'}, {'caseLevelData.biosampleId': 'HG04014'}, {'caseLevelData.biosampleId': 'HG04140'}, {'caseLevelData.biosampleId': 'HG04159'}, {'caseLevelData.biosampleId': 'HG04206'}, {'caseLevelData.biosampleId': 'NA11831'}, {'caseLevelData.biosampleId': 'NA12234'}, {'caseLevelData.biosampleId': 'NA12341'}, {'caseLevelData.biosampleId': 'NA12347'}, {'caseLevelData.biosampleId': 'NA12718'}, {'caseLevelData.biosampleId': 'NA12874'}, {'caseLevelData.biosampleId': 'NA18563'}, {'caseLevelData.biosampleId': 'NA18582'}, {'caseLevelData.biosampleId': 'NA18609'}, {'caseLevelData.biosampleId': 'NA18626'}, {'caseLevelData.biosampleId': 'NA18631'}, {'caseLevelData.biosampleId': 'NA18643'}, {'caseLevelData.biosampleId': 'NA18861'}, {'caseLevelData.biosampleId': 'NA18951'}, {'caseLevelData.biosampleId': 'NA18978'}, {'caseLevelData.biosampleId': 'NA18993'}, {'caseLevelData.biosampleId': 'NA18986'}, {'caseLevelData.biosampleId': 'NA19149'}, {'caseLevelData.biosampleId': 'NA19223'}, {'caseLevelData.biosampleId': 'NA19225'}, {'caseLevelData.biosampleId': 'NA19332'}, {'caseLevelData.biosampleId': 'NA19438'}, {'caseLevelData.biosampleId': 'NA19719'}, {'caseLevelData.biosampleId': 'NA19759'}, {'caseLevelData.biosampleId': 'NA19916'}, {'caseLevelData.biosampleId': 'NA20512'}, {'caseLevelData.biosampleId': 'NA20538'}, {'caseLevelData.biosampleId': 'NA20756'}, {'caseLevelData.biosampleId': 'NA20772'}, {'caseLevelData.biosampleId': 'NA20870'}, {'caseLevelData.biosampleId': 'NA20806'}]}
            loop.run_until_complete(test_check_cross_query_3_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_4_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_4_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'caseLevelData.zygosity.id': 'GENO:GENO_0000458'}]}, 'genomicVariation', 'g_variants', {'$and': [{'variation.location.interval.start.value': {'$gte': 16050074}}, {'variation.location.interval.end.value': {'$lte': 16050075}}, {'variation.alternateBases': {'$eq': 'A'}}, {'variation.referenceBases': {'$eq': 'G'}}, {'$and': [{'$or': [{'identifiers.genomicHGVSId': {'$regex': '^NC_000022'}}]}]}]})
                assert resp == {'$or': [{'caseLevelData.zygosity.id': 'GENO:GENO_0000458'}], '$and': [{'$or': [{'caseLevelData.biosampleId': 'HG03771'}]}]}
            loop.run_until_complete(test_check_cross_query_4_is_working())
            loop.run_until_complete(client.close())



if __name__ == '__main__':
    unittest.main()


