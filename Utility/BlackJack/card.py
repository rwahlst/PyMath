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
        f = str(self.face)
        s = str(self.suit)
        return "[" + f[f.index('.') + 1:] + " of " + s[s.index('.') + 1:] + "]"

    def GetValue(self, curr_value=0, aces_only=False):
        if not aces_only:
            if self.face == self.Faces.TWO:
                return 2
            elif self.face == self.Faces.THREE:
                return 3
            elif self.face == self.Faces.FOUR:
                return 4
            elif self.face == self.Faces.FIVE:
                return 5
            elif self.face == self.Faces.SIX:
                return 6
            elif self.face == self.Faces.SEVEN:
                return 7
            elif self.face == self.Faces.EIGHT:
                return 8
            elif self.face == self.Faces.NINE:
                return 9
            elif self.face == self.Faces.TEN:
                return 10
            elif self.face == self.Faces.JACK:
                return 10
            elif self.face == self.Faces.QUEEN:
                return 10
            elif self.face == self.Faces.KING:
                return 10
            elif self.face == self.Faces.ACE:
                return 0
            else:
                return 0
        else:
            if self.face == self.Faces.ACE:
                if curr_value + 11 <= 21:
                    return 11
                else:
                    return 1
            else:
                return 0
