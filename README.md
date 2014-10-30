deck_of_cards
=============

A simple model for a standard deck of 52 playing cards.


Deck contains three methods:
    shuffle()
        Rearranges cards with random.randint.
        Probably doesn't have a noticeable skew.
    deal_a_card()
        Returns one card from the deck (removing it, not copying it).
    list()
        Returns a list containing the proper names of each card in the deck.

Card contains no external methods...
    And it may be called independently of Deck to return a proper card
        with a random value.
    It may also be called with the keyword parameter card_index, which takes
        a number from 0 to 51 and uses that to generate a card according to
        a cryptic schema unknown to any but the masters of modulus.

Both the Deck and Card classes can be invoked as strings
    to more legibly view their contents.

Resources used:
    My memory of how to code objects in Python
    Supplementary feature suggestions from Dan Hable
    Testing idea from:
        https://github.com/markableidinger/card_deck/blob/master/test_cards.py

Collaborators:
    deck_of_cards.py
        Me
        Myself
        I

