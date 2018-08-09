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
            ('2', 2),
            ('a', 1))

        for card, expected in subtests:
            with self.subTest(card=card):
                actual = hand_analyzer.AnalyzeRank(card)
                
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()