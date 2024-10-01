from beacon.request.parameters import RequestParams
from beacon.response.schemas import DefaultSchemas
import yaml
from beacon.connections.mongo.__init__ import client
from beacon.connections.mongo.utils import get_docs_by_response_type, query_id
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from beacon.connections.mongo.filters import apply_filters
from beacon.connections.mongo.request_parameters import apply_request_parameters
from typing import Optional

@log_with_args(level)
def get_runs(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'runs'
    mongo_collection = client.beacon.runs
    parameters_as_filters=False
    query_parameters, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    if parameters_as_filters == True:
        query, parameters_as_filters = apply_request_parameters(self, {}, qparams)# pragma: no cover
        query_parameters={}# pragma: no cover
    else:
        query={}
    query = apply_filters(self, query, qparams.query.filters, collection, query_parameters)
    schema = DefaultSchemas.RUNS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    idq="biosampleId"
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_run_with_id(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'runs'
    mongo_collection = client.beacon.runs
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    schema = DefaultSchemas.RUNS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100# pragma: no cover
    idq="biosampleId"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_variants_of_run(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'runs'
    mongo_collection = client.beacon.genomicVariations
    query = {"$and": [{"id": entry_id}]}
    query = apply_filters(self, query, qparams.query.filters, collection, {})
    run_ids = client.beacon.runs \
        .find_one(query, {"biosampleId": 1, "_id": 0})
    query = {"caseLevelData.biosampleId": run_ids["biosampleId"]}
    query = apply_filters(self, query, qparams.query.filters, collection, {})
    schema = DefaultSchemas.GENOMICVARIATIONS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100# pragma: no cover
    idq="caseLevelData.biosampleId"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_analyses_of_run(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'runs'
    mongo_collection = client.beacon.analyses
    query = {"runId": entry_id}
    query = apply_filters(self, query, qparams.query.filters, collection, {})
    schema = DefaultSchemas.RUNS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100# pragma: no cover
    idq="biosampleId"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset