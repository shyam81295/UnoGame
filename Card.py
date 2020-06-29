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
