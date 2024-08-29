from beacon.connections.mongo.__init__ import client
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level

@log_with_args(level)
def get_datasets(self):
    collection = client.beacon.datasets
    query = {}
    query = collection.find(query)
    return query

@log_with_args(level)
def get_list_of_datasets(self):
    datasets = get_datasets(self)
    beacon_datasets = [ r for r in datasets ]
    return beacon_datasets