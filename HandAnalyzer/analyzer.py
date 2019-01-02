from collections import namedtuple

def DetermineBestFiveCardHand(string_cards: list):
    result = []
    high_card = 1

    Card = namedtuple('Card', ['rank', 'rank_value', 'suit'])

    cards = []
    for sc in string_cards:
        break_out = list(sc)
        cards.append(Card(break_out[0], __GetRankValue(break_out[0]), break_out[1]))

    cards.sort(key=lambda tup: tup[1], reverse = True)

    result.append(high_card)
    for c in cards:
        result.append(c.rank_value) 

    return result

def __GetRankValue(rank):
    if rank == 'T':
        return 10
    
    if rank == 'J':
        return 11

    if rank == 'Q':
        return 12

    if rank == 'K':
        return 13
    
    if rank == 'A':
        return 14

    return int(rank)