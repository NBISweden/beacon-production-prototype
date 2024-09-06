from beacon.connections.mongo.__init__ import client
from beacon.logs.logs import log_with_args_mongo
from beacon.conf.conf import level
from beacon.exceptions.exceptions import raise_exception

@log_with_args_mongo(level)
def get_datasets(self):
    collection = client.beacon.datasets
    query = {}
    query = collection.find(query)
    return query

@log_with_args_mongo(level)
def get_list_of_datasets(self):
    try:
        datasets = get_datasets(self)
        beacon_datasets = [ r for r in datasets ]
        return beacon_datasets
    except Exception as e:
        err = str(e)
        errcode=500
        raise_exception(err, errcode)