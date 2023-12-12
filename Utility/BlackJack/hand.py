from enum import Enum

class Hand:

    class HandType(Enum):
        Player = 1,
        Dealer = 2

    type = None
    cards = None
    value = 0

    def __init__(self, cards, hand_type):
        self.value = 0

        if cards is not None:
            self.cards = cards
        else:
            self.cards = []

        if hand_type is not None:
            self.type = hand_type
        else:
            self.type = self.HandType.Player

    def AddCard(self, card):
        self.cards.append(card)

    def PopCard(self):
        return self.cards.pop()

    def ClearHand(self):
        self.cards = []

    def GetValue(self):
        return self.value # TODO - implement this

    def __str__(self):

        s = ""

        if self.type == self.HandType.Dealer and len(self.cards) > 0 and len(self.cards) == 2:
            s = "[X] " + " - " + str(self.cards[1])
        else:
            for i in range(0, len(self.cards)):
                if i == len(self.cards) - 1:
                    s += str(self.cards[i])
                else:
                    s += str(self.cards[i]) + " - "

        return s
