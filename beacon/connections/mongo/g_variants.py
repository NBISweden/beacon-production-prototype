from beacon.request.parameters import RequestParams, AlphanumericFilter, Operator
from beacon.response.schemas import DefaultSchemas
import yaml
from beacon.connections.mongo.__init__ import client
from bson.json_util import dumps
from typing import Optional, List, Dict
from beacon.connections.mongo.utils import get_docs_by_response_type
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from aiohttp import web
from beacon.connections.mongo.filters import apply_alphanumeric_filter, apply_filters

VARIANTS_PROPERTY_MAP = {
    "start": "variation.location.interval.start.value",
    "end": "variation.location.interval.end.value",
    "assemblyId": "identifiers.genomicHGVSId",
    "referenceName": "identifiers.genomicHGVSId",
    "referenceBases": "variation.referenceBases",
    "alternateBases": "variation.alternateBases",
    "variantType": "variation.variantType",
    "variantMinLength": "variantInternalId",
    "variantMaxLength": "variantInternalId",
    "geneId": "molecularAttributes.geneIds",
    "genomicAlleleShortForm": "identifiers.genomicHGVSId",
    "aminoacidChange": "molecularAttributes.aminoacidChanges",
    "clinicalRelevance": "caseLevelData.clinicalInterpretations.clinicalRelevance",
    "mateName": "identifiers.genomicHGVSId"
}

@log_with_args(level)
def generate_position_filter_start(self, key: str, value: List[int]) -> List[AlphanumericFilter]:
    filters = []
    if len(value) == 1:
        filters.append(AlphanumericFilter(
            id=VARIANTS_PROPERTY_MAP[key],
            value=value[0],
            operator=Operator.GREATER_EQUAL
        ))
    elif len(value) == 2:
        filters.append(AlphanumericFilter(
            id=VARIANTS_PROPERTY_MAP[key],
            value=value[0],
            operator=Operator.GREATER_EQUAL
        ))
        filters.append(AlphanumericFilter(
            id=VARIANTS_PROPERTY_MAP[key],
            value=value[1],
            operator=Operator.LESS_EQUAL
        ))
    return filters

@log_with_args(level)
def generate_position_filter_end(self, key: str, value: List[int]) -> List[AlphanumericFilter]:
    filters = []
    if len(value) == 1:
        filters.append(AlphanumericFilter(
            id=VARIANTS_PROPERTY_MAP[key],
            value=value[0],
            operator=Operator.LESS_EQUAL
        ))
    elif len(value) == 2:
        filters.append(AlphanumericFilter(
            id=VARIANTS_PROPERTY_MAP[key],
            value=value[0],
            operator=Operator.GREATER_EQUAL
        ))
        filters.append(AlphanumericFilter(
            id=VARIANTS_PROPERTY_MAP[key],
            value=value[1],
            operator=Operator.LESS_EQUAL
        ))
    return filters

@log_with_args(level)
def apply_request_parameters(self, query: Dict[str, List[dict]], qparams: RequestParams):
    collection = 'g_variants'
    if len(qparams.query.request_parameters) > 0 and "$and" not in query:
        query["$and"] = []
    if isinstance(qparams.query.request_parameters, list):
        query={}
        query["$or"]=[]
        for reqparam in qparams.query.request_parameters:
            subquery={}
            subquery["$and"] = []
            subqueryor={}
            subqueryor["$or"] = []
            for k, v in reqparam.items():
                if k == "start":
                    if isinstance(v, str):
                        v = v.split(',')
                    filters = generate_position_filter_start(self, k, v)
                    for filter in filters:
                        subquery["$and"].append(apply_alphanumeric_filter({}, filter, collection))
                elif k == "end":
                    if isinstance(v, str):
                        v = v.split(',')
                    filters = generate_position_filter_end(self, k, v)
                    for filter in filters:
                        subquery["$and"].append(apply_alphanumeric_filter({}, filter, collection))
                elif k == "datasets":
                    pass
                elif k == "variantMinLength":
                    try:
                        subquery["$and"].append(apply_alphanumeric_filter({}, AlphanumericFilter(
                            id=VARIANTS_PROPERTY_MAP[k],
                            value='min'+v
                        ), collection))
                    except KeyError:
                        raise web.HTTPNotFound
                elif k == "variantMaxLength":
                    try:
                        subquery["$and"].append(apply_alphanumeric_filter({}, AlphanumericFilter(
                            id=VARIANTS_PROPERTY_MAP[k],
                            value='max'+v
                        ), collection))
                    except KeyError:
                        raise web.HTTPNotFound    
                elif k == "mateName" or k == 'referenceName':
                    try:
                        subqueryor["$or"].append(apply_alphanumeric_filter({}, AlphanumericFilter(
                            id=VARIANTS_PROPERTY_MAP[k],
                            value='max'+v
                        ), collection))
                    except KeyError:
                        raise web.HTTPNotFound    
                elif k != 'filters':
                    try:
                        subquery["$and"].append(apply_alphanumeric_filter({}, AlphanumericFilter(
                            id=VARIANTS_PROPERTY_MAP[k],
                            value=v
                        ), collection))
                    except KeyError:
                        raise web.HTTPNotFound

                elif k == 'filters':
                    v_list=[]
                    if ',' in v:
                        v_list =v.split(',')
                    else:
                        v_list.append(v)
                    for id in v_list:
                        v_dict={}
                        v_dict['id']=id
                        qparams.query.filters.append(v_dict)        
                    return query, True
        try:
            if subqueryor["$or"] != []:
                subquery["$and"].append(subqueryor)
        except Exception:
            pass
        query["$or"].append(subquery)
    else:
        subquery={}
        subquery["$and"] = []
        subqueryor={}
        subqueryor["$or"] = []
        for k, v in qparams.query.request_parameters.items():
            if k == "start":
                if isinstance(v, str):
                    v = v.split(',')
                filters = generate_position_filter_start(self, k, v)
                for filter in filters:
                    query["$and"].append(apply_alphanumeric_filter(self, {}, filter, collection))
            elif k == "end":
                if isinstance(v, str):
                    v = v.split(',')
                filters = generate_position_filter_end(self, k, v)
                for filter in filters:
                    query["$and"].append(apply_alphanumeric_filter(self, {}, filter, collection))
            elif k == "datasets":
                pass
            elif k == "variantMinLength":
                try:
                    query["$and"].append(apply_alphanumeric_filter(self, {}, AlphanumericFilter(
                        id=VARIANTS_PROPERTY_MAP[k],
                        value='min'+v
                    ), collection))
                except KeyError:
                    raise web.HTTPNotFound
            elif k == "variantMaxLength":
                try:
                    query["$and"].append(apply_alphanumeric_filter(self, {}, AlphanumericFilter(
                        id=VARIANTS_PROPERTY_MAP[k],
                        value='max'+v
                    ), collection))
                except KeyError:
                    raise web.HTTPNotFound    
            elif k == "mateName" or k == 'referenceName':
                try:
                    subqueryor["$or"].append(apply_alphanumeric_filter(self, {}, AlphanumericFilter(
                        id=VARIANTS_PROPERTY_MAP[k],
                        value=v
                    ), collection))
                except KeyError:
                    raise web.HTTPNotFound
            elif k != 'filters':
                try:
                    query["$and"].append(apply_alphanumeric_filter(self, {}, AlphanumericFilter(
                        id=VARIANTS_PROPERTY_MAP[k],
                        value=v
                    ), collection))
                except KeyError:
                    raise web.HTTPNotFound

            elif k == 'filters':
                v_list=[]
                if ',' in v:
                    v_list =v.split(',')
                else:
                    v_list.append(v)
                for id in v_list:
                    v_dict={}
                    v_dict['id']=id
                    qparams.query.filters.append(v_dict)        
                return query, True
        try:
            if subqueryor["$or"] != []:
                subquery["$and"].append(subqueryor)
        except Exception:
            pass
        if subquery["$and"] != []:
            query["$and"].append(subquery)


    return query, False


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
    #with open("beacon/request/datasets.yml", 'r') as datasets_file:
    with open("/beacon/permissions/datasets/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    if include not in ['ALL', 'NONE']:
        include = 'ALL'
    count, dataset_count, docs = get_docs_by_response_type(self, include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset
