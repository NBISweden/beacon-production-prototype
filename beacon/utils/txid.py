
import uuid

def generate_txid():
    uniqueid = uuid.uuid4()
    uniqueid = str(uniqueid)[0:8]
    return uniqueid