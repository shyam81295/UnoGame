#   Filename:       Card.py
#   Description:    This class will represent UNO Card used in games.
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

from Exceptions import InvalidInstantiationError
import constant


# TODO: make Card class as named tuple.
class Card:
    def __init__(self, *, face="down", color=None, cardtype=None):
        if not (color and cardtype):
            raise InvalidInstantiationError(
                "Color, cardtype of card all are needed."
            )
        if (
            cardtype in (constant.WILD_CARD, constant.WILD_PLUS4_CARD)
            and color != constant.COLOR_WILD
        ):
            raise InvalidInstantiationError("Color & cardtype should match.")
        if (
            cardtype not in (constant.WILD_CARD, constant.WILD_PLUS4_CARD)
            and color == constant.COLOR_WILD
        ):
            raise InvalidInstantiationError("Color & cardtype should match.")

        self.face = face
        self.color = color
        self.cardtype = cardtype
        self.color_sort_priority = {
            constant.COLOR1: 0,
            constant.COLOR2: 1,
            constant.COLOR3: 2,
            constant.COLOR4: 3,
            constant.COLOR_WILD: 4,
        }
        self.card_sort_priority = {
            constant.CARD0: 0,
            constant.CARD1: 1,
            constant.CARD2: 2,
            constant.CARD3: 3,
            constant.CARD4: 4,
            constant.CARD5: 5,
            constant.CARD6: 6,
            constant.CARD7: 7,
            constant.CARD8: 8,
            constant.CARD9: 9,
            constant.SKIP_CARD: 10,
            constant.REVERSE_CARD: 11,
            constant.PLUS2_CARD: 12,
            constant.WILD_CARD: 13,
            constant.WILD_PLUS4_CARD: 14,
        }

    def __str__(self):
        card = [(self.color, self.cardtype)]
        return str(card)

    def __eq__(self, other):
        return self.color == other.color and self.cardtype == other.cardtype
