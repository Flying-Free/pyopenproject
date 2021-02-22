
from business.services.impl.command.abstract_find_all import AbstractFindAll
from model.status import Status


class FindAll(AbstractFindAll):

    def __init__(self, connection):
        super().__init__(connection)

    def cast(self, endpoint):
        return Status(endpoint)

    def request_url(self):
        return f"{self.CONTEXT}"
