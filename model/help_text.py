import json


class HelpText:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def __str__(self):
        return json.dumps(self.__dict__)
