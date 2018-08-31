import random

class Deck:
    def __init__(self):
        self.deck = []

    def draw_card(self):
        return self.deck.pop(0)

    def blane(self, target):
        return self.deck.remove(target)

    def shuffle(self):
        self.deck = self.__build_new_deck()
        random.shuffle(self.deck)

    def __build_new_deck(self):
        suits = ['H', 'D', 'S', 'C']
        ranks = [str(value) for value in range(2,10)] + 'T J Q K A'.split()
        return [f'{rank}{suit}' for suit in suits for rank in ranks]