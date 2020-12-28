from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.help_texts.help_texts_comand import HelpTextsCommand
from model.help_text import HelpText


class FindAll(HelpTextsCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            for help_text in json_obj._embedded.elements:
                yield HelpText(help_text)
        except RequestError as re:
            raise BusinessError(f"Error finding all grids") from re