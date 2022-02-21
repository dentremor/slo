from typing import Generator

def parse_wordlist(path: str) -> Generator: 
    """Return a Generator yielding the words in the wordlist

    Parameters
    ----------
    path
        path to wordlist

    Returns
    -------
    Generator 
        sequence of words in the wordlist
    """

    with open(path) as file:
        for line in file: 
            yield line.rstrip()

