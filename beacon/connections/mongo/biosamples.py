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
def get_biosamples(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'biosamples'
    mongo_collection = client.beacon.biosamples
    parameters_as_filters=False
    query_parameters, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    if parameters_as_filters == True and query_parameters != {'$and': []}:# pragma: no cover
        query, parameters_as_filters = apply_request_parameters(self, {}, qparams)
        query_parameters={}
    elif query_parameters != {'$and': []}:
        query=query_parameters
    elif query_parameters == {'$and': []}:# pragma: no cover
        query_parameters = {}
        query={}
    query = apply_filters(self, query, qparams.query.filters, collection, query_parameters)
    schema = DefaultSchemas.BIOSAMPLES
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    idq="id"
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_biosample_with_id(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'biosamples'
    mongo_collection = client.beacon.biosamples
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    schema = DefaultSchemas.BIOSAMPLES
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100# pragma: no cover
    idq="id"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_variants_of_biosample(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    mongo_collection = client.beacon.genomicVariations
    query = {"caseLevelData.biosampleId": entry_id}
    query = apply_filters(self, query, qparams.query.filters, collection, {})
    schema = DefaultSchemas.GENOMICVARIATIONS
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100# pragma: no cover
    idq="caseLevelData.biosampleId"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_analyses_of_biosample(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'biosamples'
    mongo_collection = client.beacon.analyses
    query = {"biosampleId": entry_id}
    query = apply_filters(self, query, qparams.query.filters, collection, {})
    schema = DefaultSchemas.ANALYSES
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100# pragma: no cover
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    idq="biosampleId"
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_runs_of_biosample(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'biosamples'
    mongo_collection = client.beacon.runs
    query = {"individualId": entry_id}
    query = apply_filters(self, query, qparams.query.filters, collection, {})
    schema = DefaultSchemas.RUNS
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100# pragma: no cover
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    idq="biosampleId"
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset