from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.get_request import GetRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.wiki_page.wiki_command import WikiPageCommand
from src.model.wiki_page import WikiPage


class Find(WikiPageCommand):

    def __init__(self, connection, wiki_page):
        super().__init__(connection)
        self.wiki_page = wiki_page

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.wiki_page.id}").execute()
            return WikiPage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding wiki_page by ID: {self.wiki_page.id}") from re
