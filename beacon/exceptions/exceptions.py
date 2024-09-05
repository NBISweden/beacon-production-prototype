from aiohttp import web
import json
from beacon.logs.logs import LOG
from beacon.request.classes import ErrorClass

def raise_exception(beacon_response, errorCode):
    if errorCode == 400:
        if ErrorClass.error_response == None:
            ErrorClass.error_response = beacon_response
            ErrorClass.error_code = errorCode
        raise web.HTTPBadRequest(text=json.dumps(beacon_response), content_type='application/json')
