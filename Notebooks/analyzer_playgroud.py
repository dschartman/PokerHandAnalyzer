from HandAnalyzer import analyzer

cards = ['AS', 'JD']
cards
analyzer.DetermineBestFiveCardHand(cards)


cards = ['1', '2', '3']
cards.append(cards.pop(0))
cards