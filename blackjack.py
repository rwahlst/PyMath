from Utility.constants import Constants
from Utility.command import Command
from Utility.command import Command
from Utility.BlackJack.player import Player
from Utility.BlackJack.deck import Deck
from Utility.BlackJack.hand import Hand

class BlackJack:

    commands = Command.BlkJckCmdType
    constantsRef = None
    player = None
    running = False
    debug = False
    deck = None

    def __init__(self):
        self.player = Player()
        self.constantsRef = Constants()
        self.constantsRef.SystemClear()

    def Start(self):
        self.running = True

        self.deck = Deck(5, True)

        print(self.constantsRef.BAR)
        print(self.constantsRef.LIB_BLACK_JACK_NAME + " v" + self.constantsRef.LIB_BLACK_JACK_VERSION)
        print(self.constantsRef.BAR)
        print("Enter a command to begin... Or type 'help' at any time to get help")
        pName = input("But first, what is your name? - ")

        self.player.name = pName
        print("Welcome, " + self.player.name + "!")
        print(self.constantsRef.BAR)

        while self.running:
            uInput = input()
            cmd = Command(uInput, self.constantsRef.Context.BLK_JCK)
            self.ExecuteCommand(cmd)

            if not self.running:
                break

    def ExecuteCommand(self, cmd):
        cmdType = cmd.cmd
        if cmdType == self.commands.EXIT:
            self.Exit()
        elif cmdType == self.commands.HELP:
            self.Help()
        elif cmdType == self.commands.BAL:
            self.Bal()
        elif cmdType == self.commands.DEAL:
            self.Deal()
        elif cmdType == self.commands.NOOP:
            pass
        else:
            pass

    def Deal(self):

        initial_hands = self.GetInitialHands()
        dealer_hand = Hand(initial_hands[0], Hand.HandType.Dealer)
        player_hand = Hand(initial_hands[1], Hand.HandType.Player)

        print(dealer_hand)
        print(player_hand)



    def GetInitialHands(self):
        dealer_hand = []
        player_hand = []
        dealer_hand.append(self.deck.Draw())
        player_hand.append(self.deck.Draw())
        dealer_hand.append(self.deck.Draw())
        player_hand.append(self.deck.Draw())
        return [dealer_hand, player_hand]


    def Exit(self):
        self.running = False
        self.constantsRef.SystemClear()
        self.constantsRef.PrintWelcome()

    def Bal(self):
        print(self.constantsRef.BAR)
        print("Displaying balance for player: " + self.player.name)
        print(self.constantsRef.BAR)
        print("Balance (USD): " + self.player.GetBalance())
        print("Win %: " + self.player.WinPercent())

    def Help(self):
        print("Showing a list of commands for black jack:")
        print("1.) Help - Show list of commands")
        print("2.) Deal - Deal a game of blackjack")
        print("3.) Rules - Learn the basic black jack rules")
        print("4.) Balance - Display your balance for the current running instance")
        print("5.) Exit - Return to " + self.constantsRef.LIB_NAME + " shell")
        print("More coming soon!")
        print(self.constantsRef.BAR)
