from abc import ABCMeta

from pyopenproject.business import AbstractService


class SchemaService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)
