from abc import ABCMeta

from business.services.abstract_service import AbstractService


class SchemaService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)
