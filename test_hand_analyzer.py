import unittest
import hand_analyzer

class Test_HandAnalyzerTests(unittest.TestCase):

    def __run_subtests(self, subtests):
            for hand, expected in subtests:
                with self.subTest(hand=hand):
                    actual = hand_analyzer.analyze_hand(hand)
                    
                    self.assertEqual(expected, actual)

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

    def test_high_card(self):
        subtests = (
            ('AS', '1 14'),
            ('KS', '1 13'),
            ('QS', '1 12'),
            ('JS', '1 11'),
            ('TS', '1 10'),
            ('9S', '1 9'),
            ('8S', '1 8'),
            ('7S', '1 7'),
            ('6S', '1 6'),
            ('5S', '1 5'),
            ('4S', '1 4'),
            ('3S', '1 3'),
            ('2S', '1 2'))

        self.__run_subtests(subtests)

    def test_high_card_handles_order(self):
        subtests = (
            ('AS KS', '1 14 13'),
            ('7S KS 9D', '1 13 9 7'),
            ('KS AS', '1 14 13'))

        self.__run_subtests(subtests)

    # 2. pair
    def test_pair(self):
        subtests = (
            ('AS AD', '2 14'),
            ('KS KD', '2 13'),
            ('KS KD 9S', '2 13 9'),
            ('9S KD KS', '2 13 9'))

        self.__run_subtests(subtests)

    # 3. two pair
    def test_two_pair(self):
        subtests = (
            ('AS AD KS KD', '3 14 13'),
            ('KS KD AS AD', '3 14 13'),
            ('KS KD 9S 9D', '3 13 9'),
            ('9S KD KS 8D 8C', '3 13 8 9'))

        self.__run_subtests(subtests)

    # 4. set
    def test_set(self):
        subtests = (
            ('AS AD AC', '4 14'),
            ('KS KD KC', '4 13'),
            ('9S KS KD KC', '4 13 9'))

        self.__run_subtests(subtests)

    # 5. straight
    # 5. wheel straight


    # 6. flush
    # 7. full house
    def test_full_house(self):
        subtests = (
            ('AS AD AC KS KD', '7 14 13'),
            ('KS KD KC AS AD', '7 13 14'),
            ('2S 2D 2C AS AD', '7 2 14'))

        self.__run_subtests(subtests)

    # 8. quad
    def test_quads(self):
        subtests = (
            ('AS AD AC AH KD', '8 14 13'),
            ('KS KD KC KH AD', '8 13 14'),
            ('2S 2D 2C 2H AD', '8 2 14'))

        self.__run_subtests(subtests)

    # 9. straight flush
    # 10. royal flush
    # duplicate cards
    # invalid ranks
    # invalid suits

    

if __name__ == '__main__':
    unittest.main()