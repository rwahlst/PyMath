from equation_solver import EquationSolver as EquationEngine
from blackjack import BlackJack as BlackJackEngine
from Utility.constants import Constants
from Utility.command import Command

class Shell:

    running = False
    constantsRef = None

    def __init__(self):
        self.constantsRef = Constants()

    def Start(self):

        # Set everything up!
        self.running = True
        self.constantsRef.SystemClear()
        self.constantsRef.PrintWelcome()

        # Actually begin program loop
        while self.running:
            uInput = input(self.constantsRef.APPLICATION_CURSOR)
            cmd = Command(uInput, self.constantsRef.Context.SHELL)
            self.ExecuteCommand(cmd)

    def ExecuteCommand(self, cmd):
        cmdType = cmd.cmd
        if cmdType == Command.CmdType.EQUATION_SOLVER:
            self.EQ()
        elif cmdType == Command.CmdType.BLACK_JACK:
            self.BlackJack()
        elif cmdType == Command.CmdType.EXIT:
            self.Exit()
        elif cmdType == Command.CmdType.HELP:
            self.Help()
        elif cmdType == Command.CmdType.ABOUT:
            self.About()
        elif cmdType == Command.CmdType.CLEAR:
            self.Clear()
        elif cmdType == Command.CmdType.NOOP:
            pass
        else:
            pass


    def Clear(self):
        # support for clearing console
        self.constantsRef.SystemClear()
        self.constantsRef.PrintWelcome()

    def Help(self):
        self.constantsRef.PrintHelp()

    def About(self):
        self.constantsRef.SystemClear()
        self.constantsRef.PrintAbout()
        input()
        self.Clear()

    def EQ(self):
        eq = EquationEngine()
        eq.Start()

    def Exit(self):
        print("Goodbye!")
        exit(1)

    def BlackJack(self):
        bj = BlackJackEngine()
        bj.Start()


s = Shell()
s.Start()
