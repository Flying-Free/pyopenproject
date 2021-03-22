from abc import ABCMeta

from pyopenproject.business.abstract_service import AbstractService


class SchemaService(AbstractService):
    """
    Class SchemaService,
    service for schema endpoint
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)
