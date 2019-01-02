import unittest
from HandAnalyzer.deck import Deck

class DeckTests(unittest.TestCase):
    def test_no_duplicate_cards(self):
        deck = Deck()
        deck.shuffle()

        duplicateDetected = False
        seen = set()
        for i in range(0,52): # Not a good loop
            card = deck.draw_card()
            if card not in seen:
                seen.add(card)
            else:
                duplicateDetected = True
                break

        self.assertEqual(duplicateDetected, False)