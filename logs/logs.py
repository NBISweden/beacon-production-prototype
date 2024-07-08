import logging

LOG = logging.getLogger(__name__)

'''
    fh = logging.FileHandler("/path/to/test.log")
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    # add handler to logger object
    logger.addHandler(fh)
'''

def log_with_args(level):
    def add_logging(func):
        def wrapper(*args, **kwargs):
            try:
                logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=level)
                LOG.debug(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                LOG.debug(f"{func.__name__} returned: {result}")
                return result
            except:
                err = "There was an exception in  "
                err += function.__name__
                LOG.debug(err)
                raise
        return wrapper
    return add_logging
    