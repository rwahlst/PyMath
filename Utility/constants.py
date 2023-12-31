import os
from enum import Enum

class Constants:

    class Context(Enum):
        SHELL = -1,
        EQ = 0,
        BLK_JCK = 1

    LIB_NAME = "Pythongebra"
    LIB_VERSION = "0.0.4"
    LIB_DEVELOPER = "Axel Wahlstrom"
    BAR = "====================================================================="

    LIB_EQ_SOLVER_NAME = "PyEqSolv"
    LIB_EQ_SOLVER_VERSION = "1.0.0"

    LIB_BLACK_JACK_NAME = "BlackJackEng"
    LIB_BLACK_JACK_VERSION = "1.0.0"
    NUM_DECKS = 7

    APPLICATION_CURSOR = '>'

    def PrintWelcome(self):
        print(self.BAR)
        print(self.LIB_NAME + " V" + self.LIB_VERSION)
        print("Enter a command to begin... Or type 'help' at any time to get help")
        print(self.BAR)

    def PrintAbout(self):
        print(self.BAR)
        print("Welcome to " + self.LIB_NAME + " V" + self.LIB_VERSION + "!!! by " + self.LIB_DEVELOPER)
        print("A Python Mathematical Library!")
        print("Current integrations:")
        print("1.) Equation Solver " + self.LIB_EQ_SOLVER_NAME + " v" + self.LIB_EQ_SOLVER_VERSION)
        print("2.) Black Jack Engine " + self.LIB_BLACK_JACK_NAME + " v" + self.LIB_BLACK_JACK_VERSION)
        print(self.BAR)
        print("Hit enter to continue...")

    def PrintHelp(self):
        print("Showing list of available commands - type any of them to begin...")
        print("1.) Exit - (exit the shell)")
        print("2.) Help - (display list of available commands)")
        print("3.) About - (display info about " + self.LIB_NAME + ")")
        print("4.) Clear - (clear shell console)")
        print("5.) Equation - (begin a flow that solves multi-dimensional equations)")
        print("6.) Black Jack - Start BlackJack Engine")

    def SystemClear(self):
        os.system("clear") # implement for other operating systems later
