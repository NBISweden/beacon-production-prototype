from beacon.connections.mongo.__init__ import client
from beacon.logs.logs import log_with_args_mongo
from beacon.conf.conf import level
from beacon.exceptions.exceptions import raise_exception
from beacon.connections.mongo.utils import get_count, get_documents
from typing import Optional
from beacon.response.schemas import DefaultSchemas
from beacon.request.parameters import RequestParams
from beacon.connections.mongo.filters import apply_filters
from beacon.connections.mongo.utils import get_docs_by_response_type, query_id, get_cross_query
from beacon.connections.mongo.request_parameters import apply_request_parameters
import yaml

@log_with_args_mongo(level)
def get_datasets(self):
    try:
        collection = client.beacon.datasets
        query = {}
        query = collection.find(query)
        return query
    except Exception as e:# pragma: no cover
        err = str(e)
        errcode=500
        raise_exception(err, errcode)

@log_with_args_mongo(level)
def get_full_datasets(self, entry_id: Optional[str], qparams: RequestParams):
    try:
        collection = client.beacon.datasets
        if entry_id == None:
            query = {}
        else:# pragma: no cover
            query = {'id': entry_id}
        count = get_count(self, client.beacon.datasets, query)
        query = collection.find(query)
        entity_schema = DefaultSchemas.DATASETS
        response_converted = (
            [r for r in query] if query else []
        )
        return response_converted, count, entity_schema
    except Exception as e:# pragma: no cover
        err = str(e)
        errcode=500
        raise_exception(err, errcode)

@log_with_args_mongo(level)
def get_list_of_datasets(self):
    try:
        datasets = get_datasets(self)
        beacon_datasets = [ r for r in datasets ]
        return beacon_datasets
    except Exception as e:# pragma: no cover
        err = str(e)
        errcode=500
        raise_exception(err, errcode)

@log_with_args_mongo(level)
def get_dataset_with_id(self, entry_id: Optional[str], qparams: RequestParams):
    limit = qparams.query.pagination.limit
    query_parameters, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    if parameters_as_filters == True:
        query, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    else:
        query={}
    query = query_id(self, query, entry_id)
    schema = DefaultSchemas.DATASETS
    count = get_count(self, client.beacon.datasets, query)
    docs = get_documents(self,
        client.beacon.datasets,
        query,
        qparams.query.pagination.skip,
        qparams.query.pagination.skip*limit
    )
    response_converted = (
                [r for r in docs] if docs else []
            )
    return response_converted, count, schema

@log_with_args_mongo(level)
def get_variants_of_dataset(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'datasets'
    mongo_collection = client.beacon.genomicVariations
    dataset_count=0
    limit = qparams.query.pagination.limit
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    query_count={}
    idq="caseLevelData.biosampleId"
    i=1
    query_count["$or"]=[]
    if dataset == entry_id:
        for k, v in datasets_dict.items():
            if k == entry_id and k == dataset:
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
    else:
        schema = DefaultSchemas.GENOMICVARIATIONS
        return schema, 0, -1, None, dataset
    query = apply_filters(self, query_count, qparams.query.filters, collection, {})
    schema = DefaultSchemas.GENOMICVARIATIONS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args_mongo(level)
def get_biosamples_of_dataset(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'datasets'
    mongo_collection = client.beacon.biosamples
    dataset_count=0
    limit = qparams.query.pagination.limit
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    count = get_count(self, client.beacon.datasets, query)
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    biosample_ids=get_cross_query(self, datasets_dict[entry_id],'biosampleIds','id')
    query = apply_filters(self, biosample_ids, qparams.query.filters, collection, {})
    schema = DefaultSchemas.BIOSAMPLES
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    idq="id"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args_mongo(level)
def get_individuals_of_dataset(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'datasets'
    mongo_collection = client.beacon.individuals
    dataset_count=0
    limit = qparams.query.pagination.limit
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    count = get_count(self, client.beacon.datasets, query)
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    individual_ids=get_cross_query(self, datasets_dict[entry_id],'individualIds','id')
    query = apply_filters(self, individual_ids, qparams.query.filters, collection, {})
    schema = DefaultSchemas.INDIVIDUALS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    idq="id"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args_mongo(level)
def get_runs_of_dataset(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'datasets'
    mongo_collection = client.beacon.runs
    dataset_count=0
    limit = qparams.query.pagination.limit
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    count = get_count(self, client.beacon.datasets, query)
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    biosample_ids=get_cross_query(self, datasets_dict[entry_id],'biosampleIds','biosampleId')
    query = apply_filters(self, biosample_ids, qparams.query.filters, collection, {})
    schema = DefaultSchemas.RUNS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    idq="biosampleId"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    list_of_records = (
            [r for r in docs] if docs else []
        )
    return schema, count, dataset_count, list_of_records, dataset

@log_with_args_mongo(level)
def get_analyses_of_dataset(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'datasets'
    idq="biosampleId"
    mongo_collection = client.beacon.analyses
    dataset_count=0
    limit = qparams.query.pagination.limit
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    count = get_count(self, client.beacon.datasets, query)
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    biosample_ids=get_cross_query(self, datasets_dict[entry_id],'biosampleIds','biosampleId')
    query = apply_filters(self, biosample_ids, qparams.query.filters, collection, {})
    schema = DefaultSchemas.ANALYSES
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset