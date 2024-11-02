from beacon.request.parameters import RequestParams, AlphanumericFilter, Operator
from typing import List, Dict
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from aiohttp import web
from beacon.connections.mongo.filters import apply_alphanumeric_filter

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
    elif len(value) == 2:# pragma: no cover
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
    elif len(value) == 2:# pragma: no cover
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
def apply_request_parameters(self, query: Dict[str, List[dict]], qparams: RequestParams, dataset: str):
    collection = 'g_variants'
    if len(qparams.query.request_parameters) > 0 and "$and" not in query:
        query["$and"] = []
    if isinstance(qparams.query.request_parameters, list):# pragma: no cover
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
                        subquery["$and"].append(apply_alphanumeric_filter({}, filter, collection, dataset))
                elif k == "end":
                    if isinstance(v, str):
                        v = v.split(',')
                    filters = generate_position_filter_end(self, k, v)
                    for filter in filters:
                        subquery["$and"].append(apply_alphanumeric_filter({}, filter, collection, dataset))
                elif k == "datasets":
                    pass
                elif k == "variantMinLength":
                    try:
                        subquery["$and"].append(apply_alphanumeric_filter({}, AlphanumericFilter(
                            id=VARIANTS_PROPERTY_MAP[k],
                            value='min'+v
                        ), collection, dataset))
                    except KeyError:
                        raise web.HTTPNotFound
                elif k == "variantMaxLength":
                    try:
                        subquery["$and"].append(apply_alphanumeric_filter({}, AlphanumericFilter(
                            id=VARIANTS_PROPERTY_MAP[k],
                            value='max'+v
                        ), collection, dataset))
                    except KeyError:
                        raise web.HTTPNotFound    
                elif k == "mateName" or k == 'referenceName':
                    try:
                        subqueryor["$or"].append(apply_alphanumeric_filter({}, AlphanumericFilter(
                            id=VARIANTS_PROPERTY_MAP[k],
                            value='max'+v
                        ), collection, dataset))
                    except KeyError:
                        raise web.HTTPNotFound    
                elif k != 'filters':
                    try:
                        subquery["$and"].append(apply_alphanumeric_filter({}, AlphanumericFilter(
                            id=VARIANTS_PROPERTY_MAP[k],
                            value=v
                        ), collection, dataset))
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
                    query["$and"].append(apply_alphanumeric_filter(self, {}, filter, collection, dataset))
            elif k == "end":
                if isinstance(v, str):
                    v = v.split(',')
                filters = generate_position_filter_end(self, k, v)
                for filter in filters:
                    query["$and"].append(apply_alphanumeric_filter(self, {}, filter, collection, dataset))
            elif k == "datasets":
                pass
            elif k == "variantMinLength":
                try:
                    query["$and"].append(apply_alphanumeric_filter(self, {}, AlphanumericFilter(
                        id=VARIANTS_PROPERTY_MAP[k],
                        value='min'+v
                    ), collection, dataset))
                except KeyError:# pragma: no cover
                    raise web.HTTPNotFound
            elif k == "variantMaxLength":
                try:
                    query["$and"].append(apply_alphanumeric_filter(self, {}, AlphanumericFilter(
                        id=VARIANTS_PROPERTY_MAP[k],
                        value='max'+v
                    ), collection, dataset))
                except KeyError:# pragma: no cover
                    raise web.HTTPNotFound    
            elif k == "mateName" or k == 'referenceName':
                try:
                    subqueryor["$or"].append(apply_alphanumeric_filter(self, {}, AlphanumericFilter(
                        id=VARIANTS_PROPERTY_MAP[k],
                        value=v
                    ), collection, dataset))
                except KeyError:# pragma: no cover
                    raise web.HTTPNotFound
            elif k != 'filters':
                try:
                    query["$and"].append(apply_alphanumeric_filter(self, {}, AlphanumericFilter(
                        id=VARIANTS_PROPERTY_MAP[k],
                        value=v
                    ), collection, dataset))
                except KeyError:# pragma: no cover
                    raise web.HTTPNotFound

            elif k == 'filters':
                v_list=[]
                if ',' in v:
                    v_list =v.split(',')# pragma: no cover
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
        except Exception:# pragma: no cover
            pass
        if subquery["$and"] != []:
            query["$and"].append(subquery)


    return query, False