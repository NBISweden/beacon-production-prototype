
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
    def test_main_check_post_cross_query_individuals_biosamples_is_working(self):
        with loop_context() as loop:
            app = create_app()
            client = TestClient(TestServer(app), loop=loop)
            loop.run_until_complete(client.start_server())
            async def test_check_post_cross_query_biosamples_individuals_is_working():
                resp = await client.post("/api/biosamples", data=json.dumps({"meta": {
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
                }), headers={'Content-Type': 'application/json'})
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

if __name__ == '__main__':
    unittest.main()


