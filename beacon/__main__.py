import json
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from beacon.info.info import info_response
import asyncio
import aiohttp.web as web
import uuid

def generate_txid():
    uniqueid = uuid.uuid1()
    uniqueid = str(uniqueid)[0:8]
    return uniqueid

class EndpointView(web.View):
    id = generate_txid()
    
class ControlView(EndpointView):    
    @log_with_args(level, EndpointView.id)
    def calculate(request, nombre):
        try:
            status = nombre/2
        except Exception:
            raise
        return status
    
    @log_with_args(level, EndpointView.id)
    async def control(self, request):
        self.calculate(4)
        response_obj = {'resp': 'hello world'}
        return web.Response(text=json.dumps(response_obj), status=200, content_type='application/json')

    async def get(self):
        return await self.control(self.request)

    async def post(self):
        return await self.control(self.request)


async def initialize(app):
    pass

async def destroy(app):
    pass

#passar permissions com a decorator

async def info(request):
    return web.Response(text=json.dumps(info_response), status=200, content_type='application/json')



async def create_api():
    app = web.Application()
    app.on_startup.append(initialize)
    app.on_cleanup.append(destroy)
    app.add_routes([web.view('/control', ControlView)])
    app.add_routes([web.get('/info', info)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 5070)
    await site.start()

    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(create_api())