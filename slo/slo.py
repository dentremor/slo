import click
from lib.enumerate import enumerate

@click.command()
@click.option('-w', '--wordlist', help='A wordlist for directory enumeration')
@click.option('-u', '--url', help='The URL to be enumerated')
def cli(wordlist, url):
   enumerate(wordlist, url)

if __name__ == '__main__':
   cli()