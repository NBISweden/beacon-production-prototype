from beacon.request.parameters import RequestParams
from beacon.response.schemas import DefaultSchemas
from beacon.connections.mongo.__init__ import client
from beacon.logs.logs import log_with_args_mongo
from beacon.conf.conf import level
from beacon.connections.mongo.filters import apply_filters
from typing import Optional
from beacon.connections.mongo.utils import get_count, get_documents
from beacon.connections.mongo.utils import get_docs_by_response_type, query_id, get_cross_query
import yaml

@log_with_args_mongo(level)
def get_cohorts(self, entry_id: Optional[str], qparams: RequestParams):
    collection = 'cohorts'
    limit = qparams.query.pagination.limit
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    schema = DefaultSchemas.COHORTS
    count = get_count(self, client.beacon.cohorts, query)
    docs = get_documents(self,
        client.beacon.cohorts,
        query,
        qparams.query.pagination.skip,
        qparams.query.pagination.skip*limit
    )
    response_converted = (
        [r for r in docs] if docs else []
    )
    return response_converted, count, schema

@log_with_args_mongo(level)
def get_cohort_with_id(self, entry_id: Optional[str], qparams: RequestParams):
    collection = 'cohorts'
    limit = qparams.query.pagination.limit
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    schema = DefaultSchemas.COHORTS
    count = get_count(self, client.beacon.cohorts, query)
    docs = get_documents(self,
        client.beacon.cohorts,
        query,
        qparams.query.pagination.skip,
        qparams.query.pagination.skip*limit
    )
    response_converted = (
        [r for r in docs] if docs else []
    )
    return response_converted, count, schema

@log_with_args_mongo(level)
def get_individuals_of_cohort(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'cohorts'
    mongo_collection = client.beacon.individuals
    dataset_count=0
    limit = qparams.query.pagination.limit
    include = qparams.query.include_resultset_responses
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    count = get_count(self, client.beacon.cohorts, query)
    with open("/beacon/permissions/datasets/cohorts.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    cohort_ids=get_cross_query(self, datasets_dict[entry_id],'individualIds','id')
    query = apply_filters(self, cohort_ids, qparams.query.filters, collection, {})

    schema = DefaultSchemas.INDIVIDUALS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    idq="id"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args_mongo(level)
def get_analyses_of_cohort(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'cohorts'
    mongo_collection = client.beacon.analyses
    dataset_count=0
    limit = qparams.query.pagination.limit
    include = qparams.query.include_resultset_responses
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    count = get_count(self, client.beacon.cohorts, query)
    with open("/beacon/permissions/datasets/cohorts.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    cohort_ids=get_cross_query(self, datasets_dict[entry_id],'biosampleIds','biosampleId')
    query = apply_filters(self, cohort_ids, qparams.query.filters, collection, {})
    schema = DefaultSchemas.ANALYSES
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    idq="biosampleId"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args_mongo(level)
def get_variants_of_cohort(self,entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'cohorts'
    mongo_collection = client.beacon.genomicVariations
    dataset_count=0
    limit = qparams.query.pagination.limit
    include = qparams.query.include_resultset_responses
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    count = get_count(self, client.beacon.cohorts, query)
    with open("/beacon/permissions/datasets/cohorts.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    individual_ids=get_cross_query(self, datasets_dict[entry_id],'individualIds','caseLevelData.biosampleId')
    query = apply_filters(self, individual_ids, qparams.query.filters, collection, {})
    schema = DefaultSchemas.GENOMICVARIATIONS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    idq="caseLevelData.biosampleId"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args_mongo(level)
def get_runs_of_cohort(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'cohorts'
    mongo_collection = client.beacon.runs
    dataset_count=0
    limit = qparams.query.pagination.limit
    include = qparams.query.include_resultset_responses
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    count = get_count(self, client.beacon.cohorts, query)
    with open("/beacon/permissions/datasets/cohorts.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    cohort_ids=get_cross_query(self, datasets_dict[entry_id],'biosampleIds','biosampleId')
    query = apply_filters(self, cohort_ids, qparams.query.filters, collection, {})
    schema = DefaultSchemas.RUNS
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    idq="biosampleId"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

@log_with_args_mongo(level)
def get_biosamples_of_cohort(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'cohorts'
    mongo_collection = client.beacon.biosamples
    dataset_count=0
    limit = qparams.query.pagination.limit
    include = qparams.query.include_resultset_responses
    query = apply_filters(self, {}, qparams.query.filters, collection, {})
    query = query_id(self, query, entry_id)
    count = get_count(self, client.beacon.cohorts, query)
    with open("/beacon/permissions/datasets/cohorts.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    cohort_ids=get_cross_query(self, datasets_dict[entry_id],'biosampleIds','id')
    query = apply_filters(self, cohort_ids, qparams.query.filters, collection, {})
    schema = DefaultSchemas.BIOSAMPLES
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    skip = qparams.query.pagination.skip
    if limit > 100 or limit == 0:
        limit = 100
    idq="id"
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset