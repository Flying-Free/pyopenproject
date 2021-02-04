from util.URLParameter import URLParameter


class Filters(URLParameter):

    def __init__(self, name, value):
        super().__init__(name, value)

    def __str__(self) -> str:
        output = f"{self.name}=["
        for i in range(len(self.value)):
            output += "{"
            output += f"\"{self.value[i].name}\":"
            output += "{"
            output += f"\"operator\":\"{self.value[i].operator}\",\"values\":["
            for j in range(len(self.value[i].values)):
                output += f"\"{self.value[i].values[j]}\""
                output += "," if len(self.value) != 1 and i != len(self.value)-1 else ""
            output += "]}}"
            output += "," if len(self.value) != 1 and i != len(self.value)-1 else ""
        output += "]"
        return output
