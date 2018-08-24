import unittest
import hand_analyzer

class Test_HandAnalyzerTests(unittest.TestCase):
    def test_rank_properly_detected(self):
        subtests = (
            ('A', 14),
            ('K', 13),
            ('Q', 12),
            ('J', 11),
            ('T', 10),
            ('9', 9),
            ('8', 8),
            ('7', 7),
            ('6', 6),
            ('5', 5),
            ('4', 4),
            ('3', 3),
            ('2', 2))

        for card, expected in subtests:
            with self.subTest(card=card):
                actual = hand_analyzer.determine_rank(card)
                
                self.assertEqual(expected, actual)

    # 1. high card
    def test_high_card(self):
        subtests = ('AS', '1 14')

        for hand, expected in subtests:
            with self.subTest(hand=hand):
                actual = hand_analyzer.analyze_hand(hand)
                
                self.assertEqual(expected, actual)
    # 2. pair
    # 3. two pair
    # 4. set
    # 5. straight
    # 6. flush
    # 7. full house
    # 8. quad
    # 9. straight flush
    # 10. royal flush


if __name__ == '__main__':
    unittest.main()