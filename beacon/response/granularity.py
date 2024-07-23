from beacon.response.schemas import DefaultSchemas
from beacon.request.parameters import RequestParams
from beacon.request.parameters import Granularity
from beacon.conf import conf
from typing import Optional


def build_response_summary_by_dataset(exists, num_total_results, data):
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

def build_meta(qparams: RequestParams, entity_schema: Optional[DefaultSchemas], returned_granularity: Granularity):
    """"Builds the `meta` part of the response

    We assume that receivedRequest is the evaluated request (qparams) sent by the user.
    """
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

def build_response_by_dataset(data, dict_counts, qparams):
    """"Fills the `response` part with the correct format in `results`"""
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
            #LOG.debug(list_of_responses)
            

    #LOG.debug(list_of_responses)
    return list_of_responses

def build_beacon_boolean_response_by_dataset(data,
                                    dict_counts,
                                    num_total_results,
                                    qparams: RequestParams,
                                    entity_schema: DefaultSchemas):

    beacon_response = {
        'meta': build_meta(qparams, entity_schema, Granularity.BOOLEAN),
        'responseSummary': build_response_summary_by_dataset(num_total_results > 0, num_total_results, data),
        'response': {
            'resultSets': build_response_by_dataset(data, dict_counts, qparams)
        },
        'beaconHandovers': 'beacon_handovers()',
    }
    return beacon_response