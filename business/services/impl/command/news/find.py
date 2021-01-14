from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.news.news_command import NewsCommand
from model.news import News


class Find(NewsCommand):

    def __init__(self, news):
        self.news = news

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.news.id}")
            return News(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding news by id: {self.news.id}") from re