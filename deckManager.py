import random
from cardManager import Card

class Deck:

    def __init__(self, decksInShoe):
        self.cards = []
        self.decksInShoe = decksInShoe
        self.build()



    def build(self):
        suits = ["Heart", "Diamond", "Club", "Spade"]
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for x in range(self.decksInShoe):

            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(suit=suit, rank=rank))


                    
    def shuffle(self):
        random.shuffle(self.cards)



    def dealCard(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        
        else:
            return None



testDeck = Deck(decksInShoe=6)
for card in testDeck.cards:
    print(card)

testDeck.shuffle()


for card in testDeck.cards:
    print(card)

print("Dealing Card", testDeck.dealCard())
print("Dealing Card", testDeck.dealCard())
print("Dealing Card", testDeck.dealCard())

print(testDeck.cards[-1])