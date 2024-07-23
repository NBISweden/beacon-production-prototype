from beacon.connections.mongo.__init__ import client

def get_datasets():
    collection = client.beacon.datasets
    query = {}
    query = collection.find(query)
    return query

def get_list_of_datasets():
    datasets = get_datasets()
    beacon_datasets = [ r for r in datasets ]
    return beacon_datasets