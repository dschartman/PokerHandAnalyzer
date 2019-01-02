import unittest
from HandAnalyzer import hand_analyzer

class HandAnalyzerTests(unittest.TestCase):

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
    def test_straight(self):
        subtests = (
            ('2S 3S 4S 5C 6D', '5 6'),
            ('2S 3S 4S 6C 5D', '5 6'),
            ('KS QD JC TD 9C', '5 13'),
            ('AS QD JC TD 9C 8D', '5 12'),
            ('AS 2D 3C 4D 5C', '5 5'), 
            ('AS KC QC JD TC', '5 14'))

        self.__run_subtests(subtests)

    # 6. flush
    def test_flush(self):
        subtests = (
            ('2S 7S 8S TS QS', '6 12 10 8 7 2'),
            ('AS 7S 8S TS QS', '6 14 12 10 8 7'))

        self.__run_subtests(subtests)

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
    def test_straight_flush(self):
        subtests = (
            ('2S 3S 4S 5S 6S', '9 6'),
            ('2S 3S 4S 6S 5S', '9 6'),
            ('KS QS JS TS 9S', '9 13'),
            ('AC QS JS TS 9S 8S', '9 12'),
            ('AS 2S 3S 4S 5S', '9 5'))

        self.__run_subtests(subtests)

    # 10. royal 
    def test_royal_flush(self):
        subtests = (
            ('AS KS QS JS TS', '10 14'),
            ('AC KC QC JC TC', '10 14'))

        self.__run_subtests(subtests)

    # duplicate cards
    # invalid ranks
    # invalid suits

    # def test_only_best_five_are_returned(self):
    #     subtests = (
    #         ('KH 5H AH 6D TS 7H TH', '2 10 14 13 7 6'),
    #         ('KH 2S AH 6D TS 7H TH', '2 10 14 13 7 6'))

    #     self.__run_subtests(subtests)
    

if __name__ == '__main__':
    unittest.main()