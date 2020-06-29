#   Filename:       tests/test_deck.py
#   Description:    Tests class 'Deck'
#
#   Copyright (C) 2020 Shyam Singh
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
import sys
import unittest

from Deck import Deck
import constant

if sys.platform == "win32":
    pwd = os.getenv("PYTHONPATH")
else:
    pwd = os.getenv("PWD")
sys.path.append(pwd)


class TestDeck(unittest.TestCase):
    def test_deck_cards_list(self):
        deck = Deck()
        self.count_deck_cards(deck)

    def test_shuffled_deck_cards_list(self):
        deck = Deck()
        # deck is shuffled and then tested
        deck.get_shuffled_deck()
        self.count_deck_cards(deck)

    # TODO: Add more test cases for cards_count
    # test cards list of Deck are proper or not
    # count different types of cards
    # 4 Wild Cards
    # 4 Wild +4 Cards
    # For each color:
    #   1 Card 0
    #   2 Cards for 1-9
    #   2 Skip Cards
    #   2 Reverse Cards
    #   2 +2 Cards

    # Check in the list do we have all the above count of cards with
    # respective color.
    def count_deck_cards(self, deck):
        # 4 Wild Cards
        wildcard_count = deck.count_card(
            cardtype=constant.WILD_CARD, color=constant.COLOR_WILD
        )  # returns 4
        self.assertEqual(wildcard_count, 4)

        # 4 Wild +4 Cards
        wildcard_plus4_count = deck.count_card(
            cardtype=constant.WILD_PLUS4_CARD, color=constant.COLOR_WILD
        )  # returns 4
        self.assertEqual(wildcard_plus4_count, 4)

        for color in deck.color_list:
            #   1 Card 0
            card0_count = deck.count_card(
                cardtype=constant.CARD0, color=color
            )  # returns 1
            self.assertEqual(card0_count, 1)

            #   2 Cards for 1-9
            cardtype_list = [
                constant.CARD1,
                constant.CARD2,
                constant.CARD3,
                constant.CARD4,
                constant.CARD5,
                constant.CARD6,
                constant.CARD7,
                constant.CARD8,
                constant.CARD9,
            ]
            for cardtype in cardtype_list:
                card_count = deck.count_card(
                    cardtype=cardtype, color=color
                )  # returns 2
                self.assertEqual(card_count, 2)

            #   2 Skip Cards
            skip_card_count = deck.count_card(
                cardtype=constant.SKIP_CARD, color=color
            )  # returns 2
            self.assertEqual(skip_card_count, 2)

            #   2 Reverse Cards
            reverse_card_count = deck.count_card(
                cardtype=constant.REVERSE_CARD, color=color
            )  # returns 2
            self.assertEqual(reverse_card_count, 2)

            #   2 +2 Cards
            plus2_card_count = deck.count_card(
                cardtype=constant.PLUS2_CARD, color=color
            )  # returns 2
            self.assertEqual(plus2_card_count, 2)


if __name__ == "__main__":
    unittest.main()
