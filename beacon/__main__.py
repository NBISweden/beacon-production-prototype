import json
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from beacon.permissions.__main__ import permission
import asyncio
import aiohttp.web as web

def calculate(nombre):
    try:
        status = nombre/2
    except Exception:
        raise
    return status

@log_with_args(level=level)
async def initialize(app):
    pass

@log_with_args(level=level)
async def destroy(app):
    pass

@log_with_args(level=level)
async def control(request):
    try:
        permissions_dict = await permission(request)
    except Exception:
        user = 'public'
        visa_datasets = []
    status = calculate(4)
    response_obj = {'status': int(status)}
    return web.Response(text=json.dumps(response_obj), status=200, content_type='application/json')

async def create_api():
    app = web.Application()
    app.on_startup.append(initialize)
    app.on_cleanup.append(destroy)
    app.add_routes([web.get('/control', control)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 5070)
    await site.start()

    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(create_api())