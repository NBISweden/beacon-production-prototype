import logging
from typing_extensions import Self
from pydantic import BaseModel
from strenum import StrEnum
from typing import List, Optional, Union
from beacon.conf.conf import api_version, default_beacon_granularity
from humps.main import camelize
from aiohttp.web_request import Request
from aiohttp import web
import html

class CamelModel(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class IncludeResultsetResponses(StrEnum):
    ALL = "ALL",
    HIT = "HIT",
    MISS = "MISS",
    NONE = "NONE"


class Similarity(StrEnum):
    EXACT = "exact",
    HIGH = "high",
    MEDIUM = "medium",
    LOW = "low"


class Operator(StrEnum):
    EQUAL = "=",
    LESS = "<",
    GREATER = ">",
    NOT = "!",
    LESS_EQUAL = "<=",
    GREATER_EQUAL = ">="

class Granularity(StrEnum):
    BOOLEAN = "boolean",
    COUNT = "count",
    RECORD = "record"

class OntologyFilter(CamelModel):
    id: str
    scope: Optional[str] = None
    include_descendant_terms: bool = False
    similarity: Similarity = Similarity.EXACT


class AlphanumericFilter(CamelModel):
    id: str
    value: Union[str, List[int]]
    scope: Optional[str] = None
    operator: Operator = Operator.EQUAL


class CustomFilter(CamelModel):
    id: str
    scope: Optional[str] = None


class Pagination(CamelModel):
    skip: int = 0
    limit: int = 10


class RequestMeta(CamelModel):
    requested_schemas: List[str] = []
    api_version: str = api_version


class RequestQuery(CamelModel):
    filters: List[dict] = []
    include_resultset_responses: IncludeResultsetResponses = IncludeResultsetResponses.HIT
    pagination: Pagination = Pagination()
    request_parameters: Union[list,dict] = {}
    test_mode: bool = False
    requested_granularity: Granularity = Granularity(default_beacon_granularity)
    scope: str = None

class SequenceQuery(BaseModel):
    referenceName: str
    start: int
    alternateBases:str
    referenceBases: str

class RangeQuery(BaseModel):
    referenceName: str
    start: int
    end: int
    variantType: Optional[str]
    alternateBases: Optional[str]
    aminoacidChange: Optional[str]
    variantMinLength: Optional[int]
    variantMaxLength: Optional[int]

class GeneIdQuery(BaseModel):
    geneId: str
    variantType: Optional[str]
    alternateBases: Optional[str]
    aminoacidChange: Optional[str]
    variantMinLength: Optional[int]
    variantMaxLength: Optional[int]

class BracketQuery(BaseModel):
    referenceName: str
    start: str
    end: str
    variantType: Optional[str]

class GenomicAlleleQuery(BaseModel):
    genomicAlleleShortForm: str

class AminoacidChangeQuery(BaseModel):
    aminoacidChange: str

class RequestParams(CamelModel):
    meta: RequestMeta = RequestMeta()
    query: RequestQuery = RequestQuery()

    def from_request(self, request: Request) -> Self:
        request_params={}
        if request.method != "POST" or not request.has_body or not request.can_read_body:            
            for k, v in request.query.items():
                if k == "requestedSchema":
                    self.meta.requested_schemas = [html.escape(v)]
                elif k == "skip":
                    self.query.pagination.skip = int(html.escape(v))
                elif k == "limit":
                    self.query.pagination.limit = int(html.escape(v))
                elif k == "includeResultsetResponses":
                    self.query.include_resultset_responses = IncludeResultsetResponses(html.escape(v))
                elif k == 'filters':
                    self.query.request_parameters[k] = html.escape(v)
                elif k in ["start", "end", "assemblyId", "referenceName", "referenceBases", "alternateBases", "variantType","variantMinLength","variantMaxLength","geneId","genomicAlleleShortForm","aminoacidChange","clinicalRelevance", "mateName"]:
                    request_params[k]=v
                    self.query.request_parameters[k] = html.escape(v)
                else:
                    raise web.HTTPBadRequest(text='request parameter introduced is not allowed')
        if request_params != {}:
            try:
                RangeQuery(**request_params)
                return self
            except Exception:
                pass
            try:
                SequenceQuery(**request_params)
                return self
            except Exception:
                pass
            try:
                BracketQuery(**request_params)
                return self
            except Exception:
                pass
            try:
                GeneIdQuery(**request_params)
                return self
            except Exception:
                pass
            try:
                AminoacidChangeQuery(**request_params)
                return self
            except Exception:
                pass
            try:
                GenomicAlleleQuery(**request_params)
                return self
            except Exception:
                pass
            raise web.HTTPBadRequest(text='set of parameters not allowed')
        return self

    def summary(self):
        list_of_filters=[]
        for item in self.query.filters:
            for k,v in item.items():
                if v not in list_of_filters:
                    list_of_filters.append(html.escape(v))
        return {
            "apiVersion": self.meta.api_version,
            "requestedSchemas": self.meta.requested_schemas,
            "filters": list_of_filters,
            "requestParameters": self.query.request_parameters,
            "includeResultsetResponses": self.query.include_resultset_responses,
            "pagination": self.query.pagination.dict(),
            "requestedGranularity": self.query.requested_granularity,
            "testMode": self.query.test_mode
        }
