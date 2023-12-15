

class Player:

    name = ""
    balance = 0
    win = 0
    loss = 0
    games_played = 0
    hand = None

    def __init__(self):
        self.balance = 100.00

    def GetBalance(self):
        return "$" + str(self.balance)

    def Win(self, winnings):
        self.games_played += 1
        self.win += 1
        self.balance += winnings
        self.balance = round(self.balance, 2)

    def Loss(self, bet):
        self.games_played += 1
        self.loss += 1
        self.balance -= bet
        self.balance = round(self.balance, 2)

    def WinPercent(self):
        wPercent = 0
        try:
            wPercent = (self.win / self.games_played) * 100
        except:
            wPercent = 0
        return str(wPercent) + "%"
