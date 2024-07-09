import logging
import time

LOG = logging.getLogger(__name__)
fh = logging.FileHandler("beacon/logs/logs.log")
fh.setLevel(logging.DEBUG)
fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(fmt)
fh.setFormatter(formatter)
LOG.addHandler(fh)

def log_with_args(level):
    def add_logging(func):
        def wrapper(*args, **kwargs):
            try:
                start = time.time()
                logging.basicConfig(format='%(asctime)s - %(pathname)s - %(lineno)s - %(message)s', level=level)
                LOG.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                LOG.info(f"{func.__name__} returned: {result}")
                finish = time.time()
                LOG.info(finish-start)
                return result
            except:
                err = "There was an exception in  "
                err += func.__name__
                LOG.info(err)
                LOG.exception(err)
                raise
        return wrapper
    return add_logging
    