import click
from lib.request import request

@click.command()
@click.option('-w', '--wordlist', help='A wordlist for directory enumeration')
@click.option('-u', '--url', help='The URL to be enumerated')
def cli(wordlist, url):
   request("hans", "werner")

if __name__ == '__main__':
   cli()