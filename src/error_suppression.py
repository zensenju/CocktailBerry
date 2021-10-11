""" Special configs for the Logger """
import logging
from functools import wraps

from config.config_manager import shared


def logerror(func):
    """ Logs every time an error occours """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if shared.supress_error:
            logger = logging.getLogger("debuglog")
            try:
                func(*args, **kwargs)
            except Exception:
                logger.exception("The function %s could not be fully excecuted!", func.__name__)
                print("The function {} could not be fully excecuted!".format(func.__name__))
        else:
            func(*args, **kwargs)

    return wrapper
