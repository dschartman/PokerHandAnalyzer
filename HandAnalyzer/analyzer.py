from collections import namedtuple
from itertools import groupby
from operator import attrgetter

Card = namedtuple('Card', ['rank', 'rank_value', 'suit'])
Result = namedtuple('Result', ['hand_score', 'best_five'])
__PLACE_MODIFIER = 10
__HIGH_CARD = "11"
__PAIR = "12"
__TWO_PAIR = "13"
__SET = "14"
__STRAIGHT = "15"
__FLUSH = "16"
__FULL_HOUSE = "17"
__QUADS = "18"
__STRAIGHT_FLUSH = "19"
__ROYAL_FLUSH = "20"

def DetermineBestFiveCardHand(string_cards: list):
    cards = __to_cards(string_cards)
    cards.sort(key=lambda tup: tup[1], reverse = True)

    rank_value_groups = __group_attribute(cards, 'rank_value')
    rank_value_groups.sort(key=lambda tup: tup[1], reverse = True)
    pair_count, set_count = __count_pairs(rank_value_groups)

    straight_counter = 0
    next_value = []
    straight_cards = []
    for c in cards:
        if c.rank_value in next_value:
            straight_counter += 1
        else:
            straight_counter = 1
            straight_cards = []

        straight_cards.append(c)
        if c.rank_value == 14:
            next_value = [13, 5]
        else:
            next_value = [c.rank_value - 1]

    suit_groups = __group_attribute(cards, 'suit')
    suit_groups.sort(key=lambda tup: tup[1], reverse = True)
    flush_counter = suit_groups[0][1]

    string_score = __HIGH_CARD
    if pair_count == 1:
        string_score = __PAIR

    if pair_count > 1:
        string_score = __TWO_PAIR

    if set_count == 1:
        string_score = __SET

    if straight_counter > 4:
        string_score = __STRAIGHT

    if flush_counter > 4:
        string_score = __FLUSH

    if pair_count == 1 and set_count == 1:
        string_score = __FULL_HOUSE
    
    if set_count > 1:
        string_score = __FULL_HOUSE

    if straight_counter > 4 and flush_counter > 4:
        string_score = __STRAIGHT_FLUSH

    card_count = 0
    top_five_cards = []
    if string_score == __FLUSH:
        for sp in suit_groups:
            for c in sp[2]:
                if card_count < 5:
                    top_five_cards.append(c)
                    card_count += 1
    elif string_score == __STRAIGHT:
        for c in straight_cards:
            if card_count < 5:
                top_five_cards.append(c)
                card_count += 1
    else:
        for sp in rank_value_groups:
            for c in sp[2]:
                if card_count < 5:
                    top_five_cards.append(c)
                    card_count += 1

    for c in top_five_cards:
        string_score += str(c.rank_value + __PLACE_MODIFIER)
        string_score += __suit_conversion(c.suit)

    score = int(string_score)

    return Result(score, [f'{c.rank}{c.suit}' for c in top_five_cards])

def __count_straight(cards):
    straight_counter = 0
    next_value = 0
    for c in cards:
        if c.rank_value == next_value:
            straight_counter += 1
        else:
            straight_counter = 1

        next_value = c.rank_value - 1

    return straight_counter

def __count_pairs(grouped_cards):
    pair_count = 0
    set_count = 0
    for g in grouped_cards:
        if g[1] == 2:
            pair_count += 1
        if g[1] == 3:
            set_count += 1

    return pair_count, set_count

def __group_attribute(cards, attribute):
    grouped_cards = []
    rank_value_groups = groupby(cards, key=attrgetter(attribute))
    for key, rank_value_group in rank_value_groups:
        group = list(rank_value_group)
        grouped_cards.append((key, len(group), group))

    return grouped_cards

def __to_cards(string_cards: list):
    cards = []
    for sc in string_cards:
        break_out = list(sc)
        cards.append(Card(break_out[0], __get_rank_value(break_out[0]), break_out[1]))

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

def __get_rank_value(rank):
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