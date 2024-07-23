from aiohttp.web_request import Request
from pymongo.cursor import Cursor
from beacon.response.schemas import DefaultSchemas
from beacon.request.parameters import RequestParams, Granularity
from aiohttp import web
import yaml
from beacon.connections.mongo.datasets import get_list_of_datasets
import asyncio
from concurrent.futures import ThreadPoolExecutor
from beacon.connections.mongo.__init__ import client
from pymongo.collection import Collection
from beacon.response.granularity import build_beacon_boolean_response_by_dataset
from bson.json_util import dumps
from typing import Optional
from beacon.logs.logs import LOG

def get_variants(entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    mongo_collection = client.beacon.genomicVariations
    include = 'ALL'
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    query={}
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    schema = DefaultSchemas.GENOMICVARIATIONS
    idq="caseLevelData.biosampleId"
    count, dataset_count, docs = get_docs_by_response_type(include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    docs = dumps(docs)
    return schema, count, dataset_count, docs, dataset

def get_documents(collection: Collection, query: dict, skip: int, limit: int) -> Cursor:
    return collection.find(query).skip(skip).limit(limit).max_time_ms(100 * 1000)

def get_count(collection: Collection, query: dict) -> int:
    if not query:
        return collection.estimated_document_count()
    else:
        counts=client.beacon.counts.find({"id": str(query), "collection": str(collection)})
        try:
            counts=list(counts)
            if counts == []:
                match_dict={}
                match_dict['$match']=query
                count_dict={}
                aggregated_query=[]
                count_dict["$count"]='Total'
                aggregated_query.append(match_dict)
                aggregated_query.append(count_dict)
                total=list(collection.aggregate(aggregated_query))
                insert_dict={}
                insert_dict['id']=str(query)
                total_counts=total[0]['Total']
                insert_dict['num_results']=total_counts
                insert_dict['collection']=str(collection)
                insert_total=client.beacon.counts.insert_one(insert_dict)
            else:
                total_counts=counts[0]["num_results"]
        except Exception:
            try:
                total_counts=client.beacon.counts.count_documents(query)
                insert_dict={}
                insert_dict['id']=str(query)
                insert_dict['num_results']=total_counts
                insert_dict['collection']=str(collection)
                insert_total=client.beacon.counts.insert_one(insert_dict)
            except Exception:
                total_counts=15
        return total_counts

def get_docs_by_response_type(include: str, query: dict, datasets_dict: dict, dataset: str, limit: int, skip: int, mongo_collection, idq: str):
    if include == 'NONE':
        count = get_count(mongo_collection, query)
        dataset_count=0
        docs = get_documents(
        mongo_collection,
        query,
        skip*limit,
        limit
        )
    elif include == 'ALL':
        count=0
        query_count=query
        i=1
        query_count["$or"]=[]
        for k, v in datasets_dict.items():
            if k == dataset:
                for id in v:
                    if i < len(v):
                        queryid={}
                        queryid[idq]=id
                        query_count["$or"].append(queryid)
                        i+=1
                    else:
                        queryid={}
                        queryid[idq]=id
                        query_count["$or"].append(queryid)
                        i=1
                if query_count["$or"]!=[]:
                    dataset_count = get_count(mongo_collection, query_count)
                    docs = get_documents(
                        mongo_collection,
                        query_count,
                        skip*limit,
                        limit
                    )
                else:
                    dataset_count=0
    return count, dataset_count, docs

async def builder(request: Request, authorized_datasets):
    # Get params
    json_body = await request.json() if request.method == "POST" and request.has_body and request.can_read_body else {}
    qparams = RequestParams(**json_body).from_request(request)
    include = qparams.query.include_resultset_responses
    skip = qparams.query.pagination.skip
    limit = qparams.query.pagination.limit
    specific_datasets_unauthorized = []
    search_and_authorized_datasets = []
    try:
        specific_datasets = qparams.query.request_parameters['datasets']
    except Exception:
        specific_datasets = []
    # Get response
    if specific_datasets != []:
        for element in authorized_datasets:
            if element in specific_datasets:
                search_and_authorized_datasets.append(element)
        for elemento in specific_datasets:
            if elemento not in search_and_authorized_datasets:
                specific_datasets_unauthorized.append(elemento)
        beacon_datasets = get_list_of_datasets()
        response_datasets = [ r['id'] for r in beacon_datasets if r['id'] in search_and_authorized_datasets]

    else:
        beacon_datasets = get_list_of_datasets()
        LOG.debug(beacon_datasets)
        LOG.debug(type(beacon_datasets))
        specific_datasets = [ r['id'] for r in beacon_datasets if r['id'] not in authorized_datasets['datasets']]
        response_datasets = [ r['id'] for r in beacon_datasets if r['id'] in authorized_datasets['datasets']]
        specific_datasets_unauthorized.append(specific_datasets)


    entry_id = request.match_info.get('id', None)
    if entry_id == None:
        entry_id = request.match_info.get('variantInternalId', None)
    datasets_docs={}
    datasets_count={}
    new_count=0
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        done, pending = await asyncio.wait(fs=[loop.run_in_executor(pool, get_variants, entry_id, qparams, dataset) for dataset in response_datasets],
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
    
    response = build_beacon_boolean_response_by_dataset(datasets_docs, datasets_count, count, qparams, entity_schema)
    
            
    return response