from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import HelpTextsCommand
from pyopenproject.model import HelpText


class Find(HelpTextsCommand):

    def __init__(self, connection, help_text):
        super().__init__(connection)
        self.help_text = help_text

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.help_text.id}").execute()
            return HelpText(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding help text by id: {self.help_text.id}") from re
