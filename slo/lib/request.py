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
      status code of the response
   int 
      response size
   """
   
   response = requests.get(url + '/' + word)
   return response.status_code, len(response.content)