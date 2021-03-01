import json


class Version:
    """
    Class Version,
    emulates a version, serve to group Work Packages into logical units where each group comprises all the work packages
    that needs to be finished in order for the version to be finished
    """
    def __init__(self, json_obj):
        """Constructor for class Version

        :param json_obj: The dict with the object data
        """
        self.__dict__ = json_obj

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
