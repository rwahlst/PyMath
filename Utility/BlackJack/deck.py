from .card import Card
import random

class Deck:

    numDecks = 0
    deck = None
    discard = None

    def __init__(self, numDecks, shouldShuffle):
        self.numDecks = numDecks
        self.Initialize(shouldShuffle)

    def Initialize(self, shuffle=False):
        self.deck = []
        self.discard = []

        numCards = self.numDecks * 52 # 52 card decks
        for i in range(0, numCards):
            self.deck.append(Card(i))

        if shuffle:
            self.Shuffle(15)

        self.deck.append(Card(-1)) # Add EOF

    def Reset(self):
        self.Initialize(True)

    def Shuffle(self, n_shuffles):
        for i in range(0, n_shuffles + 1):
            random.shuffle(self.deck)

    def Draw(self):
        c = self.deck.pop() if len(self.deck) > 0 else None
        if c == None or c.suit == Card.Suits.EOF or c.face == Card.Faces.EOF:
            print("No Cards Remaining")
            return None
        return c
