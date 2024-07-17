
from aiohttp.web_request import Request

async def check_request_content_type(self, request: Request):
    if request.headers.get('Content-Type') == 'application/json':
        post_data = await request.json()
    else:
        post_data = await request.post()
    return post_data