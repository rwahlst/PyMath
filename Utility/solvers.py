

class Solvers:

    debug = False

    def Standard(self, eq):
        variables = self.GetVariables(eq)
        print(variables)



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
