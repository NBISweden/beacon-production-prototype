
import uuid

def generate_txid():
    uniqueid = uuid.uuid1()
    uniqueid = str(uniqueid)[0:8]
    return uniqueid
