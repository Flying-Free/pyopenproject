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
                if self.parameters[i].value:
                    if not are_parameters:
                        are_parameters = True
                    if i != 0:
                        content += "&"
                    content += f"{str(self.parameters[i])}"

            if are_parameters:
                output += "?" + content

        return output
