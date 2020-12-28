from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.news.news_command import NewsCommand
from model.news import News


class FindAll(NewsCommand):

    def __init__(self, offset, pageSize, filters, sortBy):
        self.offset = offset
        self.pageSize = pageSize
        self.filters = filters
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}?{self.offset},{self.pageSize},{self.filters},{self.sortBy}")
            for news in json_obj._embedded.elements:
                yield News(news)
        except RequestError as re:
            raise BusinessError(f"Error finding all news") from re
