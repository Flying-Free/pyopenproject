class Group:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    def __str__(self):
        return self.__dict__
