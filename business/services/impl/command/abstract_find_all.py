from abc import ABCMeta, abstractmethod

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.command import Command


class AbstractFindAll(Command):
    __metaclass__ = ABCMeta

    def __init__(self):
        if self.__class__ is AbstractFindAll:
            raise TypeError('Abstract class cannot be instantiated')

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, self.request_url()).execute()
            for endpoint in json_obj["_embedded"]["elements"]:
                yield self.cast(endpoint)
        except RequestError as re:
            raise BusinessError(f"Error finding all attachments") from re

    @abstractmethod
    def cast(self, endpoint):
        raise NotImplementedError

    @abstractmethod
    def request_url(self):
        raise NotImplementedError
