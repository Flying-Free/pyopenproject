class URLParameter:

    def __init__(self, name, value):
        """
        Constructor for class URLParameter

        :param name: Parameter name
        :param value: Parameter value
        """
        self.name = name
        self.value = value

    def __str__(self) -> str:
        """ Converts the URL parameter to a string

        :return: The parameter as a string to insert it in an URL
        """
        return f"{self.name}={self.value}"
