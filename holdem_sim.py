from deck import Deck
import hand_analyzer

deck = Deck()
deck.shuffle()

player_one_cards = []
player_two_cards = []
board = []

player_one_cards.append(deck.draw_card())
player_two_cards.append(deck.draw_card())
player_one_cards.append(deck.draw_card())
player_two_cards.append(deck.draw_card())

deck.draw_card()
board.append(deck.draw_card())
board.append(deck.draw_card())
board.append(deck.draw_card())

deck.draw_card()
board.append(deck.draw_card())

deck.draw_card()
board.append(deck.draw_card())

player_one_hand = ' '.join(player_one_cards + board)
player_two_hand = ' '.join(player_two_cards + board)

player_one_result = hand_analyzer.analyze_hand(player_one_hand)
player_two_result = hand_analyzer.analyze_hand(player_two_hand)

for i, val in enumerate(player_one_result.split()):
    print(val)

print(player_one_cards)
print(player_two_cards)
print(board)

print(player_one_result)
print(player_two_result)

print('Done!')