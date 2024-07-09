import json
import logging
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
import asyncio
import aiohttp.web as web

@log_with_args(level=logging.DEBUG)
async def hello(request):
    response_obj = {'status': 'pepe'}
    return web.Response(text=json.dumps(response_obj), status=200, content_type='application/json')


async def create_api():
    app = web.Application()
    #app.on_startup.append(initialize)
    app.add_routes([web.get('/', hello)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 5070)
    await site.start()

    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(create_api())