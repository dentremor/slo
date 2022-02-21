import requests
from typing import Tuple

def request(word: str, url: str) -> Tuple[int, int]:
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
      status code of the response if it is not 404
   int 
      response size
   """
   
   response = requests.get(url + '/' + word)
   if response.status_code != 404:
      return response.status_code, len(response.content)