from .card import Card
import random

class Deck:

    numDecks = 0
    deck = None
    discard = None

    def __init__(self, numDecks, shouldShuffle):
        self.numDecks = numDecks
        self.Initialize(shouldShuffle)

    Shuffle = lambda: random.shuffle(self.deck)

    def Initialize(self, shuffle=False):
        self.deck = []
        self.discard = []

        numCards = self.numDecks * 52 # 52 card decks
        for i in range(0, numCards):
            self.deck.append(Card(i))

        if shuffle:
            self.Shuffle()

    def Reset(self):
        self.Initialize(True)
