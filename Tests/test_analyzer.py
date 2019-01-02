import pytest
from HandAnalyzer import analyzer

@pytest.mark.parametrize("test_input,expected", [
    (['2S', '3H'], [1, 3, 2]),
    (['TS', '3H'], [1, 10, 3]),
    (['TS', 'AH'], [1, 14, 10]),
    (['TS', 'AH', '4D'], [1, 14, 10, 4]),
    (['TS', 'AH', '4D', '3D'], [1, 14, 10, 4, 3]),
    (['TS', 'AH', '4D', '3D', 'QC'], [1, 14, 12, 10, 4, 3]),
])
def test_high_card(test_input, expected):
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