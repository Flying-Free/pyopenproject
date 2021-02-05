class URL:

    def __init__(self, base, parameters):
        self.base = base
        self.parameters = parameters

    def __str__(self) -> str:
        output = f"{self.base}"
        if self.parameters:
            # output += "?"
            are_parameters = False
            content = ""
            for i in range(len(self.parameters)):
                if self.parameters[i].value is not None:
                    if not are_parameters:
                        are_parameters = True
                    content += f"{str(self.parameters[i])}"
                    content += "&" if len(self.parameters) != 1 and i != len(self.parameters) - 1 else ""
            if are_parameters:
                output += "?" + content

        return output
