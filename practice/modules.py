import random

#coin = random.choice(["head","tails"])
#print(coin)

#ranNum = random.randint(1,100)
#print(ranNum)

deck = ["ace","two","three","four","five","six",
        "seven","eight","nine","ten","jack","queen","king"]
    
random.shuffle(deck)
for card in deck:
    print(card)
    
