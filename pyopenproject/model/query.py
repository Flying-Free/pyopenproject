import json


class Query:
    """
    Class Query,
    emulates a query, defines how work packages can be filtered and displayed. Clients can define a query once,
    store it, and use it later on to load the same set of filters
    """
    def __init__(self, json_obj):
        """Constructor for class Query

        :param json_obj: The dict with the object data
        """
        self.__dict__ = json_obj

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
