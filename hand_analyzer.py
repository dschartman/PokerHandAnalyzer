from card import Card
from itertools import groupby

def determine_rank(card):
    return Card(card, 'S').rankValue

def analyze_hand(hand):
    cards = sorted(
        [Card(rank, suit) for rank, suit in hand.split()],
        key = lambda card: card.rankValue,
        reverse=True)

    handRank = 1

    cardOutput = ''
    pairCount = 0
    groups = groupby(cards, lambda c: c.rankValue)
    # need to sort groups
    
    for key, group in groups:
        if len(list(group)) == 2:
            pairCount += 1
        
        cardOutput += str(key) + ' '

    if pairCount == 1:
        handRank = 2
    
    if pairCount == 2: 
        handRank = 3 

    # output = ' '.join(str(card.rankValue) for card in cards)



    return f'{handRank} {cardOutput}'
