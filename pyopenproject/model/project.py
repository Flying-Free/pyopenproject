import json


class Project:
    """
    Class Project,
    emulates a project, container structuring the information (e.g. work packages, wikis) into smaller groups.
    They can be used in a classic project management approach but also when structuring work by departments
    """
    def __init__(self, json_obj):
        """Constructor for class Project

        :param json_obj: The dict with the object data
        """
        self.__dict__ = json_obj

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
