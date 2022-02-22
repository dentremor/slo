import requests
from typing import Tuple

def request(word: str, url: str):
   """Checks if a directory exists
   
   Parameters
   ----------
   word
      searched directroy name
   url
      the url under which the directory should be found
      
   Returns
   -------
   int
      status code of the response
   int 
      response size
   """
   
   response = requests.get(url + '/' + word)
   if response.status_code != 404:
      print('==> {}/ (size: {}| status: {})'.format(word, len(response.content), response.status_code))
   