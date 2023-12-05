from enum import Enum
from Utility.constants import Constants

class Command:

    class CmdType(Enum):
        EXIT = -2
        NOOP = -1,
        HELP = 0,
        ABOUT = 1,
        CLEAR = 2,
        EQUATION_SOLVER = 3

    cmd = None # this object's current command state (Type: CmdType ENUM)
    constantsRef = None # const ref

    def __init__(self, cmd):
        self.constantsRef = Constants()
        self.cmd = self.GetCommand(cmd)

    def Execute(self, context=None):
        if self.cmd == self.CmdType.CLEAR:
            self.Clear()
        elif self.cmd == self.CmdType.HELP:
            self.Help()
        elif self.cmd == self.CmdType.ABOUT:
            self.About()
        elif self.cmd ==self.CmdType.EQUATION_SOLVER:
            self.EQ()
        elif self.cmd == self.CmdType.EXIT:
            self.Exit()
        elif self.cmd == self.CmdType.NOOP:
            return
        else:
            return

    def GetCommand(self, cmd_msg):
        upperCase = cmd_msg.upper()
        if "1" in upperCase or "EXIT" in upperCase:
            return self.CmdType.EXIT
        if "2" in upperCase or "HELP" in upperCase:
            return self.CmdType.HELP
        elif "3" in upperCase or "ABOUT" in  upperCase:
            return self.CmdType.ABOUT
        elif "4" in upperCase or "CLEAR" in upperCase or "CLS" in upperCase:
            return self.CmdType.CLEAR
        elif "5" in upperCase or "EQ" in upperCase or "SOLVER" in upperCase:
            return self.CmdType.EQUATION_SOLVER
        else:
            return self.CmdType.NOOP

    def Clear(self):
        # support for clearing console
        self.constantsRef.SystemClear()
        self.constantsRef.PrintWelcome()

    def Help(self):
        self.constantsRef.SystemClear()
        self.constantsRef.PrintHelp()

    def About(self):
        self.constantsRef.SystemClear()
        self.constantsRef.PrintAbout()
        input()
        self.Clear()

    def EQ(self):
        print("EQ not implemented")

    def Exit(self):
        print("Goodbye!")
        exit(1)
