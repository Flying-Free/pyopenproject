import json


class Activity:
    """
    Class Activity,
    emulates a module that displays the actions performed in a project over a certain period of time
    """
    def __init__(self, json_obj):
        """
        Constructor for class Activity

        :param json_obj: The dict with the object data
        """
        self.__dict__ = json_obj

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
