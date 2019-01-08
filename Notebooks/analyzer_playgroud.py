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

#%%
if type(1) is not int:
    print(True)
else:
    print(False)


#%%
from HandAnalyzer.card import Card

c = Card('A', 'S')
x = Card('A', 'S')

print(c == x)

#%%
p = [1, 2, 3,4,1,23,4,5,6,7,6,4,56,45,6]
slice(p)

sorted(p)[:5]

p = p[:5]
p

#%%
x = ['AS']
y = ['AS']

if x == y:
    print(True)
