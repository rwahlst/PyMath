import os
from enum import Enum

class Constants:

    class Context(Enum):
        SHELL = -1,
        EQ = 0

    LIB_NAME = "Pythongebra"
    LIB_VERSION = "12.2023"
    LIB_DEVELOPER = "Axel Wahlstrom"
    BAR = "====================================================================="

    def PrintWelcome(self):
        print(self.BAR)
        print(self.LIB_NAME + " V" + self.LIB_VERSION)
        print("Enter a command to begin... Or type 'help' at any time to get help")
        print(self.BAR)

    def PrintAbout(self):
        print(self.BAR)
        print("Welcome to " + self.LIB_NAME + " V" + self.LIB_VERSION + "!!! by " + self.LIB_DEVELOPER)
        print("A Python Mathematical Library!")
        print(self.BAR)
        print("Hit enter to continue...")

    def PrintHelp(self):
        print("Showing list of available commands - type any of them to begin...")
        print("1.) Exit - (exit the shell)")
        print("2.) Help - (display list of available commands)")
        print("3.) About - (display info about " + self.LIB_NAME + ")")
        print("4.) Clear - (clear shell console)")
        print("5.) Equation - (begin a flow that solves multi-dimensional equations)")

    def SystemClear(self):
        os.system("clear") # implement for other operating systems later
