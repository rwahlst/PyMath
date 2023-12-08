from Utility.constants import Constants
from Utility.command import Command
from Utility.solvers import Solvers
import re

class EquationSolver:

    constantsRef = None
    running = False
    debug = False
    solver_func = Solvers().Standard

    operations = ['*', '/', '-', '+']

    def __init__(self):
        self.constantsRef = Constants()
        self.constantsRef.SystemClear()

    def Start(self):
        self.running = True
        print(self.constantsRef.BAR)
        print(self.constantsRef.LIB_EQ_SOLVER_NAME + " v" + self.constantsRef.LIB_EQ_SOLVER_VERSION)
        print(self.constantsRef.BAR)
        print("Type an equation and I will try to find the solution!")
        print("If you forget to include '=' in your equation")
        print("Then I will try to solve its roots at =0 ... ")
        print("You may also type 'exit' at any point to exit the equation solver")
        print(self.constantsRef.BAR)

        while self.running:
            uInput = input()
            cmd = Command(uInput, self.constantsRef.Context.EQ)
            self.ExecuteCommand(cmd)

            if not self.running:
                break

            self.Solve(cmd.userInput)

    def ExecuteCommand(self, cmd):
        cmdType = cmd.cmd
        if cmdType == Command.CmdType.EXIT:
            self.Exit()
        elif cmdType == Command.CmdType.NOOP:
            pass
        else:
            pass

    def Exit(self):
        self.running = False
        self.constantsRef.SystemClear()
        self.constantsRef.PrintWelcome()

    # The meat of this particular library extension
    # takes input of string - equation to solve
    # will (attempt) to solve for the given equivalence
    # if no equivalence
    def Solve(self, eq):
        if self.ValidateEquation(eq):
            eq = self.RefineEquation(eq)
            variables = self.GetVariables(eq)
            return self.solver_func(eq)
        else:
            print("'" + eq + "' was not a recognized equation... sorry about that, try typing it a different way.")

    def ValidateEquation(self, eq):
        pattern = r'^[a-zA-Z0-9+\-*/=()^\s]+$'
        return bool(re.match(pattern, eq))

    def RefineEquation(self, eq):
        eq = eq.replace(' ', '')
        if '=' in eq:
            begin = eq[:eq.index('=')]
            end = eq[eq.index('=') + 1:]
            if len(end) == 0:
                eq += '0'
        else:
            eq += "=0"
        return eq

    def GetVariables(self, eq):
        var_list = []
        op_output = "Detected Variables: "
        for char in eq:
            if char.isalpha():
                op_output += str(char) + ", "
                var_list.append(char)

        if self.debug:
            print(op_output)

        return var_list
