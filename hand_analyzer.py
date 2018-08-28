from card import Card
from collections import Counter

def determine_rank(card):
    return Card(card, 'S').rankValue

def analyze_hand(hand):
    cards = sorted(
        [Card(rank, suit) for rank, suit in hand.split()],
        key = lambda card: card.rankValue,
        reverse=True)

    handRank = 1

    pairCount = 0
    lastRank = 0
    for card in cards:
        if card.rankValue == lastRank:
            pairCount += 1
            handRank = 2

        lastRank = card.rankValue

    output = ' '.join(str(card.rankValue) for card in cards)

    return f'{handRank} {output}'
