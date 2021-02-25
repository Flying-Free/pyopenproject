from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import RootCommand
from pyopenproject.model import Root


class Find(RootCommand):

    def __init__(self, connection):
        """Constructor for class Find, from RootCommand

        :param connection: The connection data
        """
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            return Root(json_obj)
        except RequestError as re:
            raise BusinessError("Error finding root") from re
