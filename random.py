import random

number = random.randint(1, 10)
print(number)

# program for shuffling cards
cards = ["king", "queen", "jack"]
random.shuffle(cards)
for card in cards:
    print(card)
    #https://github.com/LisaOz/random.git