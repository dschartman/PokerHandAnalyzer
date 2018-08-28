from card import Card
import pandas as pd

hand = 'AS AD 9S'
cards = sorted(
        [Card(rank, suit) for rank, suit in hand.split()],
        key = lambda card: card.rankValue,
        reverse=True)

# exec(open("playground.py").read())