import json


class Revision:
    """
    Class Revision,
    emulates a revision, is a set of updates to files in the context of repositories linked in OpenProject
    """
    def __init__(self, json_obj):
        """Constructor for class Revision

        :param json_obj: The dict with the object data
        """
        self.__dict__ = json_obj

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
