from collections import namedtuple

Card = namedtuple('Card', ['rank', 'rank_value', 'suit'])
Result = namedtuple('Result', ['hand_rank', 'hand_score', 'best_five'])
__PLACE_MODIFIER = 10

def DetermineBestFiveCardHand(string_cards: list):
    high_card = 1

    cards = []
    for sc in string_cards:
        break_out = list(sc)
        cards.append(Card(break_out[0], __GetRankValue(break_out[0]), break_out[1]))

    cards.sort(key=lambda tup: tup[1], reverse = True)

    string_score = ""
    for c in cards:
        string_score += str(c.rank_value+__PLACE_MODIFIER) 

    score = int(string_score)

    return Result(high_card, score, [f'{c.rank}{c.suit}' for c in cards])

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