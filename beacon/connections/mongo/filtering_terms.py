from beacon.connections.mongo.__init__ import client
from beacon.connections.mongo.utils import get_count
from typing import Optional
from beacon.response.schemas import DefaultSchemas
from beacon.request.parameters import RequestParams
from beacon.connections.mongo.utils import get_filtering_documents

def get_filtering_terms(self, entry_id: Optional[str], qparams: RequestParams):
    query = {}
    schema = DefaultSchemas.FILTERINGTERMS
    count = get_count(self, client.beacon.filtering_terms, query)
    remove_id={'_id':0}
    docs = get_filtering_documents(
        self,
        client.beacon.filtering_terms,
        query,
        remove_id,
        qparams.query.pagination.skip,
        qparams.query.pagination.limit
    )
    return schema, count, docs