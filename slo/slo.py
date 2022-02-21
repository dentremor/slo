import click
import time
from lib.enumerate import enumerate
from utils.url import check_url

@click.command()
@click.option('-w', '--wordlist', help='A wordlist for directory enumeration')
@click.option('-u', '--url', help='The URL to be enumerated')
def cli(wordlist, url):
   start = time.perf_counter()

   if not check_url(url):
      raise click.BadParameter('URL has invalid syntax or is unreachable')
   
   enumerate(wordlist, url)

   print(f"Completed Execution in {time.perf_counter() - start} seconds")

if __name__ == '__main__':
   cli()
