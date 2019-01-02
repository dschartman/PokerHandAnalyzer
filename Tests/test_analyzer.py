import pytest
from HandAnalyzer import analyzer

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '3H'], analyzer.Result(11133124, ['3H', '2S'])),
    (['TS', '3H'], analyzer.Result(11204133, ['TS', '3H'])),
    (['TS', 'AH'], analyzer.Result(11243204, ['AH', 'TS'])),
    (['TS', 'AH', '4D'], analyzer.Result(11243204142, ['AH', 'TS', '4D'])),
    (['TS', 'AH', '4D', '3D'], analyzer.Result(11243204142132, ['AH', 'TS', '4D', '3D'])),
    (['TS', 'AH', '4D', '3D', 'QC'], analyzer.Result(11243221204142132, ['AH', 'QC', 'TS', '4D', '3D'])),
    (['TS', 'AH', '2D', '3D', 'QC'], analyzer.Result(11243221204132122, ['AH', 'QC', 'TS', '3D', '2D'])),
    (['TS', 'AH', '2D', '3D', 'QC', 'KC'], analyzer.Result(11243231221204132, ['AH', 'KC', 'QC', 'TS', '3D'])),
])
def test_high_card(test_input, expected):
    actual = analyzer.DetermineBestFiveCardHand(test_input)

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
    actual = analyzer.DetermineBestFiveCardHand(test_input)

    assert len(actual.best_five) == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '2H'], analyzer.Result(12124123, ['2S', '2H'])),
    (['3H', '2S', '2H'], analyzer.Result(12124123133, ['2S', '2H', '3H'])),
    (['AC', '3H', '2S', '2H'], analyzer.Result(12124123241133, ['2S', '2H', 'AC', '3H'])),
])
def test_pair(test_input, expected):
    actual = analyzer.DetermineBestFiveCardHand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['3C', '3H', '2S', '2H'], analyzer.Result(13131133124123, ['3C', '3H', '2S', '2H'])),
    (['3C', '3H', 'AS', 'AH', '8C', '8H'], analyzer.Result(13244243181183131, ['AS', 'AH', '8C', '8H', '3C'])),
])
def test_two_pair(test_input, expected):
    actual = analyzer.DetermineBestFiveCardHand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '2H', '2C'], analyzer.Result(14124123121, ['2S', '2H', '2C'])),
    (['2S', '2H', '2C', '5D', '3C'], analyzer.Result(14124123121152131, ['2S', '2H', '2C', '5D', '3C'])),
])
def test_set(test_input, expected):
    actual = analyzer.DetermineBestFiveCardHand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '3H', '4C', '5S', '6H'], analyzer.Result(15163154141133124, ['6H', '5S', '4C', '3H', '2S'])),
    (['2S', '3H', '4C', '5S', '6H', '7S'], analyzer.Result(15174163154141133, ['7S', '6H', '5S', '4C', '3H'])),
    (['9S', 'QH', 'KC', 'JS', 'TH'], analyzer.Result(15231223214203194, ['KC', 'QH', 'JS', 'TH', '9S'])),
])
def test_straight(test_input, expected):
    actual = analyzer.DetermineBestFiveCardHand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '9S', '4S', '5S', '6S'], analyzer.Result(16194164154144124, ['9S', '6S', '5S', '4S', '2S'])),
])
def test_flush(test_input, expected):
    actual = analyzer.DetermineBestFiveCardHand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '2H', '2C', '3S', '3H'], analyzer.Result(17124123121134133, ['2S', '2H', '2C', '3S', '3H'])),
    (['2S', '2H', '2C', '3S', '3H', '3C'], analyzer.Result(17134133131124123, ['3S', '3H', '3C', '2S', '2H'])),
])
def test_full_house(test_input, expected):
    actual = analyzer.DetermineBestFiveCardHand(test_input)

    assert actual == expected

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
# (['TS', 'AH', '4D', '3D', 'QC'], analyzer.Result(1, 2422201413, ['AH', 'QC', 'TS', '4D', '3D'])),
# 01 14H 12C 10S 04D 03D
# 11 243 221 204 042 032 ***************
# 0114H12C10S04D03D
# 011412100403
# 112422201413
# 01:14H:12C:10S:04D:03D