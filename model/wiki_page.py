import business.service_factory as service_factory


class WikiPage:

    def __init__(self, json_obj):
        self.__dict__ = json_obj


