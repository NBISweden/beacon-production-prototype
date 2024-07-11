import logging
import time
import uuid
from beacon.conf.conf import level

LOG = logging.getLogger(__name__)
fh = logging.FileHandler("beacon/logs/logs.log")
fh.setLevel(level)
fmt = '%(levelname)s - %(asctime)s - %(message)s'
formatter = logging.Formatter(fmt)
fh.setFormatter(formatter)
LOG.addHandler(fh)

def log_with_args(level):
    def add_logging(func):
        def wrapper(*args, **kwargs):
            try:
                uniqueid = uuid.uuid1()
                uniqueid = str(uniqueid)[0:8]
                start = time.time()
                logging.basicConfig(format=fmt, level=level)
                LOG.debug(f"{uniqueid} - {func.__name__}({args},{kwargs}) - initial call")
                result = func(*args, **kwargs)
                finish = time.time()
                LOG.debug(f"{uniqueid} - {func.__name__}({args},{kwargs}) - {finish-start} - returned {result}")
                if f"{func.__name__}" == 'initialize':
                    LOG.info(f"{uniqueid} - Initialization done")
                elif f"{func.__name__}" == 'destroy':
                    LOG.info(f"{uniqueid} - Shutting down")
                return result
            except:
                err = "There was an exception in  "
                err += func.__name__
                LOG.error(f"{uniqueid} - {err}")
                raise
        return wrapper
    return add_logging
    