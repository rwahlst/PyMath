from enum import IntEnum

class Card:

    class Suits(IntEnum):
        EOF = -1
        DIAMONDS = 1,
        HEARTS = 2,
        SPADES = 3,
        CLUBS = 4

    class Faces(IntEnum):
        EOF = -1
        ACE = 1,
        TWO = 2,
        THREE = 3,
        FOUR = 4,
        FIVE = 5,
        SIX = 6,
        SEVEN = 7,
        EIGHT = 8,
        NINE = 9,
        TEN = 10,
        JACK = 11,
        QUEEN = 12,
        KING = 13

    suit = None
    face = None

    def __init__(self, i):
        self.TranslateSuit(i)
        self.TranslateFace(i)

    def TranslateSuit(self, n):
        suit = (n % 4) + 1
        self.suit = self.Suits(suit)

    def TranslateFace(self, n):
        face = (n % 13) + 1
        self.face = self.Faces(face)

    def __str__(self):
        return str(self.face) + " of " + str(self.suit)
