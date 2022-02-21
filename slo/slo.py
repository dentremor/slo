import click
from lib.enumerate import enumerate
from utils.url import check_url

@click.command()
@click.option('-w', '--wordlist', help='A wordlist for directory enumeration')
@click.option('-u', '--url', help='The URL to be enumerated')
def cli(wordlist, url):
   if not check_url(url):
      raise click.BadParameter('URL has invalid syntax or is unreachable')
   
   enumerate(wordlist, url)

if __name__ == '__main__':
   cli()
