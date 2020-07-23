#   Filename:       CardCollection.py
#   Description:    This class will represent a Collection of UNO cards.
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

from collections.abc import MutableSequence
from collections import Counter, defaultdict
import random

from Card import Card
import constant
from Exceptions import LessCardsError


def rank_card(card):
    return (
        card.color_sort_priority[card.color] * 100
        + card.card_sort_priority[card.cardtype]
    )


class CardCollection(MutableSequence):
    def __init__(self):
        self.cards_list = []
        self.count_cards = defaultdict(int)
        self.color_list = []
        # self.fill_cards()

    def count_total_cards(self):
        return len(self.cards_list)

    def count_card(self, *, color=None, cardtype=None):
        return self.count_cards[(color, cardtype)]

    def get_shuffled(self):
        # Using random.shuffle()
        # Why this works?
        # How this works?
        random.shuffle(self)

    def get_top_card(self):
        # we will peek from last, assuming card_collection as stack.
        if len(self):
            return self.cards_list[-1]
        else:
            raise LessCardsError("Card colelction might be empty!")

    def push_card(self, card):
        # we will push to last, assuming card_collection as stack.
        if type(card) is Card:
            self.cards_list.append(card)
        else:
            raise TypeError("Given object is not a Card.")

    def pop_card(self):
        # we will pop from last, assuming card_collection as stack.
        if len(self):
            return self.cards_list.pop()
        else:
            raise LessCardsError("Card colelction might be empty!")

    def transfer_cards_from(self, card_collection_src, transfer_count):
        # randomly transfer cards
        if len(card_collection_src) >= transfer_count:
            for num in range(transfer_count):
                popped_card = card_collection_src.pop_card()
                self.push_card(popped_card)
        else:
            raise LessCardsError(
                "Source card collection do not have {} cards to transfer".format(
                    transfer_count
                )
            )

    def __str__(self):
        collection = [(card.cardtype, card.color) for card in self.cards_list]
        return str(collection)

    def __len__(self):
        return len(self.cards_list)

    def __getitem__(self, position):
        return self.cards_list[position]

    def __setitem__(self, position, card):
        self.cards_list[position] = card

    def __delitem__(self, position):
        del self.cards_list[position]

    def insert(self, position, card):
        self.cards_list.append(None)
        for idx in reversed(range(position + 1, len(self.cards_list) - 1)):
            self.cards_list[idx + 1] = self.cards_list[idx]
        self.cards_list[position] = card

    def sort(self):
        self.cards_list = sorted(self.cards_list, key=rank_card)
