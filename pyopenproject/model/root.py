import json


class Root:
    """
    Class Root,
    emulates a root,  contains links to available resources in the API. By following these links a client should be
    able to discover further resources in the API
    """
    def __init__(self, json_obj):
        """Constructor for class Root

        :param json_obj: The dict with the object data
        """
        self.__dict__ = json_obj

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
