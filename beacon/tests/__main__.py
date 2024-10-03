
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
from beacon.connections.mongo.filters import cross_query, apply_filters
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
    def test_main_check_datasets_g_variants_2_endpoint_is_working(self):
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
                assert resp.status == 200
            loop.run_until_complete(test_check_post_cross_query_biosamples_individuals_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_post_cross_query_individuals_2_g_variants_is_working(self):
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
            loop.run_until_complete(client.close())# pragma: no cover
    def test_main_check_wrong_combination_request_parameters(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_wrong_combination_request_parameters():
                resp = await client.get("/api/g_variants?start=12448")
                assert resp.status == 400
            loop.run_until_complete(test_wrong_combination_request_parameters())
            loop.run_until_complete(client.close())# pragma: no cover
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
                assert resp != {}
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
                assert resp != {}
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
    def test_main_check_cross_query_5_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_5_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'caseLevelData.zygosity.id': 'GENO:GENO_0000458'}]}, 'genomicVariation', 'individuals', {'$and': [{'variation.location.interval.start.value': {'$gte': 16050074}}, {'variation.location.interval.end.value': {'$lte': 16050075}}, {'variation.alternateBases': {'$eq': 'A'}}, {'variation.referenceBases': {'$eq': 'G'}}, {'$and': [{'$or': [{'identifiers.genomicHGVSId': {'$regex': '^NC_000022'}}]}]}]})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_5_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_6_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_6_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'caseLevelData.zygosity.id': 'GENO:GENO_0000458'}]}, 'genomicVariation', 'biosamples', {'$and': [{'variation.location.interval.start.value': {'$gte': 16050074}}, {'variation.location.interval.end.value': {'$lte': 16050075}}, {'variation.alternateBases': {'$eq': 'A'}}, {'variation.referenceBases': {'$eq': 'G'}}, {'$and': [{'$or': [{'identifiers.genomicHGVSId': {'$regex': '^NC_000022'}}]}]}]})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_6_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_7_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_7_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'platformModel.id': 'OBI:0002048'}]}, 'run', 'individuals', {})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_7_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_8_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_8_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'platformModel.id': 'OBI:0002048'}]}, 'run', 'biosamples', {})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_8_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_9_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_9_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'platformModel.id': 'OBI:0002048'}]}, 'run', 'g_variants', {})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_9_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_10_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_10_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'platformModel.id': 'OBI:0002048'}]}, 'run', 'analyses', {})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_10_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_11_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_11_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'sampleOriginType.id': 'UBERON:0000178'}, {'sampleOriginType.id': 'MONDO:0013512'}, {'sampleOriginType.id': 'CL:0000232'}, {'sampleOriginType.id': 'EFO:0004842'}, {'sampleOriginType.id': 'EFO:0007988'}, {'sampleOriginType.id': 'EFO:0004808'}, {'sampleOriginType.id': 'MONDO:0009950'}, {'sampleOriginType.id': 'EFO:0009244'}, {'sampleOriginType.id': 'EFO:0009253'}, {'sampleOriginType.id': 'EFO:0010783'}, {'sampleOriginType.id': 'EFO:0003073'}, {'sampleOriginType.id': 'EFO:0009252'}, {'sampleOriginType.id': 'MONDO:0001117'}, {'sampleOriginType.id': 'MONDO:0018022'}, {'sampleOriginType.id': 'EFO:0010109'}, {'sampleOriginType.id': 'EFO:0010840'}, {'sampleOriginType.id': 'EFO:0010792'}, {'sampleOriginType.id': 'EFO:0005090'}, {'sampleOriginType.id': 'EFO:0010772'}, {'sampleOriginType.id': 'MONDO:0017829'}, {'sampleOriginType.id': 'EFO:0001941'}, {'sampleOriginType.id': 'EFO:0010790'}, {'sampleOriginType.id': 'EFO:0010861'}, {'sampleOriginType.id': 'MONDO:0018749'}, {'sampleOriginType.id': 'EFO:0010849'}, {'sampleOriginType.id': 'EFO:1001467'}, {'sampleOriginType.id': 'MONDO:0017238'}, {'sampleOriginType.id': 'EFO:0007129'}, {'sampleOriginType.id': 'MONDO:0011136'}, {'sampleOriginType.id': 'Orphanet:231242'}, {'sampleOriginType.id': 'EFO:0007481'}, {'sampleOriginType.id': 'EFO:0009215'}, {'sampleOriginType.id': 'MONDO:0017145'}, {'sampleOriginType.id': 'CL:0000775'}, {'sampleOriginType.id': 'MONDO:0008555'}, {'sampleOriginType.id': 'MONDO:0004680'}, {'sampleOriginType.id': 'EFO:0004305'}, {'sampleOriginType.id': 'MONDO:0016490'}, {'sampleOriginType.id': 'MONDO:0007838'}, {'sampleOriginType.id': 'MONDO:0013016'}, {'sampleOriginType.id': 'EFO:0007994'}, {'sampleOriginType.id': 'MONDO:0013623'}, {'sampleOriginType.id': 'CL:0000614'}, {'sampleOriginType.id': 'EFO:0010107'}, {'sampleOriginType.id': 'CL:0000976'}, {'sampleOriginType.id': 'EFO:0009225'}, {'sampleOriginType.id': 'CL:0002318'}, {'sampleOriginType.id': 'EFO:0004309'}, {'sampleOriginType.id': 'EFO:0004526'}, {'sampleOriginType.id': 'EFO:0010843'}, {'sampleOriginType.id': 'CL:0002155'}, {'sampleOriginType.id': 'EFO:0010796'}, {'sampleOriginType.id': 'EFO:0001378'}, {'sampleOriginType.id': 'EFO:0009209'}, {'sampleOriginType.id': 'EFO:0009224'}, {'sampleOriginType.id': 'EFO:0009210'}, {'sampleOriginType.id': 'MONDO:0016489'}, {'sampleOriginType.id': 'EFO:0010781'}, {'sampleOriginType.id': 'Orphanet:98791'}, {'sampleOriginType.id': 'EFO:0600063'}, {'sampleOriginType.id': 'CL:0000580'}, {'sampleOriginType.id': 'EFO:0009226'}, {'sampleOriginType.id': 'EFO:0008542'}, {'sampleOriginType.id': 'EFO:0009236'}, {'sampleOriginType.id': 'MONDO:0018269'}, {'sampleOriginType.id': 'MONDO:0016669'}, {'sampleOriginType.id': 'EFO:0004637'}, {'sampleOriginType.id': 'EFO:0010801'}, {'sampleOriginType.id': 'CL:0000978'}, {'sampleOriginType.id': 'Orphanet:846'}, {'sampleOriginType.id': 'EFO:0007445'}, {'sampleOriginType.id': 'EFO:0009239'}, {'sampleOriginType.id': 'CL:0000774'}, {'sampleOriginType.id': 'Orphanet:330032'}, {'sampleOriginType.id': 'MONDO:0019537'}, {'sampleOriginType.id': 'EFO:0010793'}, {'sampleOriginType.id': 'EFO:0009132'}, {'sampleOriginType.id': 'MONDO:0013517'}, {'sampleOriginType.id': 'EFO:0009218'}, {'sampleOriginType.id': 'MONDO:0018963'}, {'sampleOriginType.id': 'EFO:0010799'}, {'sampleOriginType.id': 'MONDO:0012354'}, {'sampleOriginType.id': 'EFO:0010860'}, {'sampleOriginType.id': 'EFO:0007989'}, {'sampleOriginType.id': 'EFO:0010835'}, {'sampleOriginType.id': 'MONDO:0011603'}, {'sampleOriginType.id': 'CL:0000975'}, {'sampleOriginType.id': 'Orphanet:168615'}, {'sampleOriginType.id': 'MONDO:0019535'}, {'sampleOriginType.id': 'CL:0000770'}, {'sampleOriginType.id': 'EFO:0010108'}, {'sampleOriginType.id': 'EFO:0010884'}, {'sampleOriginType.id': 'EFO:0010867'}, {'sampleOriginType.id': 'EFO:0009246'}, {'sampleOriginType.id': 'EFO:0009219'}, {'sampleOriginType.id': 'EFO:0010856'}, {'sampleOriginType.id': 'MONDO:0044349'}, {'sampleOriginType.id': 'EFO:0004584'}, {'sampleOriginType.id': 'MONDO:0018794'}, {'sampleOriginType.id': 'EFO:0007993'}, {'sampleOriginType.id': 'EFO:0009220'}, {'sampleOriginType.id': 'EFO:0010881'}, {'sampleOriginType.id': 'MONDO:0100326'}, {'sampleOriginType.id': 'EFO:0010768'}, {'sampleOriginType.id': 'EFO:0010862'}, {'sampleOriginType.id': 'MONDO:0000105'}, {'sampleOriginType.id': 'MONDO:0019050'}, {'sampleOriginType.id': 'MONDO:0010122'}, {'sampleOriginType.id': 'EFO:0009238'}, {'sampleOriginType.id': 'MONDO:0019098'}, {'sampleOriginType.id': 'EFO:1001316'}, {'sampleOriginType.id': 'EFO:0009646'}, {'sampleOriginType.id': 'MONDO:0016671'}, {'sampleOriginType.id': 'MONDO:0010308'}, {'sampleOriginType.id': 'MONDO:0008369'}, {'sampleOriginType.id': 'EFO:0004310'}, {'sampleOriginType.id': 'EFO:0010780'}, {'sampleOriginType.id': 'EFO:0006613'}, {'sampleOriginType.id': 'EFO:0008447'}, {'sampleOriginType.id': 'EFO:0008543'}, {'sampleOriginType.id': 'EFO:0010770'}, {'sampleOriginType.id': 'CL:0000977'}, {'sampleOriginType.id': 'EFO:0010887'}, {'sampleOriginType.id': 'EFO:0004629'}, {'sampleOriginType.id': 'MONDO:0018740'}, {'sampleOriginType.id': 'EFO:0010853'}, {'sampleOriginType.id': 'MONDO:0009490'}, {'sampleOriginType.id': 'EFO:0010791'}, {'sampleOriginType.id': 'EFO:0010847'}, {'sampleOriginType.id': 'EFO:0010775'}, {'sampleOriginType.id': 'EFO:0009245'}, {'sampleOriginType.id': 'EFO:0010763'}, {'sampleOriginType.id': 'EFO:0700023'}, {'sampleOriginType.id': 'EFO:0010970'}, {'sampleOriginType.id': 'EFO:0010764'}, {'sampleOriginType.id': 'EFO:0600062'}, {'sampleOriginType.id': 'CL:0000776'}, {'sampleOriginType.id': 'EFO:1001115'}, {'sampleOriginType.id': 'MONDO:0016672'}, {'sampleOriginType.id': 'EFO:0004634'}, {'sampleOriginType.id': 'EFO:0004528'}, {'sampleOriginType.id': 'EFO:0009390'}, {'sampleOriginType.id': 'MONDO:0015579'}, {'sampleOriginType.id': 'EFO:0700066'}, {'sampleOriginType.id': 'EFO:0007987'}, {'sampleOriginType.id': 'MONDO:0014078'}, {'sampleOriginType.id': 'EFO:0006530'}, {'sampleOriginType.id': 'MONDO:0019111'}, {'sampleOriginType.id': 'MONDO:0016360'}, {'sampleOriginType.id': 'EFO:0009250'}, {'sampleOriginType.id': 'MONDO:0015372'}, {'sampleOriginType.id': 'MONDO:0016491'}, {'sampleOriginType.id': 'EFO:0009221'}, {'sampleOriginType.id': 'CL:0000986'}, {'sampleOriginType.id': 'MONDO:0020117'}, {'sampleOriginType.id': 'EFO:0004619'}, {'sampleOriginType.id': 'Orphanet:231386'}, {'sampleOriginType.id': 'EFO:0002339'}, {'sampleOriginType.id': 'EFO:0010774'}, {'sampleOriginType.id': 'EFO:0007990'}, {'sampleOriginType.id': 'EFO:0022585'}, {'sampleOriginType.id': 'EFO:0010778'}, {'sampleOriginType.id': 'MONDO:0007293'}, {'sampleOriginType.id': 'EFO:0004633'}, {'sampleOriginType.id': 'EFO:1001996'}, {'sampleOriginType.id': 'EFO:0008446'}, {'sampleOriginType.id': 'EFO:0002322'}, {'sampleOriginType.id': 'UBERON:0001969'}, {'sampleOriginType.id': 'CL:0000985'}, {'sampleOriginType.id': 'EFO:0009181'}, {'sampleOriginType.id': 'CL:0000974'}, {'sampleOriginType.id': 'CL:0000951'}, {'sampleOriginType.id': 'EFO:0010105'}, {'sampleOriginType.id': 'EFO:0009249'}, {'sampleOriginType.id': 'EFO:0803346'}, {'sampleOriginType.id': 'EFO:0005845'}, {'sampleOriginType.id': 'EFO:0010880'}, {'sampleOriginType.id': 'MONDO:0044347'}, {'sampleOriginType.id': 'EFO:0007615'}, {'sampleOriginType.id': 'EFO:0010788'}, {'sampleOriginType.id': 'MONDO:0018922'}, {'sampleOriginType.id': 'MONDO:0016630'}, {'sampleOriginType.id': 'EFO:0007978'}, {'sampleOriginType.id': 'EFO:0010855'}, {'sampleOriginType.id': 'EFO:0006609'}, {'sampleOriginType.id': 'EFO:0006617'}, {'sampleOriginType.id': 'EFO:0010859'}, {'sampleOriginType.id': 'EFO:0009202'}, {'sampleOriginType.id': 'MONDO:0012775'}, {'sampleOriginType.id': 'EFO:0008582'}, {'sampleOriginType.id': 'EFO:0009230'}, {'sampleOriginType.id': 'EFO:0009498'}, {'sampleOriginType.id': 'EFO:0000777'}, {'sampleOriginType.id': 'EFO:0010800'}, {'sampleOriginType.id': 'EFO:0001253'}, {'sampleOriginType.id': 'EFO:0010782'}, {'sampleOriginType.id': 'EFO:0010890'}, {'sampleOriginType.id': 'EFO:0004536'}, {'sampleOriginType.id': 'MONDO:0009694'}, {'sampleOriginType.id': 'MONDO:0043768'}, {'sampleOriginType.id': 'EFO:0010837'}, {'sampleOriginType.id': 'EFO:0010857'}, {'sampleOriginType.id': 'EFO:0004630'}, {'sampleOriginType.id': 'EFO:0009229'}, {'sampleOriginType.id': 'EFO:0009214'}, {'sampleOriginType.id': 'CL:0000392'}, {'sampleOriginType.id': 'MONDO:0008332'}, {'sampleOriginType.id': 'EFO:0006616'}, {'sampleOriginType.id': 'EFO:0006619'}, {'sampleOriginType.id': 'MONDO:0800452'}, {'sampleOriginType.id': 'EFO:0009388'}, {'sampleOriginType.id': 'EFO:0009216'}, {'sampleOriginType.id': 'EFO:0009247'}, {'sampleOriginType.id': 'MONDO:0001909'}, {'sampleOriginType.id': 'MONDO:0001197'}, {'sampleOriginType.id': 'EFO:0009217'}, {'sampleOriginType.id': 'EFO:0007995'}, {'sampleOriginType.id': 'Orphanet:231249'}, {'sampleOriginType.id': 'EFO:0010789'}, {'sampleOriginType.id': 'Orphanet:231393'}, {'sampleOriginType.id': 'Orphanet:168612'}, {'sampleOriginType.id': 'EFO:0009389'}, {'sampleOriginType.id': 'MONDO:0011381'}, {'sampleOriginType.id': 'EFO:0022042'}, {'sampleOriginType.id': 'MONDO:0008497'}, {'sampleOriginType.id': 'CL:0000595'}, {'sampleOriginType.id': 'MONDO:0011382'}, {'sampleOriginType.id': 'MONDO:0012031'}, {'sampleOriginType.id': 'EFO:0010883'}, {'sampleOriginType.id': 'EFO:0010851'}, {'sampleOriginType.id': 'EFO:0004640'}, {'sampleOriginType.id': 'MONDO:0018896'}, {'sampleOriginType.id': 'EFO:0010845'}, {'sampleOriginType.id': 'EFO:0004623'}, {'sampleOriginType.id': 'MONDO:0009276'}, {'sampleOriginType.id': 'EFO:0022508'}, {'sampleOriginType.id': 'MONDO:0016668'}, {'sampleOriginType.id': 'GO:0070527'}, {'sampleOriginType.id': 'EFO:0010878'}, {'sampleOriginType.id': 'CL:0000987'}, {'sampleOriginType.id': 'Orphanet:231401'}, {'sampleOriginType.id': 'MONDO:0008553'}, {'sampleOriginType.id': 'EFO:0001219'}, {'sampleOriginType.id': 'EFO:0004541'}, {'sampleOriginType.id': 'EFO:0600027'}, {'sampleOriginType.id': 'EFO:0022579'}, {'sampleOriginType.id': 'EFO:0002207'}, {'sampleOriginType.id': 'CL:0000560'}, {'sampleOriginType.id': 'EFO:0004308'}, {'sampleOriginType.id': 'CL:0000773'}, {'sampleOriginType.id': 'EFO:0009223'}, {'sampleOriginType.id': 'EFO:0004586'}, {'sampleOriginType.id': 'MONDO:0011399'}, {'sampleOriginType.id': 'EFO:0010873'}, {'sampleOriginType.id': 'EFO:0009251'}, {'sampleOriginType.id': 'EFO:0007160'}, {'sampleOriginType.id': 'CL:0000041'}, {'sampleOriginType.id': 'EFO:1001200'}, {'sampleOriginType.id': 'MONDO:0018268'}, {'sampleOriginType.id': 'MONDO:0044635'}, {'sampleOriginType.id': 'EFO:0010844'}, {'sampleOriginType.id': 'EFO:0006552'}, {'sampleOriginType.id': 'EFO:0006654'}, {'sampleOriginType.id': 'EFO:0010882'}, {'sampleOriginType.id': 'EFO:0001068'}, {'sampleOriginType.id': 'MONDO:0000009'}, {'sampleOriginType.id': 'EFO:0006618'}, {'sampleOriginType.id': 'EFO:0010872'}, {'sampleOriginType.id': 'CL:0000043'}, {'sampleOriginType.id': 'MONDO:0011422'}, {'sampleOriginType.id': 'MONDO:0011268'}, {'sampleOriginType.id': 'EFO:0010854'}, {'sampleOriginType.id': 'CL:0000387'}, {'sampleOriginType.id': 'EFO:0006611'}, {'sampleOriginType.id': 'EFO:0010836'}, {'sampleOriginType.id': 'MONDO:0030867'}, {'sampleOriginType.id': 'EFO:0010762'}, {'sampleOriginType.id': 'EFO:0006612'}, {'sampleOriginType.id': 'EFO:0007629'}, {'sampleOriginType.id': 'UBERON:0012168'}, {'sampleOriginType.id': 'EFO:0004576'}, {'sampleOriginType.id': 'CL:0000786'}, {'sampleOriginType.id': 'EFO:0009232'}, {'sampleOriginType.id': 'EFO:1001112'}, {'sampleOriginType.id': 'EFO:0010839'}, {'sampleOriginType.id': 'MONDO:0014536'}, {'sampleOriginType.id': 'EFO:0004833'}, {'sampleOriginType.id': 'EFO:0010106'}, {'sampleOriginType.id': 'EFO:0006716'}, {'sampleOriginType.id': 'EFO:0010875'}, {'sampleOriginType.id': 'EFO:0009231'}, {'sampleOriginType.id': 'MONDO:0011988'}, {'sampleOriginType.id': 'MONDO:0011555'}, {'sampleOriginType.id': 'EFO:0010786'}, {'sampleOriginType.id': 'MONDO:0016487'}, {'sampleOriginType.id': 'EFO:0006857'}, {'sampleOriginType.id': 'MONDO:0016670'}, {'sampleOriginType.id': 'EFO:0009205'}, {'sampleOriginType.id': 'CL:0000947'}, {'sampleOriginType.id': 'EFO:0004304'}, {'sampleOriginType.id': 'MONDO:0002249'}, {'sampleOriginType.id': 'EFO:0008087'}, {'sampleOriginType.id': 'EFO:0009208'}, {'sampleOriginType.id': 'MONDO:0018795'}, {'sampleOriginType.id': 'EFO:0022513'}, {'sampleOriginType.id': 'EFO:0010841'}, {'sampleOriginType.id': 'EFO:0600058'}, {'sampleOriginType.id': 'MONDO:0016450'}, {'sampleOriginType.id': 'EFO:0010869'}, {'sampleOriginType.id': 'EFO:0005091'}, {'sampleOriginType.id': 'EFO:0006553'}, {'sampleOriginType.id': 'EFO:0600059'}, {'sampleOriginType.id': 'EFO:1000641'}, {'sampleOriginType.id': 'MONDO:0010743'}, {'sampleOriginType.id': 'EFO:0007997'}, {'sampleOriginType.id': 'EFO:0010803'}, {'sampleOriginType.id': 'EFO:0009235'}, {'sampleOriginType.id': 'MONDO:0009885'}, {'sampleOriginType.id': 'EFO:0010798'}, {'sampleOriginType.id': 'EFO:0009228'}, {'sampleOriginType.id': 'HP:0003530'}, {'sampleOriginType.id': 'MONDO:0002245'}, {'sampleOriginType.id': 'EFO:0010877'}, {'sampleOriginType.id': 'EFO:0010797'}, {'sampleOriginType.id': 'EFO:0009497'}, {'sampleOriginType.id': 'MONDO:0010480'}, {'sampleOriginType.id': 'EFO:0009133'}, {'sampleOriginType.id': 'EFO:0010766'}, {'sampleOriginType.id': 'EFO:0600060'}, {'sampleOriginType.id': 'CL:0000390'}, {'sampleOriginType.id': 'EFO:0010885'}, {'sampleOriginType.id': 'EFO:1001264'}, {'sampleOriginType.id': 'EFO:0007985'}, {'sampleOriginType.id': 'EFO:0004509'}, {'sampleOriginType.id': 'CL:0000096'}, {'sampleOriginType.id': 'EFO:0600061'}, {'sampleOriginType.id': 'EFO:0020902'}, {'sampleOriginType.id': 'EFO:0009237'}, {'sampleOriginType.id': 'EFO:0009227'}, {'sampleOriginType.id': 'EFO:0010777'}, {'sampleOriginType.id': 'EFO:0009188'}, {'sampleOriginType.id': 'EFO:0009241'}, {'sampleOriginType.id': 'CL:0000612'}, {'sampleOriginType.id': 'EFO:0009134'}, {'sampleOriginType.id': 'MONDO:0008557'}, {'sampleOriginType.id': 'MONDO:0014518'}, {'sampleOriginType.id': 'EFO:0009242'}, {'sampleOriginType.id': 'CL:0000233'}, {'sampleOriginType.id': 'MONDO:0030827'}, {'sampleOriginType.id': 'EFO:0004301'}, {'sampleOriginType.id': 'Orphanet:46532'}, {'sampleOriginType.id': 'MONDO:0031332'}, {'sampleOriginType.id': 'MONDO:0019402'}, {'sampleOriginType.id': 'EFO:0009211'}, {'sampleOriginType.id': 'MONDO:0011173'}, {'sampleOriginType.id': 'EFO:0009212'}, {'sampleOriginType.id': 'HP:0003146'}, {'sampleOriginType.id': 'MONDO:0044348'}, {'sampleOriginType.id': 'MONDO:0100241'}, {'sampleOriginType.id': 'EFO:0005576'}, {'sampleOriginType.id': 'EFO:0010863'}, {'sampleOriginType.id': 'EFO:0004527'}, {'sampleOriginType.id': 'EFO:0009213'}, {'sampleOriginType.id': 'EFO:0010858'}, {'sampleOriginType.id': 'EFO:0010776'}, {'sampleOriginType.id': 'EFO:0009243'}, {'sampleOriginType.id': 'EFO:0010761'}, {'sampleOriginType.id': 'EFO:0010846'}, {'sampleOriginType.id': 'CL:0000767'}, {'sampleOriginType.id': 'MONDO:0019740'}, {'sampleOriginType.id': 'EFO:0011039'}, {'sampleOriginType.id': 'MONDO:0044972'}, {'sampleOriginType.id': 'EFO:0010795'}, {'sampleOriginType.id': 'MONDO:0017570'}, {'sampleOriginType.id': 'MONDO:0100433'}, {'sampleOriginType.id': 'EFO:0004587'}, {'sampleOriginType.id': 'CL:0000582'}, {'sampleOriginType.id': 'MONDO:0007686'}, {'sampleOriginType.id': 'EFO:0006614'}, {'sampleOriginType.id': 'MONDO:0018023'}, {'sampleOriginType.id': 'EFO:0009233'}, {'sampleOriginType.id': 'CL:0002357'}, {'sampleOriginType.id': 'EFO:0010876'}, {'sampleOriginType.id': 'EFO:0010870'}, {'sampleOriginType.id': 'MONDO:0014386'}, {'sampleOriginType.id': 'EFO:0010888'}, {'sampleOriginType.id': 'EFO:0010779'}, {'sampleOriginType.id': 'EFO:0010785'}, {'sampleOriginType.id': 'MONDO:0010121'}, {'sampleOriginType.id': 'EFO:0803542'}, {'sampleOriginType.id': 'MONDO:0013622'}, {'sampleOriginType.id': 'EFO:0009157'}, {'sampleOriginType.id': 'EFO:0006572'}, {'sampleOriginType.id': 'MONDO:0009506'}, {'sampleOriginType.id': 'EFO:0010850'}, {'sampleOriginType.id': 'CL:0000081'}, {'sampleOriginType.id': 'EFO:0010886'}, {'sampleOriginType.id': 'EFO:0004306'}, {'sampleOriginType.id': 'EFO:0007992'}, {'sampleOriginType.id': 'EFO:0007996'}, {'sampleOriginType.id': 'CL:0000772'}, {'sampleOriginType.id': 'MONDO:0010120'}, {'sampleOriginType.id': 'E2024-09-30T16:47:31.191407049Z FO:0001221'}, {'sampleOriginType.id': 'CL:0000768'}, {'sampleOriginType.id': 'EFO:0009222'}, {'sampleOriginType.id': 'MONDO:0016242'}, {'sampleOriginType.id': 'CL:0002022'}, {'sampleOriginType.id': 'CL:0002021'}, {'sampleOriginType.id': 'MONDO:0000602'}, {'sampleOriginType.id': 'Orphanet:847'}, {'sampleOriginType.id': 'EFO:0009248'}, {'sampleOriginType.id': 'EFO:0010866'}, {'sampleOriginType.id': 'MONDO:0013597'}, {'sampleOriginType.id': 'EFO:0022546'}, {'sampleOriginType.id': 'EFO:0002229'}, {'sampleOriginType.id': 'EFO:0010868'}, {'sampleOriginType.id': 'EFO:0009203'}, {'sampleOriginType.id': 'EFO:0004348'}, {'sampleOriginType.id': 'MONDO:0013275'}, {'sampleOriginType.id': 'CL:0000771'}, {'sampleOriginType.id': 'BTO:0000133'}, {'sampleOriginType.id': 'EFO:0022507'}, {'sampleOriginType.id': 'EFO:0010802'}, {'sampleOriginType.id': 'EFO:0010842'}, {'sampleOriginType.id': 'MONDO:0016030'}, {'sampleOriginType.id': 'EFO:0009206'}, {'sampleOriginType.id': 'EFO:0010865'}, {'sampleOriginType.id': 'MONDO:0011895'}, {'sampleOriginType.id': 'MONDO:0800451'}, {'sampleOriginType.id': 'EFO:0010879'}, {'sampleOriginType.id': 'Orphanet:848'}, {'sampleOriginType.id': 'EFO:0005635'}, {'sampleOriginType.id': 'EFO:0010760'}, {'sampleOriginType.id': 'EFO:0010794'}, {'sampleOriginType.id': 'EFO:0009204'}, {'sampleOriginType.id': 'EFO:0010871'}, {'sampleOriginType.id': 'EFO:1000014'}, {'sampleOriginType.id': 'MONDO:0031447'}, {'sampleOriginType.id': 'EFO:0010874'}, {'sampleOriginType.id': 'MONDO:0016243'}, {'sampleOriginType.id': 'MONDO:0010745'}, {'sampleOriginType.id': 'EFO:0009240'}, {'sampleOriginType.id': 'EFO:0009234'}, {'sampleOriginType.id': 'EFO:0010848'}, {'sampleOriginType.id': 'EFO:0007991'}, {'sampleOriginType.id': 'MONDO:0012202'}, {'sampleOriginType.id': 'MONDO:0019031'}, {'sampleOriginType.id': 'MONDO:0021024'}, {'sampleOriginType.id': 'EFO:0010769'}, {'sampleOriginType.id': 'EFO:0010773'}, {'sampleOriginType.id': 'EFO:0004694'}, {'sampleOriginType.id': 'MONDO:0100563'}, {'sampleOriginType.id': 'EFO:0010852'}, {'sampleOriginType.id': 'EFO:0010804'}, {'sampleOriginType.id': 'MONDO:0800447'}, {'sampleOriginType.id': 'EFO:0010784'}, {'sampleOriginType.id': 'EFO:0007984'}, {'sampleOriginType.id': 'MONDO:0009158'}, {'sampleOriginType.id': 'EFO:0007172'}, {'sampleOriginType.id': 'MONDO:0009953'}, {'sampleOriginType.id': 'EFO:0007444'}, {'sampleOriginType.id': 'EFO:0006486'}, {'sampleOriginType.id': 'EFO:0008390'}, {'sampleOriginType.id': 'EFO:0004985'}, {'sampleOriginType.id': 'MONDO:0014757'}, {'sampleOriginType.id': 'MONDO:0000440'}, {'sampleOriginType.id': 'EFO:0803544'}, {'sampleOriginType.id': 'EFO:0010864'}, {'sampleOriginType.id': 'EFO:0010838'}, {'sampleOriginType.id': 'Orphanet:231230'}, {'sampleOriginType.id': 'EFO:0006615'}, {'sampleOriginType.id': 'EFO:0002534'}, {'sampleOriginType.id': 'EFO:0000479'}, {'sampleOriginType.id': 'CL:0000769'}, {'sampleOriginType.id': 'EFO:0001254'}, {'sampleOriginType.id': 'EFO:0803543'}, {'sampleOriginType.id': 'MONDO:0015978'}, {'sampleOriginType.id': 'MONDO:0001198'}, {'sampleOriginType.id': 'CL:0000094'}, {'sampleOriginType.id': 'CL:0000562'}, {'sampleOriginType.id': 'EFO:0010889'}, {'sampleOriginType.id': 'EFO:0006653'}, {'sampleOriginType.id': 'MONDO:0016486'}, {'sampleOriginType.id': 'MONDO:0030996'}]}, 'biosample', 'g_variants', {})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_11_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_12_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_12_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'sampleOriginType.id': 'UBERON:0000178'}, {'sampleOriginType.id': 'MONDO:0013512'}, {'sampleOriginType.id': 'CL:0000232'}, {'sampleOriginType.id': 'EFO:0004842'}, {'sampleOriginType.id': 'EFO:0007988'}, {'sampleOriginType.id': 'EFO:0004808'}, {'sampleOriginType.id': 'MONDO:0009950'}, {'sampleOriginType.id': 'EFO:0009244'}, {'sampleOriginType.id': 'EFO:0009253'}, {'sampleOriginType.id': 'EFO:0010783'}, {'sampleOriginType.id': 'EFO:0003073'}, {'sampleOriginType.id': 'EFO:0009252'}, {'sampleOriginType.id': 'MONDO:0001117'}, {'sampleOriginType.id': 'MONDO:0018022'}, {'sampleOriginType.id': 'EFO:0010109'}, {'sampleOriginType.id': 'EFO:0010840'}, {'sampleOriginType.id': 'EFO:0010792'}, {'sampleOriginType.id': 'EFO:0005090'}, {'sampleOriginType.id': 'EFO:0010772'}, {'sampleOriginType.id': 'MONDO:0017829'}, {'sampleOriginType.id': 'EFO:0001941'}, {'sampleOriginType.id': 'EFO:0010790'}, {'sampleOriginType.id': 'EFO:0010861'}, {'sampleOriginType.id': 'MONDO:0018749'}, {'sampleOriginType.id': 'EFO:0010849'}, {'sampleOriginType.id': 'EFO:1001467'}, {'sampleOriginType.id': 'MONDO:0017238'}, {'sampleOriginType.id': 'EFO:0007129'}, {'sampleOriginType.id': 'MONDO:0011136'}, {'sampleOriginType.id': 'Orphanet:231242'}, {'sampleOriginType.id': 'EFO:0007481'}, {'sampleOriginType.id': 'EFO:0009215'}, {'sampleOriginType.id': 'MONDO:0017145'}, {'sampleOriginType.id': 'CL:0000775'}, {'sampleOriginType.id': 'MONDO:0008555'}, {'sampleOriginType.id': 'MONDO:0004680'}, {'sampleOriginType.id': 'EFO:0004305'}, {'sampleOriginType.id': 'MONDO:0016490'}, {'sampleOriginType.id': 'MONDO:0007838'}, {'sampleOriginType.id': 'MONDO:0013016'}, {'sampleOriginType.id': 'EFO:0007994'}, {'sampleOriginType.id': 'MONDO:0013623'}, {'sampleOriginType.id': 'CL:0000614'}, {'sampleOriginType.id': 'EFO:0010107'}, {'sampleOriginType.id': 'CL:0000976'}, {'sampleOriginType.id': 'EFO:0009225'}, {'sampleOriginType.id': 'CL:0002318'}, {'sampleOriginType.id': 'EFO:0004309'}, {'sampleOriginType.id': 'EFO:0004526'}, {'sampleOriginType.id': 'EFO:0010843'}, {'sampleOriginType.id': 'CL:0002155'}, {'sampleOriginType.id': 'EFO:0010796'}, {'sampleOriginType.id': 'EFO:0001378'}, {'sampleOriginType.id': 'EFO:0009209'}, {'sampleOriginType.id': 'EFO:0009224'}, {'sampleOriginType.id': 'EFO:0009210'}, {'sampleOriginType.id': 'MONDO:0016489'}, {'sampleOriginType.id': 'EFO:0010781'}, {'sampleOriginType.id': 'Orphanet:98791'}, {'sampleOriginType.id': 'EFO:0600063'}, {'sampleOriginType.id': 'CL:0000580'}, {'sampleOriginType.id': 'EFO:0009226'}, {'sampleOriginType.id': 'EFO:0008542'}, {'sampleOriginType.id': 'EFO:0009236'}, {'sampleOriginType.id': 'MONDO:0018269'}, {'sampleOriginType.id': 'MONDO:0016669'}, {'sampleOriginType.id': 'EFO:0004637'}, {'sampleOriginType.id': 'EFO:0010801'}, {'sampleOriginType.id': 'CL:0000978'}, {'sampleOriginType.id': 'Orphanet:846'}, {'sampleOriginType.id': 'EFO:0007445'}, {'sampleOriginType.id': 'EFO:0009239'}, {'sampleOriginType.id': 'CL:0000774'}, {'sampleOriginType.id': 'Orphanet:330032'}, {'sampleOriginType.id': 'MONDO:0019537'}, {'sampleOriginType.id': 'EFO:0010793'}, {'sampleOriginType.id': 'EFO:0009132'}, {'sampleOriginType.id': 'MONDO:0013517'}, {'sampleOriginType.id': 'EFO:0009218'}, {'sampleOriginType.id': 'MONDO:0018963'}, {'sampleOriginType.id': 'EFO:0010799'}, {'sampleOriginType.id': 'MONDO:0012354'}, {'sampleOriginType.id': 'EFO:0010860'}, {'sampleOriginType.id': 'EFO:0007989'}, {'sampleOriginType.id': 'EFO:0010835'}, {'sampleOriginType.id': 'MONDO:0011603'}, {'sampleOriginType.id': 'CL:0000975'}, {'sampleOriginType.id': 'Orphanet:168615'}, {'sampleOriginType.id': 'MONDO:0019535'}, {'sampleOriginType.id': 'CL:0000770'}, {'sampleOriginType.id': 'EFO:0010108'}, {'sampleOriginType.id': 'EFO:0010884'}, {'sampleOriginType.id': 'EFO:0010867'}, {'sampleOriginType.id': 'EFO:0009246'}, {'sampleOriginType.id': 'EFO:0009219'}, {'sampleOriginType.id': 'EFO:0010856'}, {'sampleOriginType.id': 'MONDO:0044349'}, {'sampleOriginType.id': 'EFO:0004584'}, {'sampleOriginType.id': 'MONDO:0018794'}, {'sampleOriginType.id': 'EFO:0007993'}, {'sampleOriginType.id': 'EFO:0009220'}, {'sampleOriginType.id': 'EFO:0010881'}, {'sampleOriginType.id': 'MONDO:0100326'}, {'sampleOriginType.id': 'EFO:0010768'}, {'sampleOriginType.id': 'EFO:0010862'}, {'sampleOriginType.id': 'MONDO:0000105'}, {'sampleOriginType.id': 'MONDO:0019050'}, {'sampleOriginType.id': 'MONDO:0010122'}, {'sampleOriginType.id': 'EFO:0009238'}, {'sampleOriginType.id': 'MONDO:0019098'}, {'sampleOriginType.id': 'EFO:1001316'}, {'sampleOriginType.id': 'EFO:0009646'}, {'sampleOriginType.id': 'MONDO:0016671'}, {'sampleOriginType.id': 'MONDO:0010308'}, {'sampleOriginType.id': 'MONDO:0008369'}, {'sampleOriginType.id': 'EFO:0004310'}, {'sampleOriginType.id': 'EFO:0010780'}, {'sampleOriginType.id': 'EFO:0006613'}, {'sampleOriginType.id': 'EFO:0008447'}, {'sampleOriginType.id': 'EFO:0008543'}, {'sampleOriginType.id': 'EFO:0010770'}, {'sampleOriginType.id': 'CL:0000977'}, {'sampleOriginType.id': 'EFO:0010887'}, {'sampleOriginType.id': 'EFO:0004629'}, {'sampleOriginType.id': 'MONDO:0018740'}, {'sampleOriginType.id': 'EFO:0010853'}, {'sampleOriginType.id': 'MONDO:0009490'}, {'sampleOriginType.id': 'EFO:0010791'}, {'sampleOriginType.id': 'EFO:0010847'}, {'sampleOriginType.id': 'EFO:0010775'}, {'sampleOriginType.id': 'EFO:0009245'}, {'sampleOriginType.id': 'EFO:0010763'}, {'sampleOriginType.id': 'EFO:0700023'}, {'sampleOriginType.id': 'EFO:0010970'}, {'sampleOriginType.id': 'EFO:0010764'}, {'sampleOriginType.id': 'EFO:0600062'}, {'sampleOriginType.id': 'CL:0000776'}, {'sampleOriginType.id': 'EFO:1001115'}, {'sampleOriginType.id': 'MONDO:0016672'}, {'sampleOriginType.id': 'EFO:0004634'}, {'sampleOriginType.id': 'EFO:0004528'}, {'sampleOriginType.id': 'EFO:0009390'}, {'sampleOriginType.id': 'MONDO:0015579'}, {'sampleOriginType.id': 'EFO:0700066'}, {'sampleOriginType.id': 'EFO:0007987'}, {'sampleOriginType.id': 'MONDO:0014078'}, {'sampleOriginType.id': 'EFO:0006530'}, {'sampleOriginType.id': 'MONDO:0019111'}, {'sampleOriginType.id': 'MONDO:0016360'}, {'sampleOriginType.id': 'EFO:0009250'}, {'sampleOriginType.id': 'MONDO:0015372'}, {'sampleOriginType.id': 'MONDO:0016491'}, {'sampleOriginType.id': 'EFO:0009221'}, {'sampleOriginType.id': 'CL:0000986'}, {'sampleOriginType.id': 'MONDO:0020117'}, {'sampleOriginType.id': 'EFO:0004619'}, {'sampleOriginType.id': 'Orphanet:231386'}, {'sampleOriginType.id': 'EFO:0002339'}, {'sampleOriginType.id': 'EFO:0010774'}, {'sampleOriginType.id': 'EFO:0007990'}, {'sampleOriginType.id': 'EFO:0022585'}, {'sampleOriginType.id': 'EFO:0010778'}, {'sampleOriginType.id': 'MONDO:0007293'}, {'sampleOriginType.id': 'EFO:0004633'}, {'sampleOriginType.id': 'EFO:1001996'}, {'sampleOriginType.id': 'EFO:0008446'}, {'sampleOriginType.id': 'EFO:0002322'}, {'sampleOriginType.id': 'UBERON:0001969'}, {'sampleOriginType.id': 'CL:0000985'}, {'sampleOriginType.id': 'EFO:0009181'}, {'sampleOriginType.id': 'CL:0000974'}, {'sampleOriginType.id': 'CL:0000951'}, {'sampleOriginType.id': 'EFO:0010105'}, {'sampleOriginType.id': 'EFO:0009249'}, {'sampleOriginType.id': 'EFO:0803346'}, {'sampleOriginType.id': 'EFO:0005845'}, {'sampleOriginType.id': 'EFO:0010880'}, {'sampleOriginType.id': 'MONDO:0044347'}, {'sampleOriginType.id': 'EFO:0007615'}, {'sampleOriginType.id': 'EFO:0010788'}, {'sampleOriginType.id': 'MONDO:0018922'}, {'sampleOriginType.id': 'MONDO:0016630'}, {'sampleOriginType.id': 'EFO:0007978'}, {'sampleOriginType.id': 'EFO:0010855'}, {'sampleOriginType.id': 'EFO:0006609'}, {'sampleOriginType.id': 'EFO:0006617'}, {'sampleOriginType.id': 'EFO:0010859'}, {'sampleOriginType.id': 'EFO:0009202'}, {'sampleOriginType.id': 'MONDO:0012775'}, {'sampleOriginType.id': 'EFO:0008582'}, {'sampleOriginType.id': 'EFO:0009230'}, {'sampleOriginType.id': 'EFO:0009498'}, {'sampleOriginType.id': 'EFO:0000777'}, {'sampleOriginType.id': 'EFO:0010800'}, {'sampleOriginType.id': 'EFO:0001253'}, {'sampleOriginType.id': 'EFO:0010782'}, {'sampleOriginType.id': 'EFO:0010890'}, {'sampleOriginType.id': 'EFO:0004536'}, {'sampleOriginType.id': 'MONDO:0009694'}, {'sampleOriginType.id': 'MONDO:0043768'}, {'sampleOriginType.id': 'EFO:0010837'}, {'sampleOriginType.id': 'EFO:0010857'}, {'sampleOriginType.id': 'EFO:0004630'}, {'sampleOriginType.id': 'EFO:0009229'}, {'sampleOriginType.id': 'EFO:0009214'}, {'sampleOriginType.id': 'CL:0000392'}, {'sampleOriginType.id': 'MONDO:0008332'}, {'sampleOriginType.id': 'EFO:0006616'}, {'sampleOriginType.id': 'EFO:0006619'}, {'sampleOriginType.id': 'MONDO:0800452'}, {'sampleOriginType.id': 'EFO:0009388'}, {'sampleOriginType.id': 'EFO:0009216'}, {'sampleOriginType.id': 'EFO:0009247'}, {'sampleOriginType.id': 'MONDO:0001909'}, {'sampleOriginType.id': 'MONDO:0001197'}, {'sampleOriginType.id': 'EFO:0009217'}, {'sampleOriginType.id': 'EFO:0007995'}, {'sampleOriginType.id': 'Orphanet:231249'}, {'sampleOriginType.id': 'EFO:0010789'}, {'sampleOriginType.id': 'Orphanet:231393'}, {'sampleOriginType.id': 'Orphanet:168612'}, {'sampleOriginType.id': 'EFO:0009389'}, {'sampleOriginType.id': 'MONDO:0011381'}, {'sampleOriginType.id': 'EFO:0022042'}, {'sampleOriginType.id': 'MONDO:0008497'}, {'sampleOriginType.id': 'CL:0000595'}, {'sampleOriginType.id': 'MONDO:0011382'}, {'sampleOriginType.id': 'MONDO:0012031'}, {'sampleOriginType.id': 'EFO:0010883'}, {'sampleOriginType.id': 'EFO:0010851'}, {'sampleOriginType.id': 'EFO:0004640'}, {'sampleOriginType.id': 'MONDO:0018896'}, {'sampleOriginType.id': 'EFO:0010845'}, {'sampleOriginType.id': 'EFO:0004623'}, {'sampleOriginType.id': 'MONDO:0009276'}, {'sampleOriginType.id': 'EFO:0022508'}, {'sampleOriginType.id': 'MONDO:0016668'}, {'sampleOriginType.id': 'GO:0070527'}, {'sampleOriginType.id': 'EFO:0010878'}, {'sampleOriginType.id': 'CL:0000987'}, {'sampleOriginType.id': 'Orphanet:231401'}, {'sampleOriginType.id': 'MONDO:0008553'}, {'sampleOriginType.id': 'EFO:0001219'}, {'sampleOriginType.id': 'EFO:0004541'}, {'sampleOriginType.id': 'EFO:0600027'}, {'sampleOriginType.id': 'EFO:0022579'}, {'sampleOriginType.id': 'EFO:0002207'}, {'sampleOriginType.id': 'CL:0000560'}, {'sampleOriginType.id': 'EFO:0004308'}, {'sampleOriginType.id': 'CL:0000773'}, {'sampleOriginType.id': 'EFO:0009223'}, {'sampleOriginType.id': 'EFO:0004586'}, {'sampleOriginType.id': 'MONDO:0011399'}, {'sampleOriginType.id': 'EFO:0010873'}, {'sampleOriginType.id': 'EFO:0009251'}, {'sampleOriginType.id': 'EFO:0007160'}, {'sampleOriginType.id': 'CL:0000041'}, {'sampleOriginType.id': 'EFO:1001200'}, {'sampleOriginType.id': 'MONDO:0018268'}, {'sampleOriginType.id': 'MONDO:0044635'}, {'sampleOriginType.id': 'EFO:0010844'}, {'sampleOriginType.id': 'EFO:0006552'}, {'sampleOriginType.id': 'EFO:0006654'}, {'sampleOriginType.id': 'EFO:0010882'}, {'sampleOriginType.id': 'EFO:0001068'}, {'sampleOriginType.id': 'MONDO:0000009'}, {'sampleOriginType.id': 'EFO:0006618'}, {'sampleOriginType.id': 'EFO:0010872'}, {'sampleOriginType.id': 'CL:0000043'}, {'sampleOriginType.id': 'MONDO:0011422'}, {'sampleOriginType.id': 'MONDO:0011268'}, {'sampleOriginType.id': 'EFO:0010854'}, {'sampleOriginType.id': 'CL:0000387'}, {'sampleOriginType.id': 'EFO:0006611'}, {'sampleOriginType.id': 'EFO:0010836'}, {'sampleOriginType.id': 'MONDO:0030867'}, {'sampleOriginType.id': 'EFO:0010762'}, {'sampleOriginType.id': 'EFO:0006612'}, {'sampleOriginType.id': 'EFO:0007629'}, {'sampleOriginType.id': 'UBERON:0012168'}, {'sampleOriginType.id': 'EFO:0004576'}, {'sampleOriginType.id': 'CL:0000786'}, {'sampleOriginType.id': 'EFO:0009232'}, {'sampleOriginType.id': 'EFO:1001112'}, {'sampleOriginType.id': 'EFO:0010839'}, {'sampleOriginType.id': 'MONDO:0014536'}, {'sampleOriginType.id': 'EFO:0004833'}, {'sampleOriginType.id': 'EFO:0010106'}, {'sampleOriginType.id': 'EFO:0006716'}, {'sampleOriginType.id': 'EFO:0010875'}, {'sampleOriginType.id': 'EFO:0009231'}, {'sampleOriginType.id': 'MONDO:0011988'}, {'sampleOriginType.id': 'MONDO:0011555'}, {'sampleOriginType.id': 'EFO:0010786'}, {'sampleOriginType.id': 'MONDO:0016487'}, {'sampleOriginType.id': 'EFO:0006857'}, {'sampleOriginType.id': 'MONDO:0016670'}, {'sampleOriginType.id': 'EFO:0009205'}, {'sampleOriginType.id': 'CL:0000947'}, {'sampleOriginType.id': 'EFO:0004304'}, {'sampleOriginType.id': 'MONDO:0002249'}, {'sampleOriginType.id': 'EFO:0008087'}, {'sampleOriginType.id': 'EFO:0009208'}, {'sampleOriginType.id': 'MONDO:0018795'}, {'sampleOriginType.id': 'EFO:0022513'}, {'sampleOriginType.id': 'EFO:0010841'}, {'sampleOriginType.id': 'EFO:0600058'}, {'sampleOriginType.id': 'MONDO:0016450'}, {'sampleOriginType.id': 'EFO:0010869'}, {'sampleOriginType.id': 'EFO:0005091'}, {'sampleOriginType.id': 'EFO:0006553'}, {'sampleOriginType.id': 'EFO:0600059'}, {'sampleOriginType.id': 'EFO:1000641'}, {'sampleOriginType.id': 'MONDO:0010743'}, {'sampleOriginType.id': 'EFO:0007997'}, {'sampleOriginType.id': 'EFO:0010803'}, {'sampleOriginType.id': 'EFO:0009235'}, {'sampleOriginType.id': 'MONDO:0009885'}, {'sampleOriginType.id': 'EFO:0010798'}, {'sampleOriginType.id': 'EFO:0009228'}, {'sampleOriginType.id': 'HP:0003530'}, {'sampleOriginType.id': 'MONDO:0002245'}, {'sampleOriginType.id': 'EFO:0010877'}, {'sampleOriginType.id': 'EFO:0010797'}, {'sampleOriginType.id': 'EFO:0009497'}, {'sampleOriginType.id': 'MONDO:0010480'}, {'sampleOriginType.id': 'EFO:0009133'}, {'sampleOriginType.id': 'EFO:0010766'}, {'sampleOriginType.id': 'EFO:0600060'}, {'sampleOriginType.id': 'CL:0000390'}, {'sampleOriginType.id': 'EFO:0010885'}, {'sampleOriginType.id': 'EFO:1001264'}, {'sampleOriginType.id': 'EFO:0007985'}, {'sampleOriginType.id': 'EFO:0004509'}, {'sampleOriginType.id': 'CL:0000096'}, {'sampleOriginType.id': 'EFO:0600061'}, {'sampleOriginType.id': 'EFO:0020902'}, {'sampleOriginType.id': 'EFO:0009237'}, {'sampleOriginType.id': 'EFO:0009227'}, {'sampleOriginType.id': 'EFO:0010777'}, {'sampleOriginType.id': 'EFO:0009188'}, {'sampleOriginType.id': 'EFO:0009241'}, {'sampleOriginType.id': 'CL:0000612'}, {'sampleOriginType.id': 'EFO:0009134'}, {'sampleOriginType.id': 'MONDO:0008557'}, {'sampleOriginType.id': 'MONDO:0014518'}, {'sampleOriginType.id': 'EFO:0009242'}, {'sampleOriginType.id': 'CL:0000233'}, {'sampleOriginType.id': 'MONDO:0030827'}, {'sampleOriginType.id': 'EFO:0004301'}, {'sampleOriginType.id': 'Orphanet:46532'}, {'sampleOriginType.id': 'MONDO:0031332'}, {'sampleOriginType.id': 'MONDO:0019402'}, {'sampleOriginType.id': 'EFO:0009211'}, {'sampleOriginType.id': 'MONDO:0011173'}, {'sampleOriginType.id': 'EFO:0009212'}, {'sampleOriginType.id': 'HP:0003146'}, {'sampleOriginType.id': 'MONDO:0044348'}, {'sampleOriginType.id': 'MONDO:0100241'}, {'sampleOriginType.id': 'EFO:0005576'}, {'sampleOriginType.id': 'EFO:0010863'}, {'sampleOriginType.id': 'EFO:0004527'}, {'sampleOriginType.id': 'EFO:0009213'}, {'sampleOriginType.id': 'EFO:0010858'}, {'sampleOriginType.id': 'EFO:0010776'}, {'sampleOriginType.id': 'EFO:0009243'}, {'sampleOriginType.id': 'EFO:0010761'}, {'sampleOriginType.id': 'EFO:0010846'}, {'sampleOriginType.id': 'CL:0000767'}, {'sampleOriginType.id': 'MONDO:0019740'}, {'sampleOriginType.id': 'EFO:0011039'}, {'sampleOriginType.id': 'MONDO:0044972'}, {'sampleOriginType.id': 'EFO:0010795'}, {'sampleOriginType.id': 'MONDO:0017570'}, {'sampleOriginType.id': 'MONDO:0100433'}, {'sampleOriginType.id': 'EFO:0004587'}, {'sampleOriginType.id': 'CL:0000582'}, {'sampleOriginType.id': 'MONDO:0007686'}, {'sampleOriginType.id': 'EFO:0006614'}, {'sampleOriginType.id': 'MONDO:0018023'}, {'sampleOriginType.id': 'EFO:0009233'}, {'sampleOriginType.id': 'CL:0002357'}, {'sampleOriginType.id': 'EFO:0010876'}, {'sampleOriginType.id': 'EFO:0010870'}, {'sampleOriginType.id': 'MONDO:0014386'}, {'sampleOriginType.id': 'EFO:0010888'}, {'sampleOriginType.id': 'EFO:0010779'}, {'sampleOriginType.id': 'EFO:0010785'}, {'sampleOriginType.id': 'MONDO:0010121'}, {'sampleOriginType.id': 'EFO:0803542'}, {'sampleOriginType.id': 'MONDO:0013622'}, {'sampleOriginType.id': 'EFO:0009157'}, {'sampleOriginType.id': 'EFO:0006572'}, {'sampleOriginType.id': 'MONDO:0009506'}, {'sampleOriginType.id': 'EFO:0010850'}, {'sampleOriginType.id': 'CL:0000081'}, {'sampleOriginType.id': 'EFO:0010886'}, {'sampleOriginType.id': 'EFO:0004306'}, {'sampleOriginType.id': 'EFO:0007992'}, {'sampleOriginType.id': 'EFO:0007996'}, {'sampleOriginType.id': 'CL:0000772'}, {'sampleOriginType.id': 'MONDO:0010120'}, {'sampleOriginType.id': 'E2024-09-30T16:47:31.191407049Z FO:0001221'}, {'sampleOriginType.id': 'CL:0000768'}, {'sampleOriginType.id': 'EFO:0009222'}, {'sampleOriginType.id': 'MONDO:0016242'}, {'sampleOriginType.id': 'CL:0002022'}, {'sampleOriginType.id': 'CL:0002021'}, {'sampleOriginType.id': 'MONDO:0000602'}, {'sampleOriginType.id': 'Orphanet:847'}, {'sampleOriginType.id': 'EFO:0009248'}, {'sampleOriginType.id': 'EFO:0010866'}, {'sampleOriginType.id': 'MONDO:0013597'}, {'sampleOriginType.id': 'EFO:0022546'}, {'sampleOriginType.id': 'EFO:0002229'}, {'sampleOriginType.id': 'EFO:0010868'}, {'sampleOriginType.id': 'EFO:0009203'}, {'sampleOriginType.id': 'EFO:0004348'}, {'sampleOriginType.id': 'MONDO:0013275'}, {'sampleOriginType.id': 'CL:0000771'}, {'sampleOriginType.id': 'BTO:0000133'}, {'sampleOriginType.id': 'EFO:0022507'}, {'sampleOriginType.id': 'EFO:0010802'}, {'sampleOriginType.id': 'EFO:0010842'}, {'sampleOriginType.id': 'MONDO:0016030'}, {'sampleOriginType.id': 'EFO:0009206'}, {'sampleOriginType.id': 'EFO:0010865'}, {'sampleOriginType.id': 'MONDO:0011895'}, {'sampleOriginType.id': 'MONDO:0800451'}, {'sampleOriginType.id': 'EFO:0010879'}, {'sampleOriginType.id': 'Orphanet:848'}, {'sampleOriginType.id': 'EFO:0005635'}, {'sampleOriginType.id': 'EFO:0010760'}, {'sampleOriginType.id': 'EFO:0010794'}, {'sampleOriginType.id': 'EFO:0009204'}, {'sampleOriginType.id': 'EFO:0010871'}, {'sampleOriginType.id': 'EFO:1000014'}, {'sampleOriginType.id': 'MONDO:0031447'}, {'sampleOriginType.id': 'EFO:0010874'}, {'sampleOriginType.id': 'MONDO:0016243'}, {'sampleOriginType.id': 'MONDO:0010745'}, {'sampleOriginType.id': 'EFO:0009240'}, {'sampleOriginType.id': 'EFO:0009234'}, {'sampleOriginType.id': 'EFO:0010848'}, {'sampleOriginType.id': 'EFO:0007991'}, {'sampleOriginType.id': 'MONDO:0012202'}, {'sampleOriginType.id': 'MONDO:0019031'}, {'sampleOriginType.id': 'MONDO:0021024'}, {'sampleOriginType.id': 'EFO:0010769'}, {'sampleOriginType.id': 'EFO:0010773'}, {'sampleOriginType.id': 'EFO:0004694'}, {'sampleOriginType.id': 'MONDO:0100563'}, {'sampleOriginType.id': 'EFO:0010852'}, {'sampleOriginType.id': 'EFO:0010804'}, {'sampleOriginType.id': 'MONDO:0800447'}, {'sampleOriginType.id': 'EFO:0010784'}, {'sampleOriginType.id': 'EFO:0007984'}, {'sampleOriginType.id': 'MONDO:0009158'}, {'sampleOriginType.id': 'EFO:0007172'}, {'sampleOriginType.id': 'MONDO:0009953'}, {'sampleOriginType.id': 'EFO:0007444'}, {'sampleOriginType.id': 'EFO:0006486'}, {'sampleOriginType.id': 'EFO:0008390'}, {'sampleOriginType.id': 'EFO:0004985'}, {'sampleOriginType.id': 'MONDO:0014757'}, {'sampleOriginType.id': 'MONDO:0000440'}, {'sampleOriginType.id': 'EFO:0803544'}, {'sampleOriginType.id': 'EFO:0010864'}, {'sampleOriginType.id': 'EFO:0010838'}, {'sampleOriginType.id': 'Orphanet:231230'}, {'sampleOriginType.id': 'EFO:0006615'}, {'sampleOriginType.id': 'EFO:0002534'}, {'sampleOriginType.id': 'EFO:0000479'}, {'sampleOriginType.id': 'CL:0000769'}, {'sampleOriginType.id': 'EFO:0001254'}, {'sampleOriginType.id': 'EFO:0803543'}, {'sampleOriginType.id': 'MONDO:0015978'}, {'sampleOriginType.id': 'MONDO:0001198'}, {'sampleOriginType.id': 'CL:0000094'}, {'sampleOriginType.id': 'CL:0000562'}, {'sampleOriginType.id': 'EFO:0010889'}, {'sampleOriginType.id': 'EFO:0006653'}, {'sampleOriginType.id': 'MONDO:0016486'}, {'sampleOriginType.id': 'MONDO:0030996'}]}, 'biosample', 'individuals', {})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_12_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_13_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_13_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'sampleOriginType.id': 'UBERON:0000178'}, {'sampleOriginType.id': 'MONDO:0013512'}, {'sampleOriginType.id': 'CL:0000232'}, {'sampleOriginType.id': 'EFO:0004842'}, {'sampleOriginType.id': 'EFO:0007988'}, {'sampleOriginType.id': 'EFO:0004808'}, {'sampleOriginType.id': 'MONDO:0009950'}, {'sampleOriginType.id': 'EFO:0009244'}, {'sampleOriginType.id': 'EFO:0009253'}, {'sampleOriginType.id': 'EFO:0010783'}, {'sampleOriginType.id': 'EFO:0003073'}, {'sampleOriginType.id': 'EFO:0009252'}, {'sampleOriginType.id': 'MONDO:0001117'}, {'sampleOriginType.id': 'MONDO:0018022'}, {'sampleOriginType.id': 'EFO:0010109'}, {'sampleOriginType.id': 'EFO:0010840'}, {'sampleOriginType.id': 'EFO:0010792'}, {'sampleOriginType.id': 'EFO:0005090'}, {'sampleOriginType.id': 'EFO:0010772'}, {'sampleOriginType.id': 'MONDO:0017829'}, {'sampleOriginType.id': 'EFO:0001941'}, {'sampleOriginType.id': 'EFO:0010790'}, {'sampleOriginType.id': 'EFO:0010861'}, {'sampleOriginType.id': 'MONDO:0018749'}, {'sampleOriginType.id': 'EFO:0010849'}, {'sampleOriginType.id': 'EFO:1001467'}, {'sampleOriginType.id': 'MONDO:0017238'}, {'sampleOriginType.id': 'EFO:0007129'}, {'sampleOriginType.id': 'MONDO:0011136'}, {'sampleOriginType.id': 'Orphanet:231242'}, {'sampleOriginType.id': 'EFO:0007481'}, {'sampleOriginType.id': 'EFO:0009215'}, {'sampleOriginType.id': 'MONDO:0017145'}, {'sampleOriginType.id': 'CL:0000775'}, {'sampleOriginType.id': 'MONDO:0008555'}, {'sampleOriginType.id': 'MONDO:0004680'}, {'sampleOriginType.id': 'EFO:0004305'}, {'sampleOriginType.id': 'MONDO:0016490'}, {'sampleOriginType.id': 'MONDO:0007838'}, {'sampleOriginType.id': 'MONDO:0013016'}, {'sampleOriginType.id': 'EFO:0007994'}, {'sampleOriginType.id': 'MONDO:0013623'}, {'sampleOriginType.id': 'CL:0000614'}, {'sampleOriginType.id': 'EFO:0010107'}, {'sampleOriginType.id': 'CL:0000976'}, {'sampleOriginType.id': 'EFO:0009225'}, {'sampleOriginType.id': 'CL:0002318'}, {'sampleOriginType.id': 'EFO:0004309'}, {'sampleOriginType.id': 'EFO:0004526'}, {'sampleOriginType.id': 'EFO:0010843'}, {'sampleOriginType.id': 'CL:0002155'}, {'sampleOriginType.id': 'EFO:0010796'}, {'sampleOriginType.id': 'EFO:0001378'}, {'sampleOriginType.id': 'EFO:0009209'}, {'sampleOriginType.id': 'EFO:0009224'}, {'sampleOriginType.id': 'EFO:0009210'}, {'sampleOriginType.id': 'MONDO:0016489'}, {'sampleOriginType.id': 'EFO:0010781'}, {'sampleOriginType.id': 'Orphanet:98791'}, {'sampleOriginType.id': 'EFO:0600063'}, {'sampleOriginType.id': 'CL:0000580'}, {'sampleOriginType.id': 'EFO:0009226'}, {'sampleOriginType.id': 'EFO:0008542'}, {'sampleOriginType.id': 'EFO:0009236'}, {'sampleOriginType.id': 'MONDO:0018269'}, {'sampleOriginType.id': 'MONDO:0016669'}, {'sampleOriginType.id': 'EFO:0004637'}, {'sampleOriginType.id': 'EFO:0010801'}, {'sampleOriginType.id': 'CL:0000978'}, {'sampleOriginType.id': 'Orphanet:846'}, {'sampleOriginType.id': 'EFO:0007445'}, {'sampleOriginType.id': 'EFO:0009239'}, {'sampleOriginType.id': 'CL:0000774'}, {'sampleOriginType.id': 'Orphanet:330032'}, {'sampleOriginType.id': 'MONDO:0019537'}, {'sampleOriginType.id': 'EFO:0010793'}, {'sampleOriginType.id': 'EFO:0009132'}, {'sampleOriginType.id': 'MONDO:0013517'}, {'sampleOriginType.id': 'EFO:0009218'}, {'sampleOriginType.id': 'MONDO:0018963'}, {'sampleOriginType.id': 'EFO:0010799'}, {'sampleOriginType.id': 'MONDO:0012354'}, {'sampleOriginType.id': 'EFO:0010860'}, {'sampleOriginType.id': 'EFO:0007989'}, {'sampleOriginType.id': 'EFO:0010835'}, {'sampleOriginType.id': 'MONDO:0011603'}, {'sampleOriginType.id': 'CL:0000975'}, {'sampleOriginType.id': 'Orphanet:168615'}, {'sampleOriginType.id': 'MONDO:0019535'}, {'sampleOriginType.id': 'CL:0000770'}, {'sampleOriginType.id': 'EFO:0010108'}, {'sampleOriginType.id': 'EFO:0010884'}, {'sampleOriginType.id': 'EFO:0010867'}, {'sampleOriginType.id': 'EFO:0009246'}, {'sampleOriginType.id': 'EFO:0009219'}, {'sampleOriginType.id': 'EFO:0010856'}, {'sampleOriginType.id': 'MONDO:0044349'}, {'sampleOriginType.id': 'EFO:0004584'}, {'sampleOriginType.id': 'MONDO:0018794'}, {'sampleOriginType.id': 'EFO:0007993'}, {'sampleOriginType.id': 'EFO:0009220'}, {'sampleOriginType.id': 'EFO:0010881'}, {'sampleOriginType.id': 'MONDO:0100326'}, {'sampleOriginType.id': 'EFO:0010768'}, {'sampleOriginType.id': 'EFO:0010862'}, {'sampleOriginType.id': 'MONDO:0000105'}, {'sampleOriginType.id': 'MONDO:0019050'}, {'sampleOriginType.id': 'MONDO:0010122'}, {'sampleOriginType.id': 'EFO:0009238'}, {'sampleOriginType.id': 'MONDO:0019098'}, {'sampleOriginType.id': 'EFO:1001316'}, {'sampleOriginType.id': 'EFO:0009646'}, {'sampleOriginType.id': 'MONDO:0016671'}, {'sampleOriginType.id': 'MONDO:0010308'}, {'sampleOriginType.id': 'MONDO:0008369'}, {'sampleOriginType.id': 'EFO:0004310'}, {'sampleOriginType.id': 'EFO:0010780'}, {'sampleOriginType.id': 'EFO:0006613'}, {'sampleOriginType.id': 'EFO:0008447'}, {'sampleOriginType.id': 'EFO:0008543'}, {'sampleOriginType.id': 'EFO:0010770'}, {'sampleOriginType.id': 'CL:0000977'}, {'sampleOriginType.id': 'EFO:0010887'}, {'sampleOriginType.id': 'EFO:0004629'}, {'sampleOriginType.id': 'MONDO:0018740'}, {'sampleOriginType.id': 'EFO:0010853'}, {'sampleOriginType.id': 'MONDO:0009490'}, {'sampleOriginType.id': 'EFO:0010791'}, {'sampleOriginType.id': 'EFO:0010847'}, {'sampleOriginType.id': 'EFO:0010775'}, {'sampleOriginType.id': 'EFO:0009245'}, {'sampleOriginType.id': 'EFO:0010763'}, {'sampleOriginType.id': 'EFO:0700023'}, {'sampleOriginType.id': 'EFO:0010970'}, {'sampleOriginType.id': 'EFO:0010764'}, {'sampleOriginType.id': 'EFO:0600062'}, {'sampleOriginType.id': 'CL:0000776'}, {'sampleOriginType.id': 'EFO:1001115'}, {'sampleOriginType.id': 'MONDO:0016672'}, {'sampleOriginType.id': 'EFO:0004634'}, {'sampleOriginType.id': 'EFO:0004528'}, {'sampleOriginType.id': 'EFO:0009390'}, {'sampleOriginType.id': 'MONDO:0015579'}, {'sampleOriginType.id': 'EFO:0700066'}, {'sampleOriginType.id': 'EFO:0007987'}, {'sampleOriginType.id': 'MONDO:0014078'}, {'sampleOriginType.id': 'EFO:0006530'}, {'sampleOriginType.id': 'MONDO:0019111'}, {'sampleOriginType.id': 'MONDO:0016360'}, {'sampleOriginType.id': 'EFO:0009250'}, {'sampleOriginType.id': 'MONDO:0015372'}, {'sampleOriginType.id': 'MONDO:0016491'}, {'sampleOriginType.id': 'EFO:0009221'}, {'sampleOriginType.id': 'CL:0000986'}, {'sampleOriginType.id': 'MONDO:0020117'}, {'sampleOriginType.id': 'EFO:0004619'}, {'sampleOriginType.id': 'Orphanet:231386'}, {'sampleOriginType.id': 'EFO:0002339'}, {'sampleOriginType.id': 'EFO:0010774'}, {'sampleOriginType.id': 'EFO:0007990'}, {'sampleOriginType.id': 'EFO:0022585'}, {'sampleOriginType.id': 'EFO:0010778'}, {'sampleOriginType.id': 'MONDO:0007293'}, {'sampleOriginType.id': 'EFO:0004633'}, {'sampleOriginType.id': 'EFO:1001996'}, {'sampleOriginType.id': 'EFO:0008446'}, {'sampleOriginType.id': 'EFO:0002322'}, {'sampleOriginType.id': 'UBERON:0001969'}, {'sampleOriginType.id': 'CL:0000985'}, {'sampleOriginType.id': 'EFO:0009181'}, {'sampleOriginType.id': 'CL:0000974'}, {'sampleOriginType.id': 'CL:0000951'}, {'sampleOriginType.id': 'EFO:0010105'}, {'sampleOriginType.id': 'EFO:0009249'}, {'sampleOriginType.id': 'EFO:0803346'}, {'sampleOriginType.id': 'EFO:0005845'}, {'sampleOriginType.id': 'EFO:0010880'}, {'sampleOriginType.id': 'MONDO:0044347'}, {'sampleOriginType.id': 'EFO:0007615'}, {'sampleOriginType.id': 'EFO:0010788'}, {'sampleOriginType.id': 'MONDO:0018922'}, {'sampleOriginType.id': 'MONDO:0016630'}, {'sampleOriginType.id': 'EFO:0007978'}, {'sampleOriginType.id': 'EFO:0010855'}, {'sampleOriginType.id': 'EFO:0006609'}, {'sampleOriginType.id': 'EFO:0006617'}, {'sampleOriginType.id': 'EFO:0010859'}, {'sampleOriginType.id': 'EFO:0009202'}, {'sampleOriginType.id': 'MONDO:0012775'}, {'sampleOriginType.id': 'EFO:0008582'}, {'sampleOriginType.id': 'EFO:0009230'}, {'sampleOriginType.id': 'EFO:0009498'}, {'sampleOriginType.id': 'EFO:0000777'}, {'sampleOriginType.id': 'EFO:0010800'}, {'sampleOriginType.id': 'EFO:0001253'}, {'sampleOriginType.id': 'EFO:0010782'}, {'sampleOriginType.id': 'EFO:0010890'}, {'sampleOriginType.id': 'EFO:0004536'}, {'sampleOriginType.id': 'MONDO:0009694'}, {'sampleOriginType.id': 'MONDO:0043768'}, {'sampleOriginType.id': 'EFO:0010837'}, {'sampleOriginType.id': 'EFO:0010857'}, {'sampleOriginType.id': 'EFO:0004630'}, {'sampleOriginType.id': 'EFO:0009229'}, {'sampleOriginType.id': 'EFO:0009214'}, {'sampleOriginType.id': 'CL:0000392'}, {'sampleOriginType.id': 'MONDO:0008332'}, {'sampleOriginType.id': 'EFO:0006616'}, {'sampleOriginType.id': 'EFO:0006619'}, {'sampleOriginType.id': 'MONDO:0800452'}, {'sampleOriginType.id': 'EFO:0009388'}, {'sampleOriginType.id': 'EFO:0009216'}, {'sampleOriginType.id': 'EFO:0009247'}, {'sampleOriginType.id': 'MONDO:0001909'}, {'sampleOriginType.id': 'MONDO:0001197'}, {'sampleOriginType.id': 'EFO:0009217'}, {'sampleOriginType.id': 'EFO:0007995'}, {'sampleOriginType.id': 'Orphanet:231249'}, {'sampleOriginType.id': 'EFO:0010789'}, {'sampleOriginType.id': 'Orphanet:231393'}, {'sampleOriginType.id': 'Orphanet:168612'}, {'sampleOriginType.id': 'EFO:0009389'}, {'sampleOriginType.id': 'MONDO:0011381'}, {'sampleOriginType.id': 'EFO:0022042'}, {'sampleOriginType.id': 'MONDO:0008497'}, {'sampleOriginType.id': 'CL:0000595'}, {'sampleOriginType.id': 'MONDO:0011382'}, {'sampleOriginType.id': 'MONDO:0012031'}, {'sampleOriginType.id': 'EFO:0010883'}, {'sampleOriginType.id': 'EFO:0010851'}, {'sampleOriginType.id': 'EFO:0004640'}, {'sampleOriginType.id': 'MONDO:0018896'}, {'sampleOriginType.id': 'EFO:0010845'}, {'sampleOriginType.id': 'EFO:0004623'}, {'sampleOriginType.id': 'MONDO:0009276'}, {'sampleOriginType.id': 'EFO:0022508'}, {'sampleOriginType.id': 'MONDO:0016668'}, {'sampleOriginType.id': 'GO:0070527'}, {'sampleOriginType.id': 'EFO:0010878'}, {'sampleOriginType.id': 'CL:0000987'}, {'sampleOriginType.id': 'Orphanet:231401'}, {'sampleOriginType.id': 'MONDO:0008553'}, {'sampleOriginType.id': 'EFO:0001219'}, {'sampleOriginType.id': 'EFO:0004541'}, {'sampleOriginType.id': 'EFO:0600027'}, {'sampleOriginType.id': 'EFO:0022579'}, {'sampleOriginType.id': 'EFO:0002207'}, {'sampleOriginType.id': 'CL:0000560'}, {'sampleOriginType.id': 'EFO:0004308'}, {'sampleOriginType.id': 'CL:0000773'}, {'sampleOriginType.id': 'EFO:0009223'}, {'sampleOriginType.id': 'EFO:0004586'}, {'sampleOriginType.id': 'MONDO:0011399'}, {'sampleOriginType.id': 'EFO:0010873'}, {'sampleOriginType.id': 'EFO:0009251'}, {'sampleOriginType.id': 'EFO:0007160'}, {'sampleOriginType.id': 'CL:0000041'}, {'sampleOriginType.id': 'EFO:1001200'}, {'sampleOriginType.id': 'MONDO:0018268'}, {'sampleOriginType.id': 'MONDO:0044635'}, {'sampleOriginType.id': 'EFO:0010844'}, {'sampleOriginType.id': 'EFO:0006552'}, {'sampleOriginType.id': 'EFO:0006654'}, {'sampleOriginType.id': 'EFO:0010882'}, {'sampleOriginType.id': 'EFO:0001068'}, {'sampleOriginType.id': 'MONDO:0000009'}, {'sampleOriginType.id': 'EFO:0006618'}, {'sampleOriginType.id': 'EFO:0010872'}, {'sampleOriginType.id': 'CL:0000043'}, {'sampleOriginType.id': 'MONDO:0011422'}, {'sampleOriginType.id': 'MONDO:0011268'}, {'sampleOriginType.id': 'EFO:0010854'}, {'sampleOriginType.id': 'CL:0000387'}, {'sampleOriginType.id': 'EFO:0006611'}, {'sampleOriginType.id': 'EFO:0010836'}, {'sampleOriginType.id': 'MONDO:0030867'}, {'sampleOriginType.id': 'EFO:0010762'}, {'sampleOriginType.id': 'EFO:0006612'}, {'sampleOriginType.id': 'EFO:0007629'}, {'sampleOriginType.id': 'UBERON:0012168'}, {'sampleOriginType.id': 'EFO:0004576'}, {'sampleOriginType.id': 'CL:0000786'}, {'sampleOriginType.id': 'EFO:0009232'}, {'sampleOriginType.id': 'EFO:1001112'}, {'sampleOriginType.id': 'EFO:0010839'}, {'sampleOriginType.id': 'MONDO:0014536'}, {'sampleOriginType.id': 'EFO:0004833'}, {'sampleOriginType.id': 'EFO:0010106'}, {'sampleOriginType.id': 'EFO:0006716'}, {'sampleOriginType.id': 'EFO:0010875'}, {'sampleOriginType.id': 'EFO:0009231'}, {'sampleOriginType.id': 'MONDO:0011988'}, {'sampleOriginType.id': 'MONDO:0011555'}, {'sampleOriginType.id': 'EFO:0010786'}, {'sampleOriginType.id': 'MONDO:0016487'}, {'sampleOriginType.id': 'EFO:0006857'}, {'sampleOriginType.id': 'MONDO:0016670'}, {'sampleOriginType.id': 'EFO:0009205'}, {'sampleOriginType.id': 'CL:0000947'}, {'sampleOriginType.id': 'EFO:0004304'}, {'sampleOriginType.id': 'MONDO:0002249'}, {'sampleOriginType.id': 'EFO:0008087'}, {'sampleOriginType.id': 'EFO:0009208'}, {'sampleOriginType.id': 'MONDO:0018795'}, {'sampleOriginType.id': 'EFO:0022513'}, {'sampleOriginType.id': 'EFO:0010841'}, {'sampleOriginType.id': 'EFO:0600058'}, {'sampleOriginType.id': 'MONDO:0016450'}, {'sampleOriginType.id': 'EFO:0010869'}, {'sampleOriginType.id': 'EFO:0005091'}, {'sampleOriginType.id': 'EFO:0006553'}, {'sampleOriginType.id': 'EFO:0600059'}, {'sampleOriginType.id': 'EFO:1000641'}, {'sampleOriginType.id': 'MONDO:0010743'}, {'sampleOriginType.id': 'EFO:0007997'}, {'sampleOriginType.id': 'EFO:0010803'}, {'sampleOriginType.id': 'EFO:0009235'}, {'sampleOriginType.id': 'MONDO:0009885'}, {'sampleOriginType.id': 'EFO:0010798'}, {'sampleOriginType.id': 'EFO:0009228'}, {'sampleOriginType.id': 'HP:0003530'}, {'sampleOriginType.id': 'MONDO:0002245'}, {'sampleOriginType.id': 'EFO:0010877'}, {'sampleOriginType.id': 'EFO:0010797'}, {'sampleOriginType.id': 'EFO:0009497'}, {'sampleOriginType.id': 'MONDO:0010480'}, {'sampleOriginType.id': 'EFO:0009133'}, {'sampleOriginType.id': 'EFO:0010766'}, {'sampleOriginType.id': 'EFO:0600060'}, {'sampleOriginType.id': 'CL:0000390'}, {'sampleOriginType.id': 'EFO:0010885'}, {'sampleOriginType.id': 'EFO:1001264'}, {'sampleOriginType.id': 'EFO:0007985'}, {'sampleOriginType.id': 'EFO:0004509'}, {'sampleOriginType.id': 'CL:0000096'}, {'sampleOriginType.id': 'EFO:0600061'}, {'sampleOriginType.id': 'EFO:0020902'}, {'sampleOriginType.id': 'EFO:0009237'}, {'sampleOriginType.id': 'EFO:0009227'}, {'sampleOriginType.id': 'EFO:0010777'}, {'sampleOriginType.id': 'EFO:0009188'}, {'sampleOriginType.id': 'EFO:0009241'}, {'sampleOriginType.id': 'CL:0000612'}, {'sampleOriginType.id': 'EFO:0009134'}, {'sampleOriginType.id': 'MONDO:0008557'}, {'sampleOriginType.id': 'MONDO:0014518'}, {'sampleOriginType.id': 'EFO:0009242'}, {'sampleOriginType.id': 'CL:0000233'}, {'sampleOriginType.id': 'MONDO:0030827'}, {'sampleOriginType.id': 'EFO:0004301'}, {'sampleOriginType.id': 'Orphanet:46532'}, {'sampleOriginType.id': 'MONDO:0031332'}, {'sampleOriginType.id': 'MONDO:0019402'}, {'sampleOriginType.id': 'EFO:0009211'}, {'sampleOriginType.id': 'MONDO:0011173'}, {'sampleOriginType.id': 'EFO:0009212'}, {'sampleOriginType.id': 'HP:0003146'}, {'sampleOriginType.id': 'MONDO:0044348'}, {'sampleOriginType.id': 'MONDO:0100241'}, {'sampleOriginType.id': 'EFO:0005576'}, {'sampleOriginType.id': 'EFO:0010863'}, {'sampleOriginType.id': 'EFO:0004527'}, {'sampleOriginType.id': 'EFO:0009213'}, {'sampleOriginType.id': 'EFO:0010858'}, {'sampleOriginType.id': 'EFO:0010776'}, {'sampleOriginType.id': 'EFO:0009243'}, {'sampleOriginType.id': 'EFO:0010761'}, {'sampleOriginType.id': 'EFO:0010846'}, {'sampleOriginType.id': 'CL:0000767'}, {'sampleOriginType.id': 'MONDO:0019740'}, {'sampleOriginType.id': 'EFO:0011039'}, {'sampleOriginType.id': 'MONDO:0044972'}, {'sampleOriginType.id': 'EFO:0010795'}, {'sampleOriginType.id': 'MONDO:0017570'}, {'sampleOriginType.id': 'MONDO:0100433'}, {'sampleOriginType.id': 'EFO:0004587'}, {'sampleOriginType.id': 'CL:0000582'}, {'sampleOriginType.id': 'MONDO:0007686'}, {'sampleOriginType.id': 'EFO:0006614'}, {'sampleOriginType.id': 'MONDO:0018023'}, {'sampleOriginType.id': 'EFO:0009233'}, {'sampleOriginType.id': 'CL:0002357'}, {'sampleOriginType.id': 'EFO:0010876'}, {'sampleOriginType.id': 'EFO:0010870'}, {'sampleOriginType.id': 'MONDO:0014386'}, {'sampleOriginType.id': 'EFO:0010888'}, {'sampleOriginType.id': 'EFO:0010779'}, {'sampleOriginType.id': 'EFO:0010785'}, {'sampleOriginType.id': 'MONDO:0010121'}, {'sampleOriginType.id': 'EFO:0803542'}, {'sampleOriginType.id': 'MONDO:0013622'}, {'sampleOriginType.id': 'EFO:0009157'}, {'sampleOriginType.id': 'EFO:0006572'}, {'sampleOriginType.id': 'MONDO:0009506'}, {'sampleOriginType.id': 'EFO:0010850'}, {'sampleOriginType.id': 'CL:0000081'}, {'sampleOriginType.id': 'EFO:0010886'}, {'sampleOriginType.id': 'EFO:0004306'}, {'sampleOriginType.id': 'EFO:0007992'}, {'sampleOriginType.id': 'EFO:0007996'}, {'sampleOriginType.id': 'CL:0000772'}, {'sampleOriginType.id': 'MONDO:0010120'}, {'sampleOriginType.id': 'E2024-09-30T16:47:31.191407049Z FO:0001221'}, {'sampleOriginType.id': 'CL:0000768'}, {'sampleOriginType.id': 'EFO:0009222'}, {'sampleOriginType.id': 'MONDO:0016242'}, {'sampleOriginType.id': 'CL:0002022'}, {'sampleOriginType.id': 'CL:0002021'}, {'sampleOriginType.id': 'MONDO:0000602'}, {'sampleOriginType.id': 'Orphanet:847'}, {'sampleOriginType.id': 'EFO:0009248'}, {'sampleOriginType.id': 'EFO:0010866'}, {'sampleOriginType.id': 'MONDO:0013597'}, {'sampleOriginType.id': 'EFO:0022546'}, {'sampleOriginType.id': 'EFO:0002229'}, {'sampleOriginType.id': 'EFO:0010868'}, {'sampleOriginType.id': 'EFO:0009203'}, {'sampleOriginType.id': 'EFO:0004348'}, {'sampleOriginType.id': 'MONDO:0013275'}, {'sampleOriginType.id': 'CL:0000771'}, {'sampleOriginType.id': 'BTO:0000133'}, {'sampleOriginType.id': 'EFO:0022507'}, {'sampleOriginType.id': 'EFO:0010802'}, {'sampleOriginType.id': 'EFO:0010842'}, {'sampleOriginType.id': 'MONDO:0016030'}, {'sampleOriginType.id': 'EFO:0009206'}, {'sampleOriginType.id': 'EFO:0010865'}, {'sampleOriginType.id': 'MONDO:0011895'}, {'sampleOriginType.id': 'MONDO:0800451'}, {'sampleOriginType.id': 'EFO:0010879'}, {'sampleOriginType.id': 'Orphanet:848'}, {'sampleOriginType.id': 'EFO:0005635'}, {'sampleOriginType.id': 'EFO:0010760'}, {'sampleOriginType.id': 'EFO:0010794'}, {'sampleOriginType.id': 'EFO:0009204'}, {'sampleOriginType.id': 'EFO:0010871'}, {'sampleOriginType.id': 'EFO:1000014'}, {'sampleOriginType.id': 'MONDO:0031447'}, {'sampleOriginType.id': 'EFO:0010874'}, {'sampleOriginType.id': 'MONDO:0016243'}, {'sampleOriginType.id': 'MONDO:0010745'}, {'sampleOriginType.id': 'EFO:0009240'}, {'sampleOriginType.id': 'EFO:0009234'}, {'sampleOriginType.id': 'EFO:0010848'}, {'sampleOriginType.id': 'EFO:0007991'}, {'sampleOriginType.id': 'MONDO:0012202'}, {'sampleOriginType.id': 'MONDO:0019031'}, {'sampleOriginType.id': 'MONDO:0021024'}, {'sampleOriginType.id': 'EFO:0010769'}, {'sampleOriginType.id': 'EFO:0010773'}, {'sampleOriginType.id': 'EFO:0004694'}, {'sampleOriginType.id': 'MONDO:0100563'}, {'sampleOriginType.id': 'EFO:0010852'}, {'sampleOriginType.id': 'EFO:0010804'}, {'sampleOriginType.id': 'MONDO:0800447'}, {'sampleOriginType.id': 'EFO:0010784'}, {'sampleOriginType.id': 'EFO:0007984'}, {'sampleOriginType.id': 'MONDO:0009158'}, {'sampleOriginType.id': 'EFO:0007172'}, {'sampleOriginType.id': 'MONDO:0009953'}, {'sampleOriginType.id': 'EFO:0007444'}, {'sampleOriginType.id': 'EFO:0006486'}, {'sampleOriginType.id': 'EFO:0008390'}, {'sampleOriginType.id': 'EFO:0004985'}, {'sampleOriginType.id': 'MONDO:0014757'}, {'sampleOriginType.id': 'MONDO:0000440'}, {'sampleOriginType.id': 'EFO:0803544'}, {'sampleOriginType.id': 'EFO:0010864'}, {'sampleOriginType.id': 'EFO:0010838'}, {'sampleOriginType.id': 'Orphanet:231230'}, {'sampleOriginType.id': 'EFO:0006615'}, {'sampleOriginType.id': 'EFO:0002534'}, {'sampleOriginType.id': 'EFO:0000479'}, {'sampleOriginType.id': 'CL:0000769'}, {'sampleOriginType.id': 'EFO:0001254'}, {'sampleOriginType.id': 'EFO:0803543'}, {'sampleOriginType.id': 'MONDO:0015978'}, {'sampleOriginType.id': 'MONDO:0001198'}, {'sampleOriginType.id': 'CL:0000094'}, {'sampleOriginType.id': 'CL:0000562'}, {'sampleOriginType.id': 'EFO:0010889'}, {'sampleOriginType.id': 'EFO:0006653'}, {'sampleOriginType.id': 'MONDO:0016486'}, {'sampleOriginType.id': 'MONDO:0030996'}]}, 'biosample', 'runs', {})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_13_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_14_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_14_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = cross_query(MagicClass, {'$or': [{'sampleOriginType.id': 'UBERON:0000178'}, {'sampleOriginType.id': 'MONDO:0013512'}, {'sampleOriginType.id': 'CL:0000232'}, {'sampleOriginType.id': 'EFO:0004842'}, {'sampleOriginType.id': 'EFO:0007988'}, {'sampleOriginType.id': 'EFO:0004808'}, {'sampleOriginType.id': 'MONDO:0009950'}, {'sampleOriginType.id': 'EFO:0009244'}, {'sampleOriginType.id': 'EFO:0009253'}, {'sampleOriginType.id': 'EFO:0010783'}, {'sampleOriginType.id': 'EFO:0003073'}, {'sampleOriginType.id': 'EFO:0009252'}, {'sampleOriginType.id': 'MONDO:0001117'}, {'sampleOriginType.id': 'MONDO:0018022'}, {'sampleOriginType.id': 'EFO:0010109'}, {'sampleOriginType.id': 'EFO:0010840'}, {'sampleOriginType.id': 'EFO:0010792'}, {'sampleOriginType.id': 'EFO:0005090'}, {'sampleOriginType.id': 'EFO:0010772'}, {'sampleOriginType.id': 'MONDO:0017829'}, {'sampleOriginType.id': 'EFO:0001941'}, {'sampleOriginType.id': 'EFO:0010790'}, {'sampleOriginType.id': 'EFO:0010861'}, {'sampleOriginType.id': 'MONDO:0018749'}, {'sampleOriginType.id': 'EFO:0010849'}, {'sampleOriginType.id': 'EFO:1001467'}, {'sampleOriginType.id': 'MONDO:0017238'}, {'sampleOriginType.id': 'EFO:0007129'}, {'sampleOriginType.id': 'MONDO:0011136'}, {'sampleOriginType.id': 'Orphanet:231242'}, {'sampleOriginType.id': 'EFO:0007481'}, {'sampleOriginType.id': 'EFO:0009215'}, {'sampleOriginType.id': 'MONDO:0017145'}, {'sampleOriginType.id': 'CL:0000775'}, {'sampleOriginType.id': 'MONDO:0008555'}, {'sampleOriginType.id': 'MONDO:0004680'}, {'sampleOriginType.id': 'EFO:0004305'}, {'sampleOriginType.id': 'MONDO:0016490'}, {'sampleOriginType.id': 'MONDO:0007838'}, {'sampleOriginType.id': 'MONDO:0013016'}, {'sampleOriginType.id': 'EFO:0007994'}, {'sampleOriginType.id': 'MONDO:0013623'}, {'sampleOriginType.id': 'CL:0000614'}, {'sampleOriginType.id': 'EFO:0010107'}, {'sampleOriginType.id': 'CL:0000976'}, {'sampleOriginType.id': 'EFO:0009225'}, {'sampleOriginType.id': 'CL:0002318'}, {'sampleOriginType.id': 'EFO:0004309'}, {'sampleOriginType.id': 'EFO:0004526'}, {'sampleOriginType.id': 'EFO:0010843'}, {'sampleOriginType.id': 'CL:0002155'}, {'sampleOriginType.id': 'EFO:0010796'}, {'sampleOriginType.id': 'EFO:0001378'}, {'sampleOriginType.id': 'EFO:0009209'}, {'sampleOriginType.id': 'EFO:0009224'}, {'sampleOriginType.id': 'EFO:0009210'}, {'sampleOriginType.id': 'MONDO:0016489'}, {'sampleOriginType.id': 'EFO:0010781'}, {'sampleOriginType.id': 'Orphanet:98791'}, {'sampleOriginType.id': 'EFO:0600063'}, {'sampleOriginType.id': 'CL:0000580'}, {'sampleOriginType.id': 'EFO:0009226'}, {'sampleOriginType.id': 'EFO:0008542'}, {'sampleOriginType.id': 'EFO:0009236'}, {'sampleOriginType.id': 'MONDO:0018269'}, {'sampleOriginType.id': 'MONDO:0016669'}, {'sampleOriginType.id': 'EFO:0004637'}, {'sampleOriginType.id': 'EFO:0010801'}, {'sampleOriginType.id': 'CL:0000978'}, {'sampleOriginType.id': 'Orphanet:846'}, {'sampleOriginType.id': 'EFO:0007445'}, {'sampleOriginType.id': 'EFO:0009239'}, {'sampleOriginType.id': 'CL:0000774'}, {'sampleOriginType.id': 'Orphanet:330032'}, {'sampleOriginType.id': 'MONDO:0019537'}, {'sampleOriginType.id': 'EFO:0010793'}, {'sampleOriginType.id': 'EFO:0009132'}, {'sampleOriginType.id': 'MONDO:0013517'}, {'sampleOriginType.id': 'EFO:0009218'}, {'sampleOriginType.id': 'MONDO:0018963'}, {'sampleOriginType.id': 'EFO:0010799'}, {'sampleOriginType.id': 'MONDO:0012354'}, {'sampleOriginType.id': 'EFO:0010860'}, {'sampleOriginType.id': 'EFO:0007989'}, {'sampleOriginType.id': 'EFO:0010835'}, {'sampleOriginType.id': 'MONDO:0011603'}, {'sampleOriginType.id': 'CL:0000975'}, {'sampleOriginType.id': 'Orphanet:168615'}, {'sampleOriginType.id': 'MONDO:0019535'}, {'sampleOriginType.id': 'CL:0000770'}, {'sampleOriginType.id': 'EFO:0010108'}, {'sampleOriginType.id': 'EFO:0010884'}, {'sampleOriginType.id': 'EFO:0010867'}, {'sampleOriginType.id': 'EFO:0009246'}, {'sampleOriginType.id': 'EFO:0009219'}, {'sampleOriginType.id': 'EFO:0010856'}, {'sampleOriginType.id': 'MONDO:0044349'}, {'sampleOriginType.id': 'EFO:0004584'}, {'sampleOriginType.id': 'MONDO:0018794'}, {'sampleOriginType.id': 'EFO:0007993'}, {'sampleOriginType.id': 'EFO:0009220'}, {'sampleOriginType.id': 'EFO:0010881'}, {'sampleOriginType.id': 'MONDO:0100326'}, {'sampleOriginType.id': 'EFO:0010768'}, {'sampleOriginType.id': 'EFO:0010862'}, {'sampleOriginType.id': 'MONDO:0000105'}, {'sampleOriginType.id': 'MONDO:0019050'}, {'sampleOriginType.id': 'MONDO:0010122'}, {'sampleOriginType.id': 'EFO:0009238'}, {'sampleOriginType.id': 'MONDO:0019098'}, {'sampleOriginType.id': 'EFO:1001316'}, {'sampleOriginType.id': 'EFO:0009646'}, {'sampleOriginType.id': 'MONDO:0016671'}, {'sampleOriginType.id': 'MONDO:0010308'}, {'sampleOriginType.id': 'MONDO:0008369'}, {'sampleOriginType.id': 'EFO:0004310'}, {'sampleOriginType.id': 'EFO:0010780'}, {'sampleOriginType.id': 'EFO:0006613'}, {'sampleOriginType.id': 'EFO:0008447'}, {'sampleOriginType.id': 'EFO:0008543'}, {'sampleOriginType.id': 'EFO:0010770'}, {'sampleOriginType.id': 'CL:0000977'}, {'sampleOriginType.id': 'EFO:0010887'}, {'sampleOriginType.id': 'EFO:0004629'}, {'sampleOriginType.id': 'MONDO:0018740'}, {'sampleOriginType.id': 'EFO:0010853'}, {'sampleOriginType.id': 'MONDO:0009490'}, {'sampleOriginType.id': 'EFO:0010791'}, {'sampleOriginType.id': 'EFO:0010847'}, {'sampleOriginType.id': 'EFO:0010775'}, {'sampleOriginType.id': 'EFO:0009245'}, {'sampleOriginType.id': 'EFO:0010763'}, {'sampleOriginType.id': 'EFO:0700023'}, {'sampleOriginType.id': 'EFO:0010970'}, {'sampleOriginType.id': 'EFO:0010764'}, {'sampleOriginType.id': 'EFO:0600062'}, {'sampleOriginType.id': 'CL:0000776'}, {'sampleOriginType.id': 'EFO:1001115'}, {'sampleOriginType.id': 'MONDO:0016672'}, {'sampleOriginType.id': 'EFO:0004634'}, {'sampleOriginType.id': 'EFO:0004528'}, {'sampleOriginType.id': 'EFO:0009390'}, {'sampleOriginType.id': 'MONDO:0015579'}, {'sampleOriginType.id': 'EFO:0700066'}, {'sampleOriginType.id': 'EFO:0007987'}, {'sampleOriginType.id': 'MONDO:0014078'}, {'sampleOriginType.id': 'EFO:0006530'}, {'sampleOriginType.id': 'MONDO:0019111'}, {'sampleOriginType.id': 'MONDO:0016360'}, {'sampleOriginType.id': 'EFO:0009250'}, {'sampleOriginType.id': 'MONDO:0015372'}, {'sampleOriginType.id': 'MONDO:0016491'}, {'sampleOriginType.id': 'EFO:0009221'}, {'sampleOriginType.id': 'CL:0000986'}, {'sampleOriginType.id': 'MONDO:0020117'}, {'sampleOriginType.id': 'EFO:0004619'}, {'sampleOriginType.id': 'Orphanet:231386'}, {'sampleOriginType.id': 'EFO:0002339'}, {'sampleOriginType.id': 'EFO:0010774'}, {'sampleOriginType.id': 'EFO:0007990'}, {'sampleOriginType.id': 'EFO:0022585'}, {'sampleOriginType.id': 'EFO:0010778'}, {'sampleOriginType.id': 'MONDO:0007293'}, {'sampleOriginType.id': 'EFO:0004633'}, {'sampleOriginType.id': 'EFO:1001996'}, {'sampleOriginType.id': 'EFO:0008446'}, {'sampleOriginType.id': 'EFO:0002322'}, {'sampleOriginType.id': 'UBERON:0001969'}, {'sampleOriginType.id': 'CL:0000985'}, {'sampleOriginType.id': 'EFO:0009181'}, {'sampleOriginType.id': 'CL:0000974'}, {'sampleOriginType.id': 'CL:0000951'}, {'sampleOriginType.id': 'EFO:0010105'}, {'sampleOriginType.id': 'EFO:0009249'}, {'sampleOriginType.id': 'EFO:0803346'}, {'sampleOriginType.id': 'EFO:0005845'}, {'sampleOriginType.id': 'EFO:0010880'}, {'sampleOriginType.id': 'MONDO:0044347'}, {'sampleOriginType.id': 'EFO:0007615'}, {'sampleOriginType.id': 'EFO:0010788'}, {'sampleOriginType.id': 'MONDO:0018922'}, {'sampleOriginType.id': 'MONDO:0016630'}, {'sampleOriginType.id': 'EFO:0007978'}, {'sampleOriginType.id': 'EFO:0010855'}, {'sampleOriginType.id': 'EFO:0006609'}, {'sampleOriginType.id': 'EFO:0006617'}, {'sampleOriginType.id': 'EFO:0010859'}, {'sampleOriginType.id': 'EFO:0009202'}, {'sampleOriginType.id': 'MONDO:0012775'}, {'sampleOriginType.id': 'EFO:0008582'}, {'sampleOriginType.id': 'EFO:0009230'}, {'sampleOriginType.id': 'EFO:0009498'}, {'sampleOriginType.id': 'EFO:0000777'}, {'sampleOriginType.id': 'EFO:0010800'}, {'sampleOriginType.id': 'EFO:0001253'}, {'sampleOriginType.id': 'EFO:0010782'}, {'sampleOriginType.id': 'EFO:0010890'}, {'sampleOriginType.id': 'EFO:0004536'}, {'sampleOriginType.id': 'MONDO:0009694'}, {'sampleOriginType.id': 'MONDO:0043768'}, {'sampleOriginType.id': 'EFO:0010837'}, {'sampleOriginType.id': 'EFO:0010857'}, {'sampleOriginType.id': 'EFO:0004630'}, {'sampleOriginType.id': 'EFO:0009229'}, {'sampleOriginType.id': 'EFO:0009214'}, {'sampleOriginType.id': 'CL:0000392'}, {'sampleOriginType.id': 'MONDO:0008332'}, {'sampleOriginType.id': 'EFO:0006616'}, {'sampleOriginType.id': 'EFO:0006619'}, {'sampleOriginType.id': 'MONDO:0800452'}, {'sampleOriginType.id': 'EFO:0009388'}, {'sampleOriginType.id': 'EFO:0009216'}, {'sampleOriginType.id': 'EFO:0009247'}, {'sampleOriginType.id': 'MONDO:0001909'}, {'sampleOriginType.id': 'MONDO:0001197'}, {'sampleOriginType.id': 'EFO:0009217'}, {'sampleOriginType.id': 'EFO:0007995'}, {'sampleOriginType.id': 'Orphanet:231249'}, {'sampleOriginType.id': 'EFO:0010789'}, {'sampleOriginType.id': 'Orphanet:231393'}, {'sampleOriginType.id': 'Orphanet:168612'}, {'sampleOriginType.id': 'EFO:0009389'}, {'sampleOriginType.id': 'MONDO:0011381'}, {'sampleOriginType.id': 'EFO:0022042'}, {'sampleOriginType.id': 'MONDO:0008497'}, {'sampleOriginType.id': 'CL:0000595'}, {'sampleOriginType.id': 'MONDO:0011382'}, {'sampleOriginType.id': 'MONDO:0012031'}, {'sampleOriginType.id': 'EFO:0010883'}, {'sampleOriginType.id': 'EFO:0010851'}, {'sampleOriginType.id': 'EFO:0004640'}, {'sampleOriginType.id': 'MONDO:0018896'}, {'sampleOriginType.id': 'EFO:0010845'}, {'sampleOriginType.id': 'EFO:0004623'}, {'sampleOriginType.id': 'MONDO:0009276'}, {'sampleOriginType.id': 'EFO:0022508'}, {'sampleOriginType.id': 'MONDO:0016668'}, {'sampleOriginType.id': 'GO:0070527'}, {'sampleOriginType.id': 'EFO:0010878'}, {'sampleOriginType.id': 'CL:0000987'}, {'sampleOriginType.id': 'Orphanet:231401'}, {'sampleOriginType.id': 'MONDO:0008553'}, {'sampleOriginType.id': 'EFO:0001219'}, {'sampleOriginType.id': 'EFO:0004541'}, {'sampleOriginType.id': 'EFO:0600027'}, {'sampleOriginType.id': 'EFO:0022579'}, {'sampleOriginType.id': 'EFO:0002207'}, {'sampleOriginType.id': 'CL:0000560'}, {'sampleOriginType.id': 'EFO:0004308'}, {'sampleOriginType.id': 'CL:0000773'}, {'sampleOriginType.id': 'EFO:0009223'}, {'sampleOriginType.id': 'EFO:0004586'}, {'sampleOriginType.id': 'MONDO:0011399'}, {'sampleOriginType.id': 'EFO:0010873'}, {'sampleOriginType.id': 'EFO:0009251'}, {'sampleOriginType.id': 'EFO:0007160'}, {'sampleOriginType.id': 'CL:0000041'}, {'sampleOriginType.id': 'EFO:1001200'}, {'sampleOriginType.id': 'MONDO:0018268'}, {'sampleOriginType.id': 'MONDO:0044635'}, {'sampleOriginType.id': 'EFO:0010844'}, {'sampleOriginType.id': 'EFO:0006552'}, {'sampleOriginType.id': 'EFO:0006654'}, {'sampleOriginType.id': 'EFO:0010882'}, {'sampleOriginType.id': 'EFO:0001068'}, {'sampleOriginType.id': 'MONDO:0000009'}, {'sampleOriginType.id': 'EFO:0006618'}, {'sampleOriginType.id': 'EFO:0010872'}, {'sampleOriginType.id': 'CL:0000043'}, {'sampleOriginType.id': 'MONDO:0011422'}, {'sampleOriginType.id': 'MONDO:0011268'}, {'sampleOriginType.id': 'EFO:0010854'}, {'sampleOriginType.id': 'CL:0000387'}, {'sampleOriginType.id': 'EFO:0006611'}, {'sampleOriginType.id': 'EFO:0010836'}, {'sampleOriginType.id': 'MONDO:0030867'}, {'sampleOriginType.id': 'EFO:0010762'}, {'sampleOriginType.id': 'EFO:0006612'}, {'sampleOriginType.id': 'EFO:0007629'}, {'sampleOriginType.id': 'UBERON:0012168'}, {'sampleOriginType.id': 'EFO:0004576'}, {'sampleOriginType.id': 'CL:0000786'}, {'sampleOriginType.id': 'EFO:0009232'}, {'sampleOriginType.id': 'EFO:1001112'}, {'sampleOriginType.id': 'EFO:0010839'}, {'sampleOriginType.id': 'MONDO:0014536'}, {'sampleOriginType.id': 'EFO:0004833'}, {'sampleOriginType.id': 'EFO:0010106'}, {'sampleOriginType.id': 'EFO:0006716'}, {'sampleOriginType.id': 'EFO:0010875'}, {'sampleOriginType.id': 'EFO:0009231'}, {'sampleOriginType.id': 'MONDO:0011988'}, {'sampleOriginType.id': 'MONDO:0011555'}, {'sampleOriginType.id': 'EFO:0010786'}, {'sampleOriginType.id': 'MONDO:0016487'}, {'sampleOriginType.id': 'EFO:0006857'}, {'sampleOriginType.id': 'MONDO:0016670'}, {'sampleOriginType.id': 'EFO:0009205'}, {'sampleOriginType.id': 'CL:0000947'}, {'sampleOriginType.id': 'EFO:0004304'}, {'sampleOriginType.id': 'MONDO:0002249'}, {'sampleOriginType.id': 'EFO:0008087'}, {'sampleOriginType.id': 'EFO:0009208'}, {'sampleOriginType.id': 'MONDO:0018795'}, {'sampleOriginType.id': 'EFO:0022513'}, {'sampleOriginType.id': 'EFO:0010841'}, {'sampleOriginType.id': 'EFO:0600058'}, {'sampleOriginType.id': 'MONDO:0016450'}, {'sampleOriginType.id': 'EFO:0010869'}, {'sampleOriginType.id': 'EFO:0005091'}, {'sampleOriginType.id': 'EFO:0006553'}, {'sampleOriginType.id': 'EFO:0600059'}, {'sampleOriginType.id': 'EFO:1000641'}, {'sampleOriginType.id': 'MONDO:0010743'}, {'sampleOriginType.id': 'EFO:0007997'}, {'sampleOriginType.id': 'EFO:0010803'}, {'sampleOriginType.id': 'EFO:0009235'}, {'sampleOriginType.id': 'MONDO:0009885'}, {'sampleOriginType.id': 'EFO:0010798'}, {'sampleOriginType.id': 'EFO:0009228'}, {'sampleOriginType.id': 'HP:0003530'}, {'sampleOriginType.id': 'MONDO:0002245'}, {'sampleOriginType.id': 'EFO:0010877'}, {'sampleOriginType.id': 'EFO:0010797'}, {'sampleOriginType.id': 'EFO:0009497'}, {'sampleOriginType.id': 'MONDO:0010480'}, {'sampleOriginType.id': 'EFO:0009133'}, {'sampleOriginType.id': 'EFO:0010766'}, {'sampleOriginType.id': 'EFO:0600060'}, {'sampleOriginType.id': 'CL:0000390'}, {'sampleOriginType.id': 'EFO:0010885'}, {'sampleOriginType.id': 'EFO:1001264'}, {'sampleOriginType.id': 'EFO:0007985'}, {'sampleOriginType.id': 'EFO:0004509'}, {'sampleOriginType.id': 'CL:0000096'}, {'sampleOriginType.id': 'EFO:0600061'}, {'sampleOriginType.id': 'EFO:0020902'}, {'sampleOriginType.id': 'EFO:0009237'}, {'sampleOriginType.id': 'EFO:0009227'}, {'sampleOriginType.id': 'EFO:0010777'}, {'sampleOriginType.id': 'EFO:0009188'}, {'sampleOriginType.id': 'EFO:0009241'}, {'sampleOriginType.id': 'CL:0000612'}, {'sampleOriginType.id': 'EFO:0009134'}, {'sampleOriginType.id': 'MONDO:0008557'}, {'sampleOriginType.id': 'MONDO:0014518'}, {'sampleOriginType.id': 'EFO:0009242'}, {'sampleOriginType.id': 'CL:0000233'}, {'sampleOriginType.id': 'MONDO:0030827'}, {'sampleOriginType.id': 'EFO:0004301'}, {'sampleOriginType.id': 'Orphanet:46532'}, {'sampleOriginType.id': 'MONDO:0031332'}, {'sampleOriginType.id': 'MONDO:0019402'}, {'sampleOriginType.id': 'EFO:0009211'}, {'sampleOriginType.id': 'MONDO:0011173'}, {'sampleOriginType.id': 'EFO:0009212'}, {'sampleOriginType.id': 'HP:0003146'}, {'sampleOriginType.id': 'MONDO:0044348'}, {'sampleOriginType.id': 'MONDO:0100241'}, {'sampleOriginType.id': 'EFO:0005576'}, {'sampleOriginType.id': 'EFO:0010863'}, {'sampleOriginType.id': 'EFO:0004527'}, {'sampleOriginType.id': 'EFO:0009213'}, {'sampleOriginType.id': 'EFO:0010858'}, {'sampleOriginType.id': 'EFO:0010776'}, {'sampleOriginType.id': 'EFO:0009243'}, {'sampleOriginType.id': 'EFO:0010761'}, {'sampleOriginType.id': 'EFO:0010846'}, {'sampleOriginType.id': 'CL:0000767'}, {'sampleOriginType.id': 'MONDO:0019740'}, {'sampleOriginType.id': 'EFO:0011039'}, {'sampleOriginType.id': 'MONDO:0044972'}, {'sampleOriginType.id': 'EFO:0010795'}, {'sampleOriginType.id': 'MONDO:0017570'}, {'sampleOriginType.id': 'MONDO:0100433'}, {'sampleOriginType.id': 'EFO:0004587'}, {'sampleOriginType.id': 'CL:0000582'}, {'sampleOriginType.id': 'MONDO:0007686'}, {'sampleOriginType.id': 'EFO:0006614'}, {'sampleOriginType.id': 'MONDO:0018023'}, {'sampleOriginType.id': 'EFO:0009233'}, {'sampleOriginType.id': 'CL:0002357'}, {'sampleOriginType.id': 'EFO:0010876'}, {'sampleOriginType.id': 'EFO:0010870'}, {'sampleOriginType.id': 'MONDO:0014386'}, {'sampleOriginType.id': 'EFO:0010888'}, {'sampleOriginType.id': 'EFO:0010779'}, {'sampleOriginType.id': 'EFO:0010785'}, {'sampleOriginType.id': 'MONDO:0010121'}, {'sampleOriginType.id': 'EFO:0803542'}, {'sampleOriginType.id': 'MONDO:0013622'}, {'sampleOriginType.id': 'EFO:0009157'}, {'sampleOriginType.id': 'EFO:0006572'}, {'sampleOriginType.id': 'MONDO:0009506'}, {'sampleOriginType.id': 'EFO:0010850'}, {'sampleOriginType.id': 'CL:0000081'}, {'sampleOriginType.id': 'EFO:0010886'}, {'sampleOriginType.id': 'EFO:0004306'}, {'sampleOriginType.id': 'EFO:0007992'}, {'sampleOriginType.id': 'EFO:0007996'}, {'sampleOriginType.id': 'CL:0000772'}, {'sampleOriginType.id': 'MONDO:0010120'}, {'sampleOriginType.id': 'E2024-09-30T16:47:31.191407049Z FO:0001221'}, {'sampleOriginType.id': 'CL:0000768'}, {'sampleOriginType.id': 'EFO:0009222'}, {'sampleOriginType.id': 'MONDO:0016242'}, {'sampleOriginType.id': 'CL:0002022'}, {'sampleOriginType.id': 'CL:0002021'}, {'sampleOriginType.id': 'MONDO:0000602'}, {'sampleOriginType.id': 'Orphanet:847'}, {'sampleOriginType.id': 'EFO:0009248'}, {'sampleOriginType.id': 'EFO:0010866'}, {'sampleOriginType.id': 'MONDO:0013597'}, {'sampleOriginType.id': 'EFO:0022546'}, {'sampleOriginType.id': 'EFO:0002229'}, {'sampleOriginType.id': 'EFO:0010868'}, {'sampleOriginType.id': 'EFO:0009203'}, {'sampleOriginType.id': 'EFO:0004348'}, {'sampleOriginType.id': 'MONDO:0013275'}, {'sampleOriginType.id': 'CL:0000771'}, {'sampleOriginType.id': 'BTO:0000133'}, {'sampleOriginType.id': 'EFO:0022507'}, {'sampleOriginType.id': 'EFO:0010802'}, {'sampleOriginType.id': 'EFO:0010842'}, {'sampleOriginType.id': 'MONDO:0016030'}, {'sampleOriginType.id': 'EFO:0009206'}, {'sampleOriginType.id': 'EFO:0010865'}, {'sampleOriginType.id': 'MONDO:0011895'}, {'sampleOriginType.id': 'MONDO:0800451'}, {'sampleOriginType.id': 'EFO:0010879'}, {'sampleOriginType.id': 'Orphanet:848'}, {'sampleOriginType.id': 'EFO:0005635'}, {'sampleOriginType.id': 'EFO:0010760'}, {'sampleOriginType.id': 'EFO:0010794'}, {'sampleOriginType.id': 'EFO:0009204'}, {'sampleOriginType.id': 'EFO:0010871'}, {'sampleOriginType.id': 'EFO:1000014'}, {'sampleOriginType.id': 'MONDO:0031447'}, {'sampleOriginType.id': 'EFO:0010874'}, {'sampleOriginType.id': 'MONDO:0016243'}, {'sampleOriginType.id': 'MONDO:0010745'}, {'sampleOriginType.id': 'EFO:0009240'}, {'sampleOriginType.id': 'EFO:0009234'}, {'sampleOriginType.id': 'EFO:0010848'}, {'sampleOriginType.id': 'EFO:0007991'}, {'sampleOriginType.id': 'MONDO:0012202'}, {'sampleOriginType.id': 'MONDO:0019031'}, {'sampleOriginType.id': 'MONDO:0021024'}, {'sampleOriginType.id': 'EFO:0010769'}, {'sampleOriginType.id': 'EFO:0010773'}, {'sampleOriginType.id': 'EFO:0004694'}, {'sampleOriginType.id': 'MONDO:0100563'}, {'sampleOriginType.id': 'EFO:0010852'}, {'sampleOriginType.id': 'EFO:0010804'}, {'sampleOriginType.id': 'MONDO:0800447'}, {'sampleOriginType.id': 'EFO:0010784'}, {'sampleOriginType.id': 'EFO:0007984'}, {'sampleOriginType.id': 'MONDO:0009158'}, {'sampleOriginType.id': 'EFO:0007172'}, {'sampleOriginType.id': 'MONDO:0009953'}, {'sampleOriginType.id': 'EFO:0007444'}, {'sampleOriginType.id': 'EFO:0006486'}, {'sampleOriginType.id': 'EFO:0008390'}, {'sampleOriginType.id': 'EFO:0004985'}, {'sampleOriginType.id': 'MONDO:0014757'}, {'sampleOriginType.id': 'MONDO:0000440'}, {'sampleOriginType.id': 'EFO:0803544'}, {'sampleOriginType.id': 'EFO:0010864'}, {'sampleOriginType.id': 'EFO:0010838'}, {'sampleOriginType.id': 'Orphanet:231230'}, {'sampleOriginType.id': 'EFO:0006615'}, {'sampleOriginType.id': 'EFO:0002534'}, {'sampleOriginType.id': 'EFO:0000479'}, {'sampleOriginType.id': 'CL:0000769'}, {'sampleOriginType.id': 'EFO:0001254'}, {'sampleOriginType.id': 'EFO:0803543'}, {'sampleOriginType.id': 'MONDO:0015978'}, {'sampleOriginType.id': 'MONDO:0001198'}, {'sampleOriginType.id': 'CL:0000094'}, {'sampleOriginType.id': 'CL:0000562'}, {'sampleOriginType.id': 'EFO:0010889'}, {'sampleOriginType.id': 'EFO:0006653'}, {'sampleOriginType.id': 'MONDO:0016486'}, {'sampleOriginType.id': 'MONDO:0030996'}]}, 'biosample', 'analyses', {})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_14_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_cross_query_15_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_cross_query_15_is_working():
                MagicClass = MagicMock(_id='hohoho')
                resp = apply_filters(MagicClass, {'$and': [{'variation.location.interval.start.value': {'$gte': 16050074}}, {'variation.location.interval.end.value': {'$lte': 16050075}}, {'variation.alternateBases': {'$eq': 'A'}}, {'variation.referenceBases': {'$eq': 'G'}}, {'$and': [{'$or': [{'identifiers.genomicHGVSId': {'$regex': '^NC_000022'}}]}]}]}, [{'id': 'GENO:GENO_0000458', 'scope': 'genomicVariation'}], 'individuals', {'$and': [{'variation.location.interval.start.value': {'$gte': 16050074}}, {'variation.location.interval.end.value': {'$lte': 16050075}}, {'variation.alternateBases': {'$eq': 'A'}}, {'variation.referenceBases': {'$eq': 'G'}}, {'$and': [{'$or': [{'identifiers.genomicHGVSId': {'$regex': '^NC_000022'}}]}]}]})
                assert resp != {}
            loop.run_until_complete(test_check_cross_query_15_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_alphanumeric_equal_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_alphanumeric_equal_query_is_working():
                resp = await client.post("/api/individuals", json={
                "meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
            {"id": "ethnicity",
                    "operator": "=",
                    "value": "British",
            "scope":"individual"}],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
            }
            )

                assert resp.status == 200
            loop.run_until_complete(test_check_alphanumeric_equal_query_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_alphanumeric_like_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_alphanumeric_like_query_is_working():
                resp = await client.post("/api/individuals", json={
                "meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
            {"id": "ethnicity",
                    "operator": "=",
                    "value": "%itish%",
            "scope":"individual"}],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
            }
            )

                assert resp.status == 200
            loop.run_until_complete(test_check_alphanumeric_like_query_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_alphanumeric_not_like_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_alphanumeric_not_like_query_is_working():
                resp = await client.post("/api/individuals", json={
                "meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
            {"id": "ethnicity",
                    "operator": "!",
                    "value": "%itish%",
            "scope":"individual"}],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
            }
            )

                assert resp.status == 200
            loop.run_until_complete(test_check_alphanumeric_not_like_query_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_alphanumeric_not_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_alphanumeric_not_query_is_working():
                resp = await client.post("/api/individuals", json={
                "meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
            {"id": "ethnicity",
                    "operator": "!",
                    "value": "British",
            "scope":"individual"}],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
            }
            )

                assert resp.status == 200
            loop.run_until_complete(test_check_alphanumeric_not_query_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_iso8601duration_gt_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_iso8601duration_gt_query_is_working():
                resp = await client.post("/api/individuals", json={
                "meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
            {"id": "diseases.ageOfOnset.iso8601duration",
                    "operator": ">",
                    "value": "45",
            "scope":"individual"}],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
            }
            )

                assert resp.status == 200
            loop.run_until_complete(test_check_iso8601duration_gt_query_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_iso8601duration_ls_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_iso8601duration_ls_query_is_working():
                resp = await client.post("/api/individuals", json={
                "meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
            {"id": "diseases.ageOfOnset.iso8601duration",
                    "operator": "<",
                    "value": "45",
            "scope":"individual"}],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
            }
            )

                assert resp.status == 200
            loop.run_until_complete(test_check_iso8601duration_ls_query_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_measurement_value_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_measurement_value_query_is_working():
                resp = await client.post("/api/individuals", json={
                "meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
                            {
                        "id": "Weight",
                        "operator": ">",
                        "value": "75"
                    }, 
                ],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
            }
            )

                assert resp.status == 200
            loop.run_until_complete(test_check_measurement_value_query_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_custom_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_custom_query_is_working():
                resp = await client.post("/api/biosamples", json={
                "meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
                            {
                        "id": "sampleOriginType:blood"
                    } 
                , 
                ],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
            }
            )

                assert resp.status == 200
            loop.run_until_complete(test_check_custom_query_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_range_query_with_variant_min_and_max_lengths_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_range_query_with_variant_min_and_max_lengths_working():
                resp = await client.get("/api/g_variants?start=16050074&end=16050075&variantMinLength=0&variantMaxLength=3&referenceName=22")
                assert resp.status == 200
            loop.run_until_complete(test_check_range_query_with_variant_min_and_max_lengths_working())
            loop.run_until_complete(client.close())
    def test_main_check_filters_as_request_parameter_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_filters_as_request_parameter_working():
                resp = await client.get("/api/individuals?filters=NCIT:C42331")
                assert resp.status == 200
            loop.run_until_complete(test_check_filters_as_request_parameter_working())
            loop.run_until_complete(client.close())
    def test_main_check_datasets_list_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_datasets_list_query_is_working():
                resp = await client.post("/api/individuals", json={
                "meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {
                "datasets": ["CINECA_synthetic_cohort_EUROPE_UK1", "Hola"]
                },
                    "filters": [                ],
                    "includeResultsetResponses": "HIT",
                    "pagination": {
                        "skip": 0,
                        "limit": 101
                    },
                    "testMode": False,
                    "requestedGranularity": "record"
                }
            }
            )

                assert resp.status == 200
            loop.run_until_complete(test_check_datasets_list_query_is_working())
            loop.run_until_complete(client.close())
    def test_main_check_range_query_with_variant_assemblyId_GRCh38_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_range_query_with_variant_assemblyId_GRCh38_working():
                resp = await client.get("/api/g_variants?start=16050074&end=16050075&assemblyId=GRCh38&referenceName=22")
                assert resp.status == 200
            loop.run_until_complete(test_check_range_query_with_variant_assemblyId_GRCh38_working())
            loop.run_until_complete(client.close())
    def test_main_check_range_query_with_variant_assemblyId_GRCh37_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_range_query_with_variant_assemblyId_GRCh37_working():
                resp = await client.get("/api/g_variants?start=16050074&end=16050075&assemblyId=GRCh37&referenceName=22")
                assert resp.status == 200
            loop.run_until_complete(test_check_range_query_with_variant_assemblyId_GRCh37_working())
            loop.run_until_complete(client.close())
    def test_main_check_range_query_with_variant_assemblyId_NCBI36_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_range_query_with_variant_assemblyId_NCBI36_working():
                resp = await client.get("/api/g_variants?start=16050074&end=16050075&assemblyId=NCBI36&referenceName=22")
                assert resp.status == 200
            loop.run_until_complete(test_check_range_query_with_variant_assemblyId_NCBI36_working())
            loop.run_until_complete(client.close())
    def test_main_check_NONE_count_query_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_NONE_count_query_is_working():
                resp = await client.post("/api/individuals", json={
                "meta": {
                    "apiVersion": "2.0"
                },
                "query": { "requestParameters": {        },
                    "filters": [
            {"id": "ethnicity",
                    "operator": "!",
                    "value": "%itish%",
            "scope":"individual"}],
                    "includeResultsetResponses": "NONE",
                    "pagination": {
                        "skip": 0,
                        "limit": 10
                    },
                    "testMode": False,
                    "requestedGranularity": "count"
                }
            }
            )

                assert resp.status == 200
            loop.run_until_complete(test_check_NONE_count_query_is_working())
            loop.run_until_complete(client.close())





if __name__ == '__main__':
    unittest.main()