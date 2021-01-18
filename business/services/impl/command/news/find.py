from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.news.news_command import NewsCommand
from model.new import News


class Find(NewsCommand):

    def __init__(self, connection, news):
        super(connection)
        self.news = news

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.news.id}").execute()
            return News(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding news by id: {self.news.id}") from re
