from card import Card

def determine_rank(card):
    return Card(card, 'S').rankValue

#Example hand = AS AC JD 9H 2D
def analyze_hand(hand):
    cards = sorted(
        [Card(rank, suit) for rank, suit in hand.split()],
        key = lambda card: card.rankValue,
        reverse=True)

    handRank = 1

    output = ' '.join(str(card.rankValue) for card in cards)

    return f'{handRank} {output}'
