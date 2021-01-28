class URL:

    def __init__(self, base, parameters):
        self.base = base
        self.parameters = parameters

    def __str__(self) -> str:
        output = f"{self.base}"
        if self.parameters:
            output += "?"
            for i in range(len(self.parameters)):
                if self.parameters[i].value is not None:
                    output += f"{str(self.parameters[i])}"
                    output += "&" if len(self.parameters)!=1 and i != len(self.parameters)-1 else ""
        return output

