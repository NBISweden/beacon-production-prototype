from aiohttp.web_request import Request
from beacon.response.catalog import build_beacon_boolean_response_by_dataset, build_beacon_count_response, build_beacon_collection_response, build_beacon_info_response, build_map, build_configuration, build_entry_types, build_beacon_service_info_response, build_filtering_terms_response, build_beacon_boolean_response
from beacon.connections.mongo.filtering_terms import get_filtering_terms
from beacon.connections.mongo.datasets import get_full_datasets, get_dataset_with_id
from beacon.connections.mongo.cohorts import get_cohorts, get_cohort_with_id
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from beacon.utils.requests import get_qparams
from beacon.connections.mongo.executor import execute_function
from beacon.request.classes import Granularity

@log_with_args(level)
async def builder(self, request: Request, datasets, qparams, entry_type, entry_id):
    granularity = qparams.query.requested_granularity
    try:
        datasets_docs, datasets_count, count, entity_schema, include = await execute_function(self, entry_type, datasets, qparams, entry_id)
        if include != 'NONE':
            response = build_beacon_boolean_response_by_dataset(self, datasets_docs, datasets_count, count, qparams, entity_schema)
        elif include == 'NONE' and granularity == Granularity.RECORD:
            response = build_beacon_boolean_response(self, datasets_docs["NONE"], count, qparams, entity_schema)
        elif include == 'NONE' and granularity == Granularity.COUNT:
            response = build_beacon_count_response(self, datasets_docs["NONE"], count, qparams, entity_schema)
        return response
    except Exception:# pragma: no cover
        raise

@log_with_args(level)
async def collection_builder(self, request: Request, qparams, entry_type, entry_id):
    try:
        if entry_id == None:
            if entry_type == 'datasets':
                function=get_full_datasets
            elif entry_type == 'cohorts':
                function=get_cohorts
        else:
            if entry_type == 'datasets':
                function=get_dataset_with_id
            elif entry_type == 'cohorts':
                function=get_cohort_with_id
        response_converted, count, entity_schema = function(self, entry_id, qparams)
        response = build_beacon_collection_response(
                    self, response_converted, count, qparams, entity_schema
                )
        return response
    except Exception:# pragma: no cover
        raise

@log_with_args(level)
async def info_builder(self, request: Request):
    try:
        response = build_beacon_info_response(
                    self
                )
        return response
    except Exception:# pragma: no cover
        raise

@log_with_args(level)
async def configuration_builder(self, request: Request):
    try:
        response = build_configuration(
                    self
                )
        return response
    except Exception:# pragma: no cover
        raise

@log_with_args(level)
async def map_builder(self, request: Request):
    try:
        response = build_map(
                    self
                )
        return response
    except Exception:# pragma: no cover
        raise

@log_with_args(level)
async def entry_types_builder(self, request: Request):
    try:
        response = build_entry_types(
                    self
                )
        return response
    except Exception:# pragma: no cover
        raise

@log_with_args(level)
async def service_info_builder(self, request: Request):
    try:
        response = build_beacon_service_info_response(
                    self
                )
        return response
    except Exception:# pragma: no cover
        raise

@log_with_args(level)
async def filtering_terms_builder(self, request: Request, qparams):
    try:
        entity_schema, count, records = get_filtering_terms(self, qparams)
        response = build_filtering_terms_response(
                    self, records, count, qparams, entity_schema
                )
        return response
    except Exception:# pragma: no cover
        raise