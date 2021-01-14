from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.help_texts.help_texts_comand import HelpTextsCommand
from model.help_text import HelpText


class Find(HelpTextsCommand):

    def __init__(self, help_text):
        self.help_text = help_text

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.help_text.id}")
            return HelpText(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding help text by id: {self.help_text.id}") from re