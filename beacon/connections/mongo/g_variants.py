from beacon.request.parameters import RequestParams
from beacon.response.schemas import DefaultSchemas
import yaml
from beacon.connections.mongo.__init__ import client
from beacon.connections.mongo.utils import get_docs_by_response_type
from beacon.logs.logs import log_with_args, LOG
from beacon.conf.conf import level
from beacon.connections.mongo.filters import apply_filters
from beacon.connections.mongo.request_parameters import apply_request_parameters
from typing import Optional

@log_with_args(level)
def get_variants(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    mongo_collection = client.beacon.genomicVariations
    parameters_as_filters=False
    query_parameters, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    if parameters_as_filters == True and query_parameters != {'$and': []}:
        query, parameters_as_filters = apply_request_parameters(self, {}, qparams)
        query_parameters={}
    elif query_parameters != {'$and': []}:
        query=query_parameters
    elif query_parameters == {'$and': []}:
        query_parameters = {}
        query={}
    query = apply_filters(self, query, qparams.query.filters, collection,query_parameters)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    schema = DefaultSchemas.GENOMICVARIATIONS
    idq="caseLevelData.biosampleId"
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)

    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_variant_with_id(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    mongo_collection = client.beacon.genomicVariations
    query = {"$and": [{"variantInternalId": entry_id}]}
    query_parameters, parameters_as_filters = apply_request_parameters(self, query, qparams)
    if parameters_as_filters == True:
        query, parameters_as_filters = apply_request_parameters(self, {}, qparams)
        query_parameters={}
    else:
        query=query_parameters
    query = apply_filters(self, query, qparams.query.filters, collection, {})
    LOG.debug(query)
    schema = DefaultSchemas.GENOMICVARIATIONS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    idq="caseLevelData.biosampleId"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_biosamples_of_variant(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    mongo_collection = client.beacon.biosamples
    query = {"$and": [{"variantInternalId": entry_id}]}
    query_parameters, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    if parameters_as_filters == True:
        query, parameters_as_filters = apply_request_parameters(self, {}, qparams)
        query_parameters={}
    else:
        query=query_parameters
    query = apply_filters(self, query, qparams.query.filters, collection,query_parameters)
    biosample_ids = client.beacon.genomicVariations \
        .find_one(query, {"caseLevelData.biosampleId": 1, "_id": 0})
    biosample_id=biosample_ids["caseLevelData"]
    try:
        finalid=biosample_id[0]["biosampleId"]
    except Exception:
        finalid=biosample_id["biosampleId"]
    query = {"id": finalid}
    query = apply_filters(self, query, qparams.query.filters, collection, {})
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

@log_with_args(level)
def get_runs_of_variant(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    mongo_collection = client.beacon.runs
    query = {"$and": [{"variantInternalId": entry_id}]}
    query_parameters, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    if parameters_as_filters == True:
        query, parameters_as_filters = apply_request_parameters(self, {}, qparams)
        query_parameters={}
    else:
        query=query_parameters
    query = apply_filters(self, query, qparams.query.filters, collection,query_parameters)
    biosample_ids = client.beacon.genomicVariations \
        .find_one(query, {"caseLevelData.biosampleId": 1, "_id": 0})
    biosample_id=biosample_ids["caseLevelData"]
    try:
        finalid=biosample_id[0]["biosampleId"]
    except Exception:
        finalid=biosample_id["biosampleId"]
    query = {"biosampleId": finalid}
    query = apply_filters(self, query, qparams.query.filters, collection, {})
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
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_analyses_of_variant(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    mongo_collection = client.beacon.analyses
    query = {"$and": [{"variantInternalId": entry_id}]}
    query_parameters, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    if parameters_as_filters == True:
        query, parameters_as_filters = apply_request_parameters(self, {}, qparams)
        query_parameters={}
    else:
        query=query_parameters
    query = apply_filters(self, query, qparams.query.filters, collection,query_parameters)
    biosample_ids = client.beacon.genomicVariations \
        .find_one(query, {"caseLevelData.biosampleId": 1, "_id": 0})
    biosample_id=biosample_ids["caseLevelData"]
    try:
        finalid=biosample_id[0]["biosampleId"]
    except Exception:
        finalid=biosample_id["biosampleId"]
    query = {"biosampleId": finalid}
    query = apply_filters(self, query, qparams.query.filters, collection, {})
    schema = DefaultSchemas.ANALYSES
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
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_individuals_of_variant(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    mongo_collection = client.beacon.individuals
    query = {"$and": [{"variantInternalId": entry_id}]}
    query_parameters, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    if parameters_as_filters == True:
        query, parameters_as_filters = apply_request_parameters(self, {}, qparams)
        query_parameters={}
    else:
        query=query_parameters
    query = apply_filters(self, query, qparams.query.filters, collection,query_parameters)
    biosample_ids = client.beacon.genomicVariations \
        .find_one(query, {"caseLevelData.biosampleId": 1, "_id": 0})
    biosample_id=biosample_ids["caseLevelData"]
    try:
        finalid=biosample_id[0]["biosampleId"]
    except Exception:
        finalid=biosample_id["biosampleId"]
    query = {"id": finalid}
    individual_id = client.beacon.biosamples \
        .find_one(query, {"individualId": 1, "_id": 0})
    finalid=individual_id["individualId"]
    query = {"id": finalid}
    query = apply_filters(self, query, qparams.query.filters, collection, {})
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
