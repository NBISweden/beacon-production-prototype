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
def get_individuals(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'individuals'
    mongo_collection = client.beacon.individuals
    parameters_as_filters=False
    query_parameters, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    if parameters_as_filters == True and query_parameters != {'$and': []}:
        query, parameters_as_filters = apply_request_parameters(self, {}, qparams)# pragma: no cover
        query_parameters={}# pragma: no cover
    elif query_parameters != {'$and': []}:
        query=query_parameters
    elif query_parameters == {'$and': []}:
        query_parameters = {}
        query={}
    query = apply_filters(self, query, qparams.query.filters, collection, query_parameters)
    schema = DefaultSchemas.INDIVIDUALS
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    idq="id"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_individual_with_id(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'individuals'
    idq="id"
    mongo_collection = client.beacon.individuals
    query, parameters_as_filters = apply_request_parameters(self, {}, qparams)
    query = apply_filters(self, query, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    schema = DefaultSchemas.INDIVIDUALS
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100# pragma: no cover
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args(level)
def get_variants_of_individual(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    query = {"individualId": entry_id}
    mongo_collection = client.beacon.biosamples
    excluding_fields={"_id": 0, "id": 1}
    biosampleId=mongo_collection.find(query, excluding_fields)
    query = {"caseLevelData.biosampleId": biosampleId[0]["id"]}
    mongo_collection = client.beacon.genomicVariations
    query, parameters_as_filters = apply_request_parameters(self, query, qparams)
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
def get_biosamples_of_individual(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'biosamples'
    mongo_collection = client.beacon.biosamples
    query = {"individualId": entry_id}
    query, parameters_as_filters = apply_request_parameters(self, query, qparams)
    query = apply_filters(self, query, qparams.query.filters, collection, {})
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
