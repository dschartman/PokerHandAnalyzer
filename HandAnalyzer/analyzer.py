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

    best_paired_hand, paired_cards = _find_best_paired_cards(cards)
    best_straight_hand, straight_cards = _find_best_straight_cards(cards)
    best_flush_hand, flush_cards = _find_best_flush_cards(cards)

    if best_flush_hand is not None and best_straight_hand is not None:
        if flush_cards == straight_cards:
            if straight_cards[0].rank_value == 14:
                return score_top_five_cards(__ROYAL_FLUSH, straight_cards)
            else:
                return score_top_five_cards(__STRAIGHT_FLUSH, straight_cards)

        if straight_cards[0].rank_value == 14 and flush_cards == straight_cards:
            return score_top_five_cards(__ROYAL_FLUSH, straight_cards)
    
    if best_paired_hand == __QUADS:
        return score_top_five_cards(__QUADS, paired_cards)

    if best_paired_hand == __FULL_HOUSE:
        return score_top_five_cards(__FULL_HOUSE, paired_cards)

    if best_flush_hand == __FLUSH:
        return score_top_five_cards(__FLUSH, flush_cards)

    if best_straight_hand == __STRAIGHT:
        return score_top_five_cards(__STRAIGHT, straight_cards)

    if best_paired_hand == __SET:
        return score_top_five_cards(__SET, paired_cards)

    if best_paired_hand == __TWO_PAIR:
        return score_top_five_cards(__TWO_PAIR, paired_cards)

    if best_paired_hand == __PAIR:
        return score_top_five_cards(__PAIR, paired_cards)

    high_card, high_cards = _find_best_high_cards(cards)
    return score_top_five_cards(__HIGH_CARD, high_cards)

def _find_best_high_cards(cards: list):
    return __HIGH_CARD, sorted(cards, key=lambda c: c.rank_value, reverse = True)[:5]

def _find_best_paired_cards(cards: list):
    cards.sort(key=lambda c: c.rank_value, reverse = True)
    rank_value_groups = _group_cards_by_attribute(cards, 'rank_value')
    rank_value_groups.sort(key=lambda tup: tup[1], reverse = True)
    pair_count, set_count, quad_count = _count_pairs(rank_value_groups)

    best_hand = None
    if pair_count == 1:
        best_hand = __PAIR

    if pair_count > 1:
        best_hand = __TWO_PAIR

    if set_count == 1:
        best_hand = __SET

    if pair_count == 1 and set_count == 1:
        best_hand = __FULL_HOUSE

    if set_count > 1:
        best_hand = __FULL_HOUSE

    if quad_count == 1:
        best_hand = __QUADS

    card_count = 0
    top_five_cards = []
    for sp in rank_value_groups:
        for c in sp[2]:
            if card_count < 5:
                top_five_cards.append(c)
                card_count += 1

    return best_hand, top_five_cards

def _find_best_straight_cards(cards: list):
    cards.sort(key=lambda c: c.rank_value, reverse = True)
    next_values = []
    previous_value = 0
    straight = []
    straights = []
    wheel = False
    for c in cards:
        if c.rank_value == previous_value:
            continue

        if c.rank_value in next_values:
            if wheel and c.rank_value == 13:
                wheel = False

        else:
            if len(straight) > 4:
                straights.append(straight)

            straight = []
            wheel = False

        previous_value = c.rank_value
        straight.append(c)
        if c.rank_value == 14:
            wheel = True
            next_values = [13, 5]
        else:
            next_values = [c.rank_value - 1]

    straight = straight[:5]

    if wheel:
       straight.append(straight.pop(0))

    if len(straight) > 4:
        best_hand = __STRAIGHT
    else:
        best_hand = None

    return best_hand, straight

# def _find_best_straight_cards_t(cards: list):
#     buckets = None
#     straight = None
#     previous_rank_value = 0
#     for c in cards:
#         if buckets is None:
#             buckets = []
#             buckets.append([c])

#             continue

#         for bucket in buckets:
#             for bc in bucket:
#                 if bc.rank_value = c.rank_value

#             if c not in bucket:
#                 for bc in bucket:
#                 if bc.rank_value - 1 == c.rank_value:

            


#     return straights

def _find_best_flush_cards(cards: list):
    cards.sort(key=lambda c: c.rank_value, reverse = True)
    cards.sort(key=lambda c: c.suit, reverse = True)
    suit_groups = _group_cards_by_attribute(cards, 'suit')
    suit_groups.sort(key=lambda tup: tup[1], reverse = True)
    flush_counter = suit_groups[0][1]
    flush_cards = []
    if flush_counter > 4:
        best_hand = __FLUSH
        flush_cards = suit_groups[0][2][:5]
    else:
        best_hand = None

    return best_hand, flush_cards

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