import random


# Some of my assumptions:
# - Decks contain four suits with associated colors
# - Suits contain thirteen title-like designators
# - It doesn't matter if the deck's contents can change in any which way
#       as long as the initial deck contains the correct 52 cards.
# - The random library is sufficient for randomizing things, particularly
#       when used in the way it is used here.
# - The deck should be shuffled upon creation.
# - deck_of_cards.py will be imported to whatever application users desire
#       to use a deck of cards in; the module has no interface but the API.


class Deck:

    def __init__(self):

        self.all_cards = []
        for each_card_index in range(0, 52):
            self.all_cards.append(Card(card_index=each_card_index))
        self.shuffle()

    def shuffle(self):

        new_list = []
        for each_card_index in range(0, 52):
            number_of_cards_remaining = (52 - each_card_index)
            # Unline range(), random.randint() is doubly end-inclusive.
            # We need indices ranging from 0 to 51, inclusive.
            # I chose NOT to roll the -1 in which_card_index_to_take
            # into number_of_cards_remaining's defintion and add this comment
            # to underline these facts.
            which_card_index_to_take = (random.randint(0,
                                        number_of_cards_remaining) - 1)
            new_list.append(self.all_cards.pop(which_card_index_to_take))
        self.all_cards = new_list

    def deal_a_card(self):

        if len(self.all_cards) >= 1:
            return self.all_cards.pop()

    # Makes viewing the state of the deck at a glance easier.
    def __str__(self):

        # Prints the full name of each Card in the Deck.
        string_list = []
        for each_card in self.all_cards:
            string_list.append(each_card.proper_name)
        print_string = "\n".join(string_list)
        return print_string

    def list(self):

        return [each_card.proper_name for each_card in self.all_cards]


class Card:

    def __init__(self, card_index=None):

        # Support for making random Cards without a Deck:
        if card_index is None:
            import random
            card_index = random.randint(0, 51)

        # Separate from value; this is its absolute position relative to
        # the ideal deck, pre-shuffle.
        # It's logically equivalent to a specific pair of suit and value,
        # such as the Ace of Spades or the 3 of Hearts.
        self.card_index = card_index

        suits = {0: "Club",
                 1: "Spade",
                 2: "Heart",
                 3: "Diamond"}
        specials = {1: "Ace",
                    11: "Jack",
                    12: "Queen",
                    13: "King"}

        self.suit = suits[(card_index % 4)]
        if self.suit == "Club" or self.suit == "Spade":
            self.color = "black"
        else:
            self.color = "red"

        # +1 because value is 1 through 13; useful for various card games
        self.value = ((card_index % 13) + 1)
        if self.value in specials:
            self.title = specials[self.value]
        else:
            self.title = str(self.value)
        self.proper_name = str(self.title + " of " + self.suit + "s")

    # Pretty print()ing.
    def __str__(self):

        return self.proper_name
