import functools
from .client import Client
from .errors import PremiumOnly

def is_premium_endpoint(func):
    """Only allow to be used if a key was provided"""
    @functools.wraps(func)
    def wrapper_premium(*args, **kwargs):
        if Client.key is None:
            raise PremiumOnly("This endpoint can only be used by premium users.")
        return func(*args, **kwargs)
    return wrapper_premium