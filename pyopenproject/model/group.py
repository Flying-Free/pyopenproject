import json


class Group:
    """
    Class Group,
    emulates a group, is a collection of users. They support assigning/unassigning multiple users to/from
    a project in one operation
    """
    def __init__(self, json_obj):
        """Constructor for class Group

        :param json_obj: The dict with the object data
        """
        self.__dict__ = json_obj

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
