import json
from beacon.logs.logs import log_with_args
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

class EndpointView(web.View):
    def __init__(self, request: Request):
        self._request= request
        self._id = generate_txid(self)

class ControlView(EndpointView):    
    @log_with_args(level)
    def calculate(self, request, nombre):
        try:
            status = nombre/2
        except Exception:
            raise
        return status
    
    @dataset_permissions
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
        response_obj = await builder(request, datasets, qparams)
        return web.Response(text=dumps(response_obj), status=200, content_type='application/json')

    async def get(self):
        return await self.genomicVariations(self.request)

    async def post(self):
        return await self.genomicVariations(self.request)

async def initialize(app):
    pass

async def destroy(app):
    pass


async def create_api():
    app = web.Application()
    app.on_startup.append(initialize)
    app.on_cleanup.append(destroy)
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