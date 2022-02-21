import imp, asyncio
from typing import Generator
from slo.lib.read import parse_wordlist
from lib.request import request


async def enumerate(path: str, url: str):
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
      status_code, size = await request(word, url)
      if status_code != 404:
         print('==> {}/ (size: {}| status: {})'.format(word, size, status_code))