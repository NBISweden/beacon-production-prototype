import logging
import time
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

def log_with_args(level):
    def add_logging(func):
        def wrapper(self, *args, **kwargs):
            try:
                start = time.time()
                logging.basicConfig(format=fmt, level=level)
                LOG.debug(f"{self._id} - {func.__name__}({args},{kwargs}) - initial call")
                result = func(self, *args, **kwargs)
                finish = time.time()
                LOG.debug(f"{self._id} - {func.__name__}({args},{kwargs}) - {finish-start} - returned {result}")
                if f"{func.__name__}" == 'initialize':
                    LOG.info(f"{self._id} - Initialization done")
                elif f"{func.__name__}" == 'destroy':
                    LOG.info(f"{self._id} - Shutting down")
                return result
            except:
                err = "There was an exception in  "
                err += func.__name__
                LOG.error(f"{self._id} - {err}")
                raise
        return wrapper
    return add_logging
    