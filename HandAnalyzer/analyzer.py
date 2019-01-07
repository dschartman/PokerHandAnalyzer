from collections import namedtuple
from itertools import groupby
from operator import attrgetter
from .exceptions import DuplicateCardException
from .exceptions import InvalidCardException
from .card import Card
from .score import score_top_five_cards

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

def score_best_hand(string_cards: list):
    cards = _to_cards(string_cards)

    cards.sort(key=lambda c: c.rank_value, reverse = True)
    rank_value_groups = _group_cards_by_attribute(cards, 'rank_value')
    rank_value_groups.sort(key=lambda tup: tup[1], reverse = True)
    pair_count, set_count, quad_count = _count_pairs(rank_value_groups)

    straight_cards = _find_straight(cards)
    straight = True if len(straight_cards) > 4 else False

    cards.sort(key=lambda c: c.suit, reverse = True)
    suit_groups = _group_cards_by_attribute(cards, 'suit')
    suit_groups.sort(key=lambda tup: tup[1], reverse = True)
    flush_counter = suit_groups[0][1]

    best_hand = _determine_best_hand(pair_count, set_count, straight, flush_counter, quad_count, straight_cards)
    top_five_cards = _get_top_five(best_hand, suit_groups, straight_cards, rank_value_groups)

    return score_top_five_cards(best_hand, top_five_cards)

def _get_top_five(best_hand, suit_groups, straight_cards, rank_value_groups):
    card_count = 0
    top_five_cards = []
    if best_hand == __FLUSH:
        for sp in suit_groups:
            for c in sp[2]:
                if card_count < 5:
                    top_five_cards.append(c)
                    card_count += 1
    elif best_hand == __STRAIGHT or best_hand == __ROYAL_FLUSH:
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
    return top_five_cards

def _determine_best_hand(pair_count, set_count, straight, flush_counter, quad_count, straight_cards):
    string_score = __HIGH_CARD
    if pair_count == 1:
        string_score = __PAIR

    if pair_count > 1:
        string_score = __TWO_PAIR

    if set_count == 1:
        string_score = __SET

    if straight:
        string_score = __STRAIGHT

    if flush_counter > 4:
        string_score = __FLUSH

    if pair_count == 1 and set_count == 1:
        string_score = __FULL_HOUSE

    if set_count > 1:
        string_score = __FULL_HOUSE

    if quad_count == 1:
        string_score = __QUADS

    if straight and flush_counter > 4:
        if straight_cards[0].rank_value == 14:
            string_score = __ROYAL_FLUSH
        else:
            string_score = __STRAIGHT_FLUSH
    return string_score

def _find_straight(cards):
    next_values = []
    previous_value = 0
    straight = []
    wheel = False
    for c in cards:
        if c.rank_value == previous_value:
            continue

        if c.rank_value in next_values:
            if wheel and c.rank_value == 13:
                wheel = False

        else:
            straight = []
            wheel = False

        previous_value = c.rank_value
        straight.append(c)
        if c.rank_value == 14:
            wheel = True
            next_values = [13, 5]
        else:
            next_values = [c.rank_value - 1]

    if wheel:
       straight.append(straight.pop(0))

    return straight

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

def _count_pairs(grouped_cards):
    pair_count = 0
    set_count = 0
    quad_count = 0
    for g in grouped_cards:
        if g[1] == 2:
            pair_count += 1
        if g[1] == 3:
            set_count += 1
        if g[1] == 4:
            quad_count += 1

    return pair_count, set_count, quad_count

def _group_cards_by_attribute(cards, attribute):
    grouped_cards = []
    rank_value_groups = groupby(cards, key=attrgetter(attribute))
    for key, rank_value_group in rank_value_groups:
        group = list(rank_value_group)
        grouped_cards.append((key, len(group), group))

    return grouped_cards

def _to_cards(string_cards: list):
    seen = set()
    cards = []
    for sc in string_cards:
        if sc not in seen:
            seen.add(sc)
            break_out = list(sc)
            if len(break_out) > 2:
                raise InvalidCardException(f'{break_out} is not a valid card!')

            cards.append(Card(break_out[0], break_out[1]))
        else:
            raise DuplicateCardException(f'You can\'t have more than one {sc}!')

    return cards