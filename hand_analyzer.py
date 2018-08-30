from rank_dictionary import rank_dictionary
from itertools import groupby
from operator import itemgetter

def determine_rank(card):
    return rank_dictionary[card]

def analyze_hand(hand: str):
    cards =[(rank, rank_dictionary[rank], suit) for rank, suit in hand.split()]
    cards.sort(key=itemgetter(1), reverse = True)

    pairGroups, counts = __process_pairs(cards)
    straightInfo = __process_straight(cards)

    cards.sort(key=itemgetter(2),reverse = True)
    flush = __process_flush(cards)

    handRank, cardOutput = __process_result(counts, straightInfo, flush, pairGroups)

    return f'{handRank} {cardOutput}'

def __process_result(counts, straightInfo, flush, pairGroups):
    pairCount = counts[0]
    setCount = counts[1]
    quadCount = counts[2]
    straight = straightInfo[0]
    straightHigh = straightInfo[1]

    handRank = 1
    if pairCount == 1:
        handRank = 2

    if pairCount == 2: 
        handRank = 3 

    if setCount == 1:
        handRank = 4

    if straight:
        handRank = 5

    if flush:
        handRank = 6

    if setCount == 1 and pairCount == 1:
        handRank = 7

    if quadCount == 1:
        handRank = 8

    if straight and flush:
        handRank = 9

    if straight and flush and straightHigh == 14:
        handRank = 10

    if straight:
        cardOutput = straightHigh
    else:
        cardOutput = ' '.join(str(g[0]) for g in pairGroups)
        
    return handRank, cardOutput

def __process_flush(cards):
    suitedGroups = [(key, len(list(suitGroup))) for key, suitGroup in groupby(cards, key=itemgetter(2))]

    return max(suitedGroups)[1] == 5

def __process_pairs(cards: list):
    sortedGroups = []
    pairCount = 0
    setCount = 0
    quadCount = 0

    rankValueGroups = groupby(cards, key=itemgetter(1))
    for key, rankValueGroup in rankValueGroups:
        groupLength = len(list(rankValueGroup))
        sortedGroups.append((key, groupLength))
        if groupLength == 2:
            pairCount += 1

        if groupLength == 3:
            setCount += 1

        if groupLength == 4:
            quadCount += 1

    sortedGroups.sort(key = itemgetter(1), reverse=True)

    return sortedGroups, (pairCount, setCount, quadCount)

def __process_straight(cards: list):
    expectedRankValue = cards[0][1]
    straightCounter = 0
    straightHigh = 0
    wheel = False
    for card in cards:
        rankValue = card[1]

        if expectedRankValue == rankValue or (rankValue == 5 and wheel):
            straightCounter += 1

            if straightHigh < rankValue:
                straightHigh = rankValue
            
            if rankValue == 5 and wheel:
                straightHigh = 5

        elif straightCounter < 5:
            straightCounter = 1
            straightHigh = rankValue

        expectedRankValue = rankValue - 1
        if rankValue == 14:
            wheel = True

    return straightCounter == 5, straightHigh

