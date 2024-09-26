from beacon.request.parameters import RequestParams
from beacon.response.schemas import DefaultSchemas
from beacon.connections.mongo.__init__ import client
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level
from beacon.connections.mongo.filters import apply_filters
from typing import Optional
from beacon.connections.mongo.utils import get_count, get_documents

@log_with_args(level)
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
    return docs, count, schema