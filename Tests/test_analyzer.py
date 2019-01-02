import pytest
from HandAnalyzer import analyzer

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '3H'], analyzer.Result(1, 1312, ['3H', '2S'])),
    (['TS', '3H'], analyzer.Result(1, 2013, ['TS', '3H'])),
    (['TS', 'AH'], analyzer.Result(1, 2420, ['AH', 'TS'])),
    (['TS', 'AH', '4D'], analyzer.Result(1, 242014, ['AH', 'TS', '4D'])),
    (['TS', 'AH', '4D', '3D'], analyzer.Result(1, 24201413, ['AH', 'TS', '4D', '3D'])),
    (['TS', 'AH', '4D', '3D', 'QC'], analyzer.Result(1, 2422201413, ['AH', 'QC', 'TS', '4D', '3D'])),
    (['TS', 'AH', '2D', '3D', 'QC'], analyzer.Result(1, 2422201312, ['AH', 'QC', 'TS', '3D', '2D'])),
])
def test_high_card(test_input, expected):
    actual = analyzer.DetermineBestFiveCardHand(test_input)

    assert actual == expected

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '2H'], analyzer.Result(2, 12, ['2S', '2H'])),
])
def test_pair(test_input, expected):
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
# Spade (S)
# Club (C)
# Heart (H)
# Diamond (D)

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