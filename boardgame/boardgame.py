# -*- coding: utf-8 -*-


"""bootstrap.bootstrap: provides entry point main()."""


__version__ = "0.0.1"


import sys
from random import randint
from .start_cards import STARTING_CARDS

def main():
    print("Executing boardgame version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])

    print("Pull starting card")
    print("STARTING CARDS AVAILABLE: %d" % len(STARTING_CARDS))
    print("YOU DRAW:")
    starting_card = STARTING_CARDS[randint(0, len(STARTING_CARDS) - 1)]
    print(starting_card.name)
    print(starting_card.description)

