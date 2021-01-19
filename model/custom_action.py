class CustomAction:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

    # TODO
    #     "executeImmediately": {
    #         "href": "/apiChanges project and type in one go",
    #         "title": "Execute Change project and type",
    #         "method": "post"
    #     }

    def __str__(self):
        return self.__dict__
