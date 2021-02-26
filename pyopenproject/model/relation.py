import json


class Relation:
    """
    Class Relation,
    emulates a work packages relation
    """
    def __init__(self, json_obj):
        """Constructor for class Relation

        :param json_obj: The dict with the object data
        """
        self.__dict__ = json_obj

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
