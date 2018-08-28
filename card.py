from rank_dictionary import rank_dictionary

class Card:
    def __init__(self, rank, suit):
        self.rankValue = rank_dictionary[rank]
        self.suit = suit