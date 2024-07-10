import logging
import time
import uuid
from beacon.conf.conf import level

#Status, timing, funció i missatge
#Cridar id únic a les crides per mostrar-ho als logs
#Tirar queries concurrents

#DEBUG --> tota la informació per saber perquè peta i timings
#INFO --> quan ha arrancat el servidor i quan s'ha tancat

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
                start = time.time()
                logging.basicConfig(format=fmt, level=level)
                LOG.debug(f"{uniqueid} - {func.__name__}({args},{kwargs}) - initial call")
                result = func(*args, **kwargs)
                finish = time.time()
                LOG.debug(f"{uniqueid} - {func.__name__}({args},{kwargs}) - returned {result} in {finish-start}")
                if f"{func.__name__}" == 'initialize':
                    LOG.info(f"{uniqueid} - Initialization done")
                elif f"{func.__name__}" == 'destroy':
                    LOG.info(f"{uniqueid} - Shutting down")
                return result
            except:
                err = "There was an exception in  "
                err += func.__name__
                LOG.error(err)
                raise
        return wrapper
    return add_logging
    