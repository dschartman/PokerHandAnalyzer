from collections import namedtuple
from HandAnalyzer.exceptions import InvalidCardException

Result = namedtuple('Result', ['hand_score', 'best_five'])
__PLACE_MODIFIER = 10

def score_top_five_cards(string_score, cards: list):
    for c in cards:
        string_score += str(c.rank_value + __PLACE_MODIFIER)
        string_score += __suit_conversion(c.suit)

    score = int(string_score)

    return Result(score, [f'{c.rank}{c.suit}' for c in cards])

def __suit_conversion(suit):
    if suit == 'C':
        return "1"
    
    if suit == 'D':
        return "2"

    if suit == 'H':
        return "3"

    if suit == 'S':
        return "4"

    raise InvalidCardException(f'{suit} is an invalid suit!')