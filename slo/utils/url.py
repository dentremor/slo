import validators
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def check_url(url: str) -> bool:
    """Check if url is valid and can be reached

    Parameters
    ----------
    url
        url to check

    Returns
    -------
    bool
        true if url valid and server can be reached
    """

    return validators.url(url) and is_reachable(url)

def is_reachable(url: str) -> bool: 
    """Check if url can be reached 

    Parameters
    ----------
    url 
        url to check

    Returns
    -------
    bool 
        true if server responds with statuscode 200 OK
    """
    
    try: 
        response = requests.get(url)
    except Exception as e: 
        return False
    
    if response.status_code == 200:
        return True
    else: 
        return False

