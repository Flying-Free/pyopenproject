from pyopenproject.business.util.url_parameter import URLParameter


class Filters(URLParameter):

    def __init__(self, value):
        """Constructor for class Filters, from URLParameter.

        :param value: Value
        """
        super().__init__('filters', value)

    def __str__(self) -> str:
        """Return the Filters as a string.

        :return: The filters as a string
        """
        output = f"{self.name}=["
        for i in range(len(self.value)):
            output += "{"
            output += f"\"{self.value[i].name}\":"
            output += "{"
            output += f"\"operator\":\"{self.value[i].operator}\",\"values\":["
            for j in range(len(self.value[i].values)):
                if j != 0:
                    output += ","
                output += f"\"{self.value[i].values[j]}\""
            output += "]}}"
            output += "," if len(self.value) != 1 and i != len(self.value)-1 else ""
        output += "]"
        return output
