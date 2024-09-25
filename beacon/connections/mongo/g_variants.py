from beacon.request.parameters import RequestParams
from beacon.response.schemas import DefaultSchemas
import yaml
from beacon.connections.mongo.__init__ import client
from bson.json_util import dumps
from typing import Optional
from beacon.connections.mongo.utils import get_docs_by_response_type
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level

@log_with_args(level)
def get_variants(self, entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    mongo_collection = client.beacon.genomicVariations
    include = qparams.query.include_resultset_responses
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    query={}
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    schema = DefaultSchemas.GENOMICVARIATIONS
    idq="caseLevelData.biosampleId"
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset