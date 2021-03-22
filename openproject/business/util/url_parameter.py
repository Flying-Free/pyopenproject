class URLParameter:

    def __init__(self, name, value):
        """Constructor for class URLParameter.

        :param name: The parameter name
        :param value: The parameter value
        """
        self.name = name
        self.value = value

    def __str__(self) -> str:
        """Converts the URL parameter to a string.

        :return: The URL as a string
        """
        return f"{self.name}={self.value}"
