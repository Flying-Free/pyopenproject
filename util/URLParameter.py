class URLParameter:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name}={self.value}"

