from beacon.validator.classes import JSONSchemaValidator
import requests
import json
from jsonschema import validate, RefResolver, Draft202012Validator
import os
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from aiohttp import web

#Crear json from url. Fer funció i test.
#Escriure dos tests, un que va i un que no va.

@log_with_args(level=level)
def load_json_from_url(url: str):
    try:
        f = requests.get(url)
        if f.status_code == 200:
            total_response = json.loads(f.text)
        else:
            raise web.HTTPNotFound
    except Exception as e:
        return e
    return total_response

@log_with_args(level=level)
def validate_endpoint(path: str, json_from_url):
    try:
        with open(path, 'r') as f:
            info = json.load(f)
        schema_path = 'file:///{0}/'.format(
                os.path.dirname(path).replace("\\", "/"))
        resolver = RefResolver(schema_path, info)
        response = JSONSchemaValidator.validate(json_from_url, info, resolver)
    except Exception as e:
        return e
    return response

@log_with_args(level=level)
def info_check(url: str):
    try:
        total_response = load_json_from_url(url)
        info_path = 'beacon/validator/ref_schemas/framework/json/responses/beaconInfoResponse.json'
        response = validate_endpoint(info_path, total_response)
    except Exception as e:
        return e
    return response