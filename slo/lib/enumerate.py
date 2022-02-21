import imp
from typing import Generator
from lib.wordlist.read import parse_wordlist
from lib.request import request


def enumerate(path: str, url: str):
   """Enumerates over wordlist and vreates a request for each word
   
   Parameters
   ----------
   path
      path to wordlist
   url
      url which should be enumerated
   """

   wordlist = parse_wordlist(path)
   for word in wordlist:
      statuscode, size = request(word, url)
      print('==> {}/ (size: {}| status: {})'.format(word, size, statuscode))