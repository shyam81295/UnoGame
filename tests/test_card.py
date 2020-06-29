#   Filename:       tests/test_card.py
#   Description:    Tests class 'Card'
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

from Card import Card
from Exceptions import InvalidInstantiationError
import constant

if sys.platform == "win32":
    pwd = os.getenv("PYTHONPATH")
else:
    pwd = os.getenv("PWD")
sys.path.append(pwd)


class TestCard(unittest.TestCase):
    def setUp(self):
        pass

    def test_card_initialise(self):
        card1 = Card(
            color=constant.COLOR_WILD, cardtype=constant.WILD_PLUS4_CARD
        )
        self.assertEqual(card1.cardtype, constant.WILD_PLUS4_CARD)
        self.assertEqual(card1.color, constant.COLOR_WILD)

        card2 = Card(color=constant.COLOR4, cardtype=constant.SKIP_CARD)
        self.assertEqual(card2.cardtype, constant.SKIP_CARD)
        self.assertEqual(card2.color, constant.COLOR4)

    def test_card_initialise_failed(self):
        self.assertRaises(InvalidInstantiationError, Card)

        self.assertRaises(
            InvalidInstantiationError,
            Card,
            cardtype=constant.WILD_PLUS4_CARD,
            color=constant.COLOR4,
        )

        self.assertRaises(
            InvalidInstantiationError,
            Card,
            cardtype=constant.SKIP_CARD,
            color=constant.COLOR_WILD,
        )


if __name__ == "__main__":
    unittest.main()
