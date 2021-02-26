import json


class Role:
    """
    Class Role,
    emulates a role. When principals (groups or users) are assigned to a project, they are receive roles in
    that project. Roles regulate access to specific resources by having permissions configured for them.
    """
    def __init__(self, json_obj):
        """Constructor for class Role

        :param json_obj: The dict with the object data
        """
        self.__dict__ = json_obj

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
