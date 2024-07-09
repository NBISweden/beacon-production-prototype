import json
import logging
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
import asyncio
import aiohttp.web as web

def calculate(nombre):
    try:
        status = nombre/2
    except Exception:
        raise
    return status

@log_with_args(level=logging.DEBUG)
async def success(request):
    status = calculate(4)
    response_obj = {'status': int(status)}
    return web.Response(text=json.dumps(response_obj), status=200, content_type='application/json')

@log_with_args(level=logging.DEBUG)
async def failure(request):
    status = calculate('nonumber')
    response_obj = {'status': int(status)}
    return web.Response(text=json.dumps(response_obj), status=200, content_type='application/json')


async def create_api():
    app = web.Application()
    #app.on_startup.append(initialize)
    app.add_routes([web.get('/success', success)])
    app.add_routes([web.get('/failure', failure)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 5070)
    await site.start()

    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(create_api())