from HandAnalyzer import analyzer

cards = ['AS', 'JD']
cards
analyzer.score_best_hand(cards)


cards = ['1', '2', '3']
cards.append(cards.pop(0))
cards

cards = ['2S', '2C']
seen = set()
uniq = []
for x in cards:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
    else:
        print('GOTCHA!')

seen

# %%
cards = ['2S', '2C', '3H', '3D', '4C', '4S', '5S', '5D', '6H', '6C', '7S', '7C']
cards.sort(reverse = True)
cards