from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
import asyncio
import aiohttp.web as web
from aiohttp.web_request import Request
from beacon.utils.txid import generate_txid
from beacon.permissions.__main__ import dataset_permissions
from beacon.response.builder import builder, collection_builder, info_builder, configuration_builder, map_builder, entry_types_builder, service_info_builder, filtering_terms_builder
from bson import json_util
from beacon.response.catalog import build_beacon_error_response
from beacon.request.classes import ErrorClass
import time
import os
import signal
from threading import Thread

class EndpointView(web.View):
    def __init__(self, request: Request):
        self._request= request
        self._id = generate_txid(self)
        ErrorClass.error_code = None
        ErrorClass.error_response = None

class ServiceInfo(EndpointView):
    @log_with_args(level)
    async def service_info(self, request):
        try:
            response_obj = await service_info_builder(self, request)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def get(self):
        try:
            return await self.service_info(self.request)
        except Exception as e:# pragma: no cover
            raise

    async def post(self):
        try:
            return await self.service_info(self.request)
        except Exception as e:# pragma: no cover
            raise

class EntryTypes(EndpointView):
    @log_with_args(level)
    async def entry_types(self, request):
        try:
            response_obj = await entry_types_builder(self, request)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.entry_types(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.entry_types(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

class Map(EndpointView):
    @log_with_args(level)
    async def map(self, request):
        try:
            response_obj = await map_builder(self, request)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.map(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.map(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

class Configuration(EndpointView):
    @log_with_args(level)
    async def configuration(self, request):
        try:
            response_obj = await configuration_builder(self, request)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.configuration(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.configuration(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

class Info(EndpointView):
    @log_with_args(level)
    async def info(self, request):
        try:
            response_obj = await info_builder(self, request)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.info(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.info(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

class Datasets(EndpointView):
    @log_with_args(level)
    async def datasets(self, request):
        try:
            entry_type='datasets'
            response_obj = await collection_builder(self, request, entry_type)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.datasets(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.datasets(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')
        
class Cohorts(EndpointView):
    @log_with_args(level)
    async def cohorts(self, request):
        try:
            entry_type='cohorts'
            response_obj = await collection_builder(self, request, entry_type)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.cohorts(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.cohorts(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')
        
class FilteringTerms(EndpointView):
    @dataset_permissions
    @log_with_args(level)
    async def filteringTerms(self, request, datasets, qparams):
        try:
            entry_type='filtering_terms'
            response_obj = await filtering_terms_builder(self, request, datasets, qparams, entry_type)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.filteringTerms(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.filteringTerms(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

class GenomicVariations(EndpointView):
    @dataset_permissions
    @log_with_args(level)
    async def genomicVariations(self, request, datasets, qparams):
        try:
            entry_type='genomicVariations'
            response_obj = await builder(self, request, datasets, qparams, entry_type)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.genomicVariations(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.genomicVariations(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')
        
class Individuals(EndpointView):
    @dataset_permissions
    @log_with_args(level)
    async def individuals(self, request, datasets, qparams):
        try:
            entry_type='individuals'
            response_obj = await builder(self, request, datasets, qparams, entry_type)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.individuals(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.individuals(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')
        
class Analyses(EndpointView):
    @dataset_permissions
    @log_with_args(level)
    async def analyses(self, request, datasets, qparams):
        try:
            entry_type='analyses'
            response_obj = await builder(self, request, datasets, qparams, entry_type)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.analyses(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.analyses(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

class Biosamples(EndpointView):
    @dataset_permissions
    @log_with_args(level)
    async def biosamples(self, request, datasets, qparams):
        try:
            entry_type='biosamples'
            response_obj = await builder(self, request, datasets, qparams, entry_type)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.biosamples(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.biosamples(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

class Runs(EndpointView):
    @dataset_permissions
    @log_with_args(level)
    async def runs(self, request, datasets, qparams):
        try:
            entry_type='runs'
            response_obj = await builder(self, request, datasets, qparams, entry_type)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:# pragma: no cover
            raise

    async def get(self):
        try:
            return await self.runs(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.runs(self.request)
        except Exception as e:# pragma: no cover
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

async def initialize(app):# pragma: no cover
    pass

def _on_shutdown(pid):# pragma: no cover
    time.sleep(6)

    #  Sending SIGINT to close server
    os.kill(pid, signal.SIGINT)


async def _graceful_shutdown_ctx(app):# pragma: no cover
    def graceful_shutdown_sigterm_handler():
        nonlocal thread
        thread = Thread(target=_on_shutdown, args=(os.getpid(),))
        thread.start()

    thread = None

    loop = asyncio.get_event_loop()
    loop.add_signal_handler(
        signal.SIGTERM, graceful_shutdown_sigterm_handler,
    )

    yield

    loop.remove_signal_handler(signal.SIGTERM)

    if thread is not None:
        thread.join()


async def create_api():# pragma: no cover
    app = web.Application()
    app.on_startup.append(initialize)
    app.cleanup_ctx.append(_graceful_shutdown_ctx)
    app.add_routes([web.view('/api', Info)])
    app.add_routes([web.view('/api/info', Info)])
    app.add_routes([web.view('/api/entry_types', EntryTypes)])
    app.add_routes([web.view('/api/service-info', ServiceInfo)])
    app.add_routes([web.view('/api/configuration', Configuration)])
    app.add_routes([web.view('/api/map', Map)])
    app.add_routes([web.view('/api/filtering_terms', FilteringTerms)])
    app.add_routes([web.view('/api/datasets', Datasets)])
    app.add_routes([web.view('/api/g_variants', GenomicVariations)])
    app.add_routes([web.view('/api/individuals', Individuals)])
    app.add_routes([web.view('/api/analyses', Analyses)])
    app.add_routes([web.view('/api/biosamples', Biosamples)])
    app.add_routes([web.view('/api/runs', Runs)])
    app.add_routes([web.view('/api/cohorts', Cohorts)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 5050)
    await site.start()

    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':# pragma: no cover
    asyncio.run(create_api())