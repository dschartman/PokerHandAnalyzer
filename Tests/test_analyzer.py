import pytest
from HandAnalyzer import analyzer
from HandAnalyzer.score import Result 
from HandAnalyzer.exceptions import DuplicateCardException
from HandAnalyzer.exceptions import InvalidCardException

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '3H'], Result(11133124, ['3H', '2S'])),
    (['TS', '3H'], Result(11204133, ['TS', '3H'])),
    (['TS', 'AH'], Result(11243204, ['AH', 'TS'])),
    (['TS', 'AH', '4D'], Result(11243204142, ['AH', 'TS', '4D'])),
    (['TS', 'AH', '4D', '3D'], Result(11243204142132, ['AH', 'TS', '4D', '3D'])),
    (['TS', 'AH', '4D', '3D', 'QC'], Result(11243221204142132, ['AH', 'QC', 'TS', '4D', '3D'])),
    (['TS', 'AH', '2D', '3D', 'QC'], Result(11243221204132122, ['AH', 'QC', 'TS', '3D', '2D'])),
    (['TS', 'AH', '2D', '3D', 'QC', 'KC'], Result(11243231221204132, ['AH', 'KC', 'QC', 'TS', '3D'])),
])
def test_high_card(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['TS'], 1),
    (['TS', 'AH'], 2),
    (['TS', 'AH', '2D'], 3),
    (['TS', 'AH', '2D', '3D'], 4),
    (['TS', 'AH', '2D', '3D', 'QC'], 5),
    (['TS', 'AH', '2D', '3D', 'QC', 'KC'], 5),
])
def test_five_or_less_cards_returned(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert len(actual.best_five) == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '2H'], Result(12124123, ['2S', '2H'])),
    (['3H', '2S', '2H'], Result(12124123133, ['2S', '2H', '3H'])),
    (['AC', '3H', '2S', '2H'], Result(12124123241133, ['2S', '2H', 'AC', '3H'])),
])
def test_pair(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['3C', '3H', '2S', '2H'], Result(13131133124123, ['3C', '3H', '2S', '2H'])),
    (['3C', '3H', 'AS', 'AH', '8C', '8H'], Result(13244243181183131, ['AS', 'AH', '8C', '8H', '3C'])),
])
def test_two_pair(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '2H', '2C'], Result(14124123121, ['2S', '2H', '2C'])),
    (['2S', '2H', '2C', '5D', '3C'], Result(14124123121152131, ['2S', '2H', '2C', '5D', '3C'])),
])
def test_set(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '3H', '4C', '5S', '6H'], Result(15163154141133124, ['6H', '5S', '4C', '3H', '2S'])),
    (['2S', '3H', '4C', '5S', 'AH'], Result(15154141133124243, ['5S', '4C', '3H', '2S', 'AH'])),
    (['2S', '3H', '4C', '5S', '6H', '7S'], Result(15174163154141133, ['7S', '6H', '5S', '4C', '3H'])),
    (['2S', '3H', '4C', '5S', '6H', '7S', '7C'], Result(15174163154141133, ['7S', '6H', '5S', '4C', '3H'])),
    (['2S', '3H', '4C', '5S', '6H', 'AS'], Result(15163154141133124, ['6H', '5S', '4C', '3H', '2S'])),
    (['9S', 'QH', 'KC', 'JS', 'TH'], Result(15231223214203194, ['KC', 'QH', 'JS', 'TH', '9S'])),
])
def test_straight(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '9S', '4S', '5S', '6S'], Result(16194164154144124, ['9S', '6S', '5S', '4S', '2S'])),
])
def test_flush(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '2H', '2C', '3S', '3H'], Result(17124123121134133, ['2S', '2H', '2C', '3S', '3H'])),
    (['2S', '2H', '2C', '3S', '3H', '3C'], Result(17134133131124123, ['3S', '3H', '3C', '2S', '2H'])),
])
def test_full_house(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '2H', '2C', '2D'], Result(18124123121122, ['2S', '2H', '2C', '2D'])),
    (['2S', '2H', '2C', '2D', '3S'], Result(18124123121122134, ['2S', '2H', '2C', '2D', '3S'])),
])
def test_quads(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2H', '3H', '4H', '5H', '6H'], Result(19163153143133123, ['6H', '5H', '4H', '3H', '2H'])),
])
def test_straight_flush(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['TH', 'JH', 'QH', 'KH', 'AH'], Result(20243233223213203, ['AH', 'KH', 'QH', 'JH', 'TH'])),
])
def test_royal_flush(test_input, expected):
    actual = analyzer.score_best_hand(test_input)

    assert actual == expected

def test_duplicate_cards_should_throw_duplicate_card_exception():
    with pytest.raises(DuplicateCardException):
        cards = ['2S', '2S']
        analyzer.score_best_hand(cards)

def test_with_whole_deck_should_return_royal_flush():
    expected = Result(20243233223213203, ['AH', 'KH', 'QH', 'JH', 'TH'])
    suits = ['H', 'D', 'S', 'C']
    ranks = [str(value) for value in range(2,10)] + 'T J Q K A'.split()
    cards = [f'{rank}{suit}' for suit in suits for rank in ranks]

    actual = analyzer.score_best_hand(cards)

    assert actual == expected

@pytest.mark.parametrize("test_input", [
    ['Don'],
    ['D0n'],
    ['D1n'],
    ['AHD'],
    ['HA'],
    ['AHAD'],
    ['AX']
])
def test_not_a_card_should_throw_invalid_card_exception(test_input):
    with pytest.raises(InvalidCardException):
        analyzer.score_best_hand(test_input)

# ___________Hand Ranks____________
# HighCard       (1)
# Pair           (2)
# Two Pair       (3)
# Set            (4)
# Straight       (5)
# Flush          (6)
# Full House     (7)
# Quads          (8)
# Straight Flush (9)
# Royal Flush    (10)

# __________Suits__________
# Spade (S)(4)
# Club (C)(1)
# Heart (H)(3)
# Diamond (D)(2)

# __________Ranks__________
# a (1)
# 2 (2)
# 3 (3)
# 4 (4)
# 5 (5)
# 6 (6)
# 7 (7)
# 8 (8)
# 9 (9)
# T (10)
# J (11)
# Q (12)
# K (13)
# A (14)

# _________Result Code Brainstorm___________
# (['TS', 'AH', '4D', '3D', 'QC'], Result(1, 2422201413, ['AH', 'QC', 'TS', '4D', '3D'])),
# 01 14H 12C 10S 04D 03D
# 11 243 221 204 042 032 ***************
# 0114H12C10S04D03D
# 011412100403
# 112422201413
# 01:14H:12C:10S:04D:03D