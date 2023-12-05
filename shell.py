from Utility.constants import Constants
from command import Command

class Shell:

    running = False
    constantsRef = None
    context = None

    def __init__(self):
        self.constantsRef = Constants()
        self.context = self.constantsRef.Context.SHELL

    def Start(self):

        # Set everything up!
        self.running = True
        self.constantsRef.SystemClear()
        self.constantsRef.PrintWelcome()

        # Actually begin program loop
        while self.running:
            uInput = input()
            cmd = Command(uInput)

            # Set Context (if applicable)
            if cmd.cmd == Command.CmdType.EQUATION_SOLVER:
                self.context = self.constantsRef.Context.EQ

            cmd.Execute(self.context)



    def SystemClear(self):
        os.system("clear") # implement for other operating systems later


s = Shell()
s.Start()
