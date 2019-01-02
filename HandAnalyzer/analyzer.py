from collections import namedtuple
from itertools import groupby
from operator import attrgetter

Card = namedtuple('Card', ['rank', 'rank_value', 'suit'])
Result = namedtuple('Result', ['hand_score', 'best_five'])
__PLACE_MODIFIER = 10

def DetermineBestFiveCardHand(string_cards: list):
    cards = __to_sorted_cards(string_cards)

    string_score = "11"
    top_five_cards = []
    card_count = 0
    for c in cards:
        if card_count < 5:
            string_score += str(c.rank_value + __PLACE_MODIFIER)
            string_score += str(__suit_conversion(c.suit))
            top_five_cards.append(f'{c.rank}{c.suit}')
            card_count += 1

    score = int(string_score)

    pair_count = 0

    grouped_cards = []
    rank_value_groups = groupby(cards, key=attrgetter('rank_value'))
    for key, rank_value_group in rank_value_groups:
        group = list(rank_value_group)
        grouped_cards.append((key, len(group), group))

    grouped_cards.sort(key=lambda tup: tup[1], reverse = True)
    for g in grouped_cards:
        if g[1] == 2:
            pair_count += 1

    if pair_count == 1:
        card_count = 0
        string_score = "12"
        top_five_cards = []
        for sp in grouped_cards:
            for c in sp[2]:
                if card_count < 5:
                    string_score += str(c.rank_value + __PLACE_MODIFIER)
                    string_score += __suit_conversion(c.suit)
                    top_five_cards.append(f'{c.rank}{c.suit}')
                    card_count += 1
        
        score = int(string_score)

    if pair_count == 2:
        card_count = 0
        string_score = "13"
        top_five_cards = []
        for sp in grouped_cards:
            for c in sp[2]:
                if card_count < 5:
                    string_score += str(c.rank_value + __PLACE_MODIFIER)
                    string_score += __suit_conversion(c.suit)
                    top_five_cards.append(f'{c.rank}{c.suit}')
                    card_count += 1
        
        score = int(string_score)

    return Result(score, top_five_cards)

def __to_sorted_cards(string_cards: list):
    cards = []
    for sc in string_cards:
        break_out = list(sc)
        cards.append(Card(break_out[0], __GetRankValue(break_out[0]), break_out[1]))

    cards.sort(key=lambda tup: tup[1], reverse = True)

    return cards

def __suit_conversion(suit):
    if suit == 'C':
        return "1"
    
    if suit == 'D':
        return "2"

    if suit == 'H':
        return "3"

    if suit == 'S':
        return "4"

    return 'Potato'

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