# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.0.1"


import sys
from .card import Card


def main():
    print("Executing boardgame version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
