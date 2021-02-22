
from business.services.impl.command.abstract_find_all import AbstractFindAll
from model.type import Type


class FindAll(AbstractFindAll):

    def __init__(self, connection):
        super().__init__(connection)

    def cast(self, endpoint):
        return Type(endpoint)

    def request_url(self):
        return f"{self.CONTEXT}"
