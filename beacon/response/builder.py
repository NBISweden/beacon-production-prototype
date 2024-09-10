from aiohttp.web_request import Request
import asyncio
from concurrent.futures import ThreadPoolExecutor
from beacon.response.granularity import build_beacon_boolean_response_by_dataset, build_beacon_count_response, build_beacon_collection_response
from beacon.connections.mongo.g_variants import get_variants
from beacon.connections.mongo.datasets import get_full_datasets
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level

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
        loop = asyncio.get_running_loop()

        if datasets != []:
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
async def collection_builder(self, request: Request, datasets, qparams, entry_type):
    try:
        entry_id = request.match_info.get('id', None)
        records, count, entity_schema = get_full_datasets(self, entry_id)
        response_converted = (
                    [r for r in records] if records else []
                )
        response = build_beacon_collection_response(
                    self, response_converted, count, qparams, entity_schema
                )
        return response
    except Exception:
        raise