from rank_dictionary import rank_dictionary
from itertools import groupby
from operator import itemgetter

def determine_rank(card):
    return rank_dictionary[card]

def analyze_hand(hand):
    cards =[(rank, rank_dictionary[rank], suit) for rank, suit in hand.split()]
    cards.sort(key=itemgetter(1),reverse = True)
    groupedCards = groupby(cards, key=itemgetter(1))

    handRank = 1

    sortedGroups = []
    pairCount = 0
    setCount = 0
    
    for key, group in groupedCards:
        groupLength = len(list(group))
        sortedGroups.append((key, groupLength))
        if groupLength == 2:
            pairCount += 1

        if groupLength == 3:
            setCount += 1
        
        if groupLength == 4:
            handRank = 8

    sortedGroups.sort(key = itemgetter(1), reverse=True)

    if pairCount == 1:
        handRank = 2
    
    if pairCount == 2: 
        handRank = 3 

    if setCount == 1:
        handRank = 4

    if setCount == 1 and pairCount == 1:
        handRank = 7

    cardOutput = ' '.join(str(g[0]) for g in sortedGroups)

    return f'{handRank} {cardOutput}'
