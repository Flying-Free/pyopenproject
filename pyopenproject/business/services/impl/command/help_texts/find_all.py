from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import HelpTextsCommand
from pyopenproject.model import HelpText


class FindAll(HelpTextsCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            for help_text in json_obj['_embedded']['elements']:
                yield HelpText(help_text)
        except RequestError as re:
            raise BusinessError("Error finding all grids") from re
