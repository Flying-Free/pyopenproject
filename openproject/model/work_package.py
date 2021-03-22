import json


class WorkPackage:
    """
    Class WorkPackage,
    emulates a work package, can basically be everything you need to keep track off within your projects.
    It can be e.g. a task, a feature, a bug, a risk, a milestone or a project phase
    """
    def __init__(self, json_obj):
        """Constructor for class WorkPackage

        :param json_obj: The dict with the object data
        """
        self.__dict__ = json_obj

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
