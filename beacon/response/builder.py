from aiohttp.web_request import Request
from beacon.response.catalog import build_beacon_boolean_response_by_dataset, build_beacon_count_response, build_beacon_collection_response, build_beacon_info_response, build_map, build_configuration, build_entry_types, build_beacon_service_info_response, build_filtering_terms_response, build_beacon_boolean_response
from beacon.connections.mongo.filtering_terms import get_filtering_terms
from beacon.connections.mongo.datasets import get_full_datasets
from beacon.connections.mongo.cohorts import get_cohorts
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from beacon.utils.requests import get_qparams
from beacon.connections.mongo.executor import execute_function
from beacon.request.classes import Granularity

@log_with_args(level)
async def builder(self, request: Request, datasets, qparams, entry_type):
    granularity = qparams.query.requested_granularity
    try:
        entry_id = request.match_info.get('id', None)
        if entry_id == None:
            entry_id = request.match_info.get('variantInternalId', None)

        datasets_docs, datasets_count, count, entity_schema, include = await execute_function(self, entry_type, datasets, qparams, entry_id)

        if include != 'NONE':
            response = build_beacon_boolean_response_by_dataset(self, datasets_docs, datasets_count, count, qparams, entity_schema)
        elif include == 'NONE' and granularity == Granularity.RECORD:
            response = build_beacon_boolean_response(self, datasets_docs["NONE"], count, qparams, entity_schema)
        elif include == 'NONE' and granularity == Granularity.COUNT:
            response = build_beacon_count_response(self, datasets_docs["NONE"], count, qparams, entity_schema)
        return response
    except Exception:
        raise
        

@log_with_args(level)
async def collection_builder(self, request: Request, entry_type):
    try:
        qparams = await get_qparams(self, request)
        entry_id = request.match_info.get('id', None)
        if entry_type == 'datasets':
            function=get_full_datasets
        elif entry_type == 'cohorts':
            function=get_cohorts
        records, count, entity_schema = function(self, entry_id, qparams)
        response_converted = (
                    [r for r in records] if records else []
                )
        response = build_beacon_collection_response(
                    self, response_converted, count, qparams, entity_schema
                )
        return response
    except Exception:
        raise

@log_with_args(level)
async def info_builder(self, request: Request):
    try:
        qparams = await get_qparams(self, request)
        response = build_beacon_info_response(
                    self
                )
        return response
    except Exception:
        raise

@log_with_args(level)
async def configuration_builder(self, request: Request):
    try:
        qparams = await get_qparams(self, request)
        response = build_configuration(
                    self
                )
        return response
    except Exception:
        raise

@log_with_args(level)
async def map_builder(self, request: Request):
    try:
        qparams = await get_qparams(self, request)
        response = build_map(
                    self
                )
        return response
    except Exception:
        raise

@log_with_args(level)
async def entry_types_builder(self, request: Request):
    try:
        qparams = await get_qparams(self, request)
        response = build_entry_types(
                    self
                )
        return response
    except Exception:
        raise

@log_with_args(level)
async def service_info_builder(self, request: Request):
    try:
        qparams = await get_qparams(self, request)
        response = build_beacon_service_info_response(
                    self
                )
        return response
    except Exception:
        raise

@log_with_args(level)
async def filtering_terms_builder(self, request: Request, datasets, qparams, entry_type):
    try:
        qparams = await get_qparams(self, request)
        entry_id = request.match_info.get('id', None)
        entity_schema, count, records = get_filtering_terms(self, entry_id, qparams)
        response = build_filtering_terms_response(
                    self, records, count, qparams, entity_schema
                )
        return response
    except Exception:
        raise