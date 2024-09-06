import json
from beacon.logs.logs import log_with_args, LOG
from beacon.conf.conf import level
from beacon.info.info import info_response
import asyncio
import aiohttp.web as web
from bson.json_util import dumps
from aiohttp.web_request import Request
from beacon.utils.txid import generate_txid
from beacon.utils.requests import get_qparams
from beacon.permissions.__main__ import dataset_permissions
from beacon.response.builder import builder
from bson import json_util
from beacon.response.granularity import build_beacon_error_response
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

class ControlView(EndpointView):    
    @log_with_args(level)
    def calculate(self, request, nombre):
        try:
            status = nombre/2
        except Exception:
            raise
        return status
    
    @log_with_args(level)
    async def control(self, request):
        qparams = get_qparams(self, request)
        self.calculate(self, 4)
        response_obj = {'resp': 'hello world'}
        return web.Response(text=json.dumps(response_obj), status=200, content_type='application/json')

    async def get(self):
        return await self.control(self.request)

    async def post(self):
        return await self.control(self.request)
    
class InfoView(EndpointView):
    @log_with_args(level)
    async def info(self, request):
        response_obj = info_response
        return web.Response(text=json.dumps(response_obj), status=200, content_type='application/json')

    async def get(self):
        return await self.info(self.request)

    async def post(self):
        return await self.info(self.request)

class GenomicVariations(EndpointView):
    @dataset_permissions
    @log_with_args(level)
    async def genomicVariations(self, request, datasets, qparams):
        try:
            response_obj = await builder(self, request, datasets, qparams)
            return web.Response(text=json_util.dumps(response_obj), status=200, content_type='application/json')
        except Exception:
            raise


    async def get(self):
        try:
            return await self.genomicVariations(self.request)
        except Exception as e:
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

    async def post(self):
        try:
            return await self.genomicVariations(self.request)
        except Exception as e:
            response_obj = build_beacon_error_response(self, ErrorClass.error_code, 'prova', ErrorClass.error_response)
            return web.Response(text=json_util.dumps(response_obj), status=ErrorClass.error_code, content_type='application/json')

async def initialize(app):
    pass

def _on_shutdown(pid):
    time.sleep(6)

    #  Sending SIGINT to close server
    os.kill(pid, signal.SIGINT)


async def _graceful_shutdown_ctx(app):
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


async def create_api():
    app = web.Application()
    app.on_startup.append(initialize)
    app.cleanup_ctx.append(_graceful_shutdown_ctx)
    app.add_routes([web.view('/control', ControlView)])
    app.add_routes([web.view('/info', InfoView)])
    app.add_routes([web.view('/g_variants', GenomicVariations)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 5070)
    await site.start()

    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(create_api())