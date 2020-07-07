#   Filename:       tests/test_card_collection.py
#   Description:    This class will test class 'CardCollection'
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

import unittest

from Card import Card
from Deck import Deck
from Hand import Hand
import constant


class TestCardCollection(unittest.TestCase):
    def test_count_total_cards(self):
        deck = Deck()
        self.assertEqual(deck.count_total_cards(), constant.DECK_MAX_SIZE)

    def test_top_card(self):
        deck = Deck()
        deck_top_card = deck.get_top_card()
        self.assertEqual(deck_top_card, deck.cards_list[-1])

    def test_pop_card(self):
        deck = Deck()
        deck_top_card = deck.get_top_card()
        popped_card = deck.pop_card()
        self.assertEqual(deck.count_total_cards(), constant.DECK_MAX_SIZE - 1)
        self.assertEqual(deck_top_card, popped_card)

    def test_push_card(self):
        card = Card(color=constant.COLOR2, cardtype=constant.CARD7)
        hand1 = Hand()
        hand1.push_card(card)
        self.assertEqual(hand1.count_total_cards(), 1)
        self.assertEqual(hand1.get_top_card(), card)

    def test_transfer_cards_from(self):
        deck = Deck()
        hand1 = Hand()
        hand2 = Hand()
        hand1.transfer_cards_from(deck, hand1.hand_starting_size)
        self.assertEqual(
            deck.count_total_cards(),
            constant.DECK_MAX_SIZE - constant.HAND_SIZE_CLASSIC,
        )
        hand2.transfer_cards_from(deck, hand1.hand_starting_size)
        self.assertEqual(
            deck.count_total_cards(),
            constant.DECK_MAX_SIZE - 2 * constant.HAND_SIZE_CLASSIC,
        )


if __name__ == "__main__":
    unittest.main()
