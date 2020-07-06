#   Filename:       Deck.py
#   Description:    This class will represent UNO Deck used in games.
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

from collections import Counter, defaultdict
import random

from CardCollection import CardCollection
from Card import Card
import constant
from Exceptions import InvalidInstantiationError


class Deck(CardCollection):
    def __init__(self):
        super().__init__()
        self.color_list = [
            constant.COLOR1,
            constant.COLOR2,
            constant.COLOR3,
            constant.COLOR4,
        ]
        self.fill_cards()

    # Different types of cards:
    # 4 Wild Cards
    # 4 Wild +4 Cards
    # For each color:
    #   1 Card 0
    #   2 Cards for 1-9
    #   2 Skip Cards
    #   2 Reverse Cards
    #   2 +2 Cards
    def fill_cards(self):
        # 4 Wild Cards
        for num in range(4):
            card = Card(color=constant.COLOR_WILD, cardtype=constant.WILD_CARD)
            self.cards_list.append(card)

        # 4 Wild +4 Cards
        for num in range(4):
            card = Card(
                color=constant.COLOR_WILD, cardtype=constant.WILD_PLUS4_CARD
            )
            self.cards_list.append(card)

        if not self.color_list:
            raise InvalidInstantiationError("Color list cannot be None.")

        for color in self.color_list:
            #   1 Card 0
            card0 = Card(color=color, cardtype=constant.CARD0)
            self.cards_list.append(card0)

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
            for num in range(2):
                for card in cardtype_list:
                    card = Card(color=color, cardtype=card)
                    self.cards_list.append(card)

            #   2 Skip Cards
            for num in range(2):
                card = Card(color=color, cardtype=constant.SKIP_CARD)
                self.cards_list.append(card)

            #   2 Reverse Cards
            for num in range(2):
                card = Card(color=color, cardtype=constant.REVERSE_CARD)
                self.cards_list.append(card)

            #   2 +2 Cards
            for num in range(2):
                card = Card(color=color, cardtype=constant.PLUS2_CARD)
                self.cards_list.append(card)

        for card in self.cards_list:
            self.count_cards[(card.color, card.cardtype)] += 1
