from aiohttp.web_request import Request
import asyncio
from concurrent.futures import ThreadPoolExecutor
from beacon.response.catalog import build_beacon_boolean_response_by_dataset, build_beacon_count_response, build_beacon_collection_response, build_beacon_info_response, build_map, build_configuration, build_entry_types, build_beacon_service_info_response, build_filtering_terms_response, build_beacon_boolean_response
from beacon.connections.mongo.g_variants import get_variants
from beacon.connections.mongo.individuals import get_individuals
from beacon.connections.mongo.analyses import get_analyses
from beacon.connections.mongo.biosamples import get_biosamples
from beacon.connections.mongo.runs import get_runs
from beacon.connections.mongo.filtering_terms import get_filtering_terms
from beacon.connections.mongo.datasets import get_full_datasets
from beacon.connections.mongo.cohorts import get_cohorts
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from beacon.utils.requests import get_qparams

@log_with_args(level)
async def builder(self, request: Request, datasets, qparams, entry_type):
    try:
        include = qparams.query.include_resultset_responses
        limit = qparams.query.pagination.limit
        entry_id = request.match_info.get('id', None)
        if entry_id == None:
            entry_id = request.match_info.get('variantInternalId', None)
        datasets_docs={}
        datasets_count={}
        new_count=0
        if entry_type == 'genomicVariations':
            function=get_variants
        elif entry_type == 'individuals':
            function=get_individuals
        elif entry_type == 'analyses':
            function=get_analyses
        elif entry_type == 'biosamples':
            function=get_biosamples
        elif entry_type == 'runs':
            function=get_runs
        loop = asyncio.get_running_loop()

        if datasets != [] and include != 'NONE':
            with ThreadPoolExecutor() as pool:
                done, pending = await asyncio.wait(fs=[loop.run_in_executor(pool, function, self, entry_id, qparams, dataset) for dataset in datasets],
                return_when=asyncio.ALL_COMPLETED
                )
            for task in done:
                entity_schema, count, dataset_count, records, dataset = task.result()
                if dataset_count != -1:
                    new_count+=dataset_count
                    datasets_docs[dataset]=records
                    datasets_count[dataset]=dataset_count
            
            if include != 'NONE':
                count=new_count
            else:
                if limit == 0 or new_count < limit:
                    pass
                else:
                    count = limit
            
            response = build_beacon_boolean_response_by_dataset(self, datasets_docs, datasets_count, count, qparams, entity_schema)
            return response
        elif include == 'NONE':
            with ThreadPoolExecutor() as pool:
                done, pending = await asyncio.wait(fs=[loop.run_in_executor(pool, get_variants, self, entry_id, qparams, None)],
                return_when=asyncio.ALL_COMPLETED
                )
            for task in done:
                entity_schema, count, dataset_count, records, dataset = task.result()
            
            response = build_beacon_boolean_response(self, records, count, qparams, entity_schema)
        
            return response
        else:
            with ThreadPoolExecutor() as pool:
                done, pending = await asyncio.wait(fs=[loop.run_in_executor(pool, get_variants, self, entry_id, qparams, None)],
                return_when=asyncio.ALL_COMPLETED
                )
            for task in done:
                entity_schema, count, dataset_count, records, dataset = task.result()
            
            response = build_beacon_count_response(self, records, count, qparams, entity_schema)
        
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