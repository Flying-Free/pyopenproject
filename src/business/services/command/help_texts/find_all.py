from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.get_request import GetRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.find_list_command import FindListCommand
from src.business.services.command.help_texts.help_texts_comand import HelpTextsCommand
from src.model.help_text import HelpText


class FindAll(HelpTextsCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            request = GetRequest(self.connection, f"{self.CONTEXT}")
            return FindListCommand(self.connection, request, HelpText).execute()
            # for help_text in json_obj['_embedded']['elements']:
            #     yield HelpText(help_text)
        except RequestError as re:
            raise BusinessError("Error finding all grids") from re
