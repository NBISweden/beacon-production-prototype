import logging
import time
import uuid
from beacon.conf.conf import level
from typing import Optional
import os

LOG = logging.getLogger(__name__)
fh = logging.FileHandler("beacon/logs/logs.log")
fh.setLevel(level)
fmt = '%(levelname)s - %(asctime)s - %(message)s'
formatter = logging.Formatter(fmt)
fh.setFormatter(formatter)
LOG.addHandler(fh)

def log_with_args(level, uuid):
    def add_logging(func):
        def wrapper(*args, **kwargs):
            try:
                # Si no hi ha transaction, com a txid indicar algun string que faci entendre que el log no correspon a cap transaction.
                start = time.time()
                logging.basicConfig(format=fmt, level=level)
                LOG.debug(f"{uuid} - {func.__name__}({args},{kwargs}) - initial call")
                result = func(*args, **kwargs)
                finish = time.time()
                LOG.debug(f"{uuid} - {func.__name__}({args},{kwargs}) - {finish-start} - returned {result}")
                if f"{func.__name__}" == 'initialize':
                    LOG.info(f"{uuid} - Initialization done")
                elif f"{func.__name__}" == 'destroy':
                    LOG.info(f"{uuid} - Shutting down")
                return result
            except:
                err = "There was an exception in  "
                err += func.__name__
                LOG.error(f"{uuid} - {err}")
                raise
        return wrapper
    return add_logging
    