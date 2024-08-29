from beacon.response.schemas import DefaultSchemas
from beacon.request.parameters import RequestParams
from beacon.request.parameters import Granularity
from beacon.conf import conf
from typing import Optional
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level

@log_with_args(level)
def build_response_summary_by_dataset(self, exists, num_total_results, data):
    count=num_total_results
    if count == 0:
        return {
            'exists': count > 0
        }
    else:
        return {
            'exists': count > 0,
            'numTotalResults': count
        }

@log_with_args(level)
def build_meta(self, qparams: RequestParams, entity_schema: Optional[DefaultSchemas], returned_granularity: Granularity):
    try:
        meta = {
            'beaconId': conf.beacon_id,
            'apiVersion': conf.api_version,
            'returnedGranularity': returned_granularity,
            'receivedRequestSummary': qparams.summary(),
            'returnedSchemas': [entity_schema.value] if entity_schema is not None else []
        }
    except Exception:
        meta = {
            'beaconId': conf.beacon_id,
            'apiVersion': conf.api_version,
            'returnedGranularity': returned_granularity,
            'receivedRequestSummary': qparams,
            'returnedSchemas': [entity_schema.value] if entity_schema is not None else []
        }
    return meta

@log_with_args(level)
def build_response_by_dataset(self, data, dict_counts, qparams):
    list_of_responses=[]
    for k,v in data.items():

        if v:
            response = {
                'id': k, # TODO: Set the name of the dataset/cohort
                'setType': 'dataset', # TODO: Set the type of collection
                'exists': dict_counts[k] > 0,
                'resultsCount': dict_counts[k],
                'results': v,
                # 'info': None,
                'resultsHandover': 'beacon_handovers_by_dataset(k)',  # build_results_handover
            }
            
            list_of_responses.append(response)

    return list_of_responses

@log_with_args(level)
def build_beacon_boolean_response_by_dataset(self, data,
                                    dict_counts,
                                    num_total_results,
                                    qparams: RequestParams,
                                    entity_schema: DefaultSchemas):

    beacon_response = {
        'meta': build_meta(self, qparams, entity_schema, Granularity.BOOLEAN),
        'responseSummary': build_response_summary_by_dataset(self, num_total_results > 0, num_total_results, data),
        'response': {
            'resultSets': build_response_by_dataset(self, data, dict_counts, qparams)
        },
        'beaconHandovers': 'beacon_handovers()',
    }
    return beacon_response