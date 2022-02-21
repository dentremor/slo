import requests

def request(word: str, url: str) -> bool:
   """Checks if a directory exists
   
   Parameters
   ----------
   word
      searched directroy name
   url
      the url under which the directory should be found
      
   Returns
   -------
   bool
      true if directory exists false otherwise
   """
   
   response = requests.get(url + "/" + word)
   if response.status_code == 200:
      return True
   else:
      return False