from enum import Enum
from Utility.constants import Constants

class Command:

    class CmdType(Enum):
        NOOP = 0,
        EXIT = 1,
        HELP = 2,
        ABOUT = 3,
        CLEAR = 4,
        EQUATION_SOLVER = 5
        BLACK_JACK = 6

    class BlkJckCmdType(Enum):
        NOOP = 0,
        EXIT = 1,
        HELP = 2,
        BAL = 3

    cmd = None # this object's current command state (Type: CmdType ENUM)
    constantsRef = None # const ref
    userInput = ""

    def __init__(self, cmd, ctx):
        self.userInput = cmd
        self.constantsRef = Constants()

        if ctx == self.constantsRef.Context.SHELL:
            self.cmd = self.GetCommand(cmd)
        elif ctx == self.constantsRef.Context.EQ:
            self.cmd = self.GetEQCommand(cmd)
        elif ctx == self.constantsRef.Context.BLK_JCK:
            self.cmd = self.GetBJCommand(cmd)
        else:
            self.cmd = self.GetCommand(cmd)

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
        elif "6" in upperCase or "BL" in upperCase or "JA" in upperCase:
            return self.CmdType.BLACK_JACK
        else:
            return self.CmdType.NOOP

    def GetEQCommand(self, cmd_msg):
        upperCase = cmd_msg.upper()
        if "EXIT" in upperCase:
            return self.CmdType.EXIT
        else:
            return self.CmdType.NOOP

    def GetBJCommand(self, cmd_msg):
        upperCase = cmd_msg.upper()
        if "EXIT" in upperCase:
            return self.BlkJckCmdType.EXIT
        if "HELP" in upperCase:
            return self.BlkJckCmdType.HELP
        if "BAL" in upperCase:
            return self.BlkJckCmdType.BAL
        else:
            return self.BlkJckCmdType.NOOP
