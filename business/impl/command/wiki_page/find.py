from model.wiki_page import WikiPage

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.wiki_page.wiki_command import WikiPageCommand


class Find(WikiPageCommand):

    def __init__(self, wiki_page):
        self.wiki_page = wiki_page

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.wiki_page.id}")
            return WikiPage(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding wiki_page by ID: {self.wiki_page.id}") from re
