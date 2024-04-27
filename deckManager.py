import random
from cardManager import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ["Heart", "Diamond", "Club", "Spade"]
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit=suit, rank=rank))

    def shuffle(self):
        random.shuffle(self.cards)


testDeck = Deck()
testDeck.build()
for card in testDeck.cards:
    print(card)

testDeck.shuffle()


for card in testDeck.cards:
    print(card)