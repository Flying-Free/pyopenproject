from business.service_factory import ServiceFactory


class Document:

    def __init__(self, json_obj):
        self.__dict__ = json_obj

