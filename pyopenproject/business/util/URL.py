class URL:

    def __init__(self, base, parameters):
        """Constructor for class URL.

        :param base: The base of the URL
        :param parameters: The URL parameters
        """
        self.base = base
        self.parameters = parameters

    def __str__(self) -> str:
        """Return the URL as a string.

        :return: The URL as a string
        """
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
