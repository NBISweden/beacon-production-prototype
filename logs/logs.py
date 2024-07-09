import logging

LOG = logging.getLogger(__name__)
fh = logging.FileHandler("logs/logs.log")
fh.setLevel(logging.DEBUG)
fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(fmt)
fh.setFormatter(formatter)
LOG.addHandler(fh)

def log_with_args(level):
    def add_logging(func):
        def wrapper(*args, **kwargs):
            try:
                logging.basicConfig(format='%(asctime)s - %(pathname)s - %(lineno)s - %(message)s', level=level)
                LOG.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                LOG.info(f"{func.__name__} returned: {result}")
                return result
            except:
                err = "There was an exception in  "
                err += func.__name__
                LOG.info(err)
                LOG.exception(err)
                raise
        return wrapper
    return add_logging
    