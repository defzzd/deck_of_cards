import unittest
import deck_of_cards as d_o_c


class test_Deck(unittest.TestCase):

    def setUp(self):

        # Also tests the constructor.
        self.test_deck = d_o_c.Deck()
        self.secondary_test_deck = d_o_c.Deck()


    def test_shuffle(self):

        self.setUp()

        # Mass random testing is kind of neat.
        # Inspired by/mostly copied from:
        # https://github.com/markableidinger/
        #    card_deck/blob/master/test_cards.py

        # Also tests deal_a_card().
        test_deal = self.secondary_test_deck.deal_a_card()
        number_of_failed_tests = 0
        for each_pass in range(0, 1000):
            self.test_deck.shuffle()
            the_top_card = self.test_deck.all_cards[0]
            if the_top_card == test_deal:
                number_of_failed_tests += 1
        # It's pretty unlikely.
        if number_of_failed_tests > 3:
            raise Exception

    def test_list(self):

        self.setUp()

        if isinstance(self.test_deck.list(), list):
            assert True
        else:
            assert False

        with self.assertRaises(AssertionError):
            self.assertEqual(self.test_deck.list(),
                             self.secondary_test_deck.list())


class test_Card(unittest.TestCase):

    def test_constructor(self):

        d_o_c.Card()
        d_o_c.Card(0)
        d_o_c.Card(-1)
        d_o_c.Card(1)
        # It uses modulus to assign values; this may be
        # used to create mild unpredictability
        # when playing with the API.
        # This does NOT create a random value.
        d_o_c.Card(100000000)
        # Why you'd want those particular card values to be considered
        # True or False is left as an exercise for future creative minds.
        d_o_c.Card(True)
        d_o_c.Card(False)
        d_o_c.Card(card_index=51)

        assert d_o_c.Card(0).color == "black"
        assert d_o_c.Card(1).color == "black"
        assert d_o_c.Card(2).color == "red"
        assert d_o_c.Card(3).color == "red"

        with self.assertRaises(TypeError):
            d_o_c.Card("Testing string for the Card constructor")

        with self.assertRaises(TypeError):
            d_o_c.Card(d_o_c.Card(1))


unittest.main()
