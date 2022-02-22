from threading import Thread
from typing import Generator
from lib.wordlist import parse_wordlist
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
   threads = []
   for word in wordlist:
      process = Thread(target = request, args=[word, url])
      process.start()
      threads.append(process)
      
   for process in threads:
      process.join()