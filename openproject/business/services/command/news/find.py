from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.news.news_command import NewsCommand
from openproject.model.new import New


class Find(NewsCommand):

    def __init__(self, connection, news):
        super().__init__(connection)
        self.news = news

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.news.id}").execute()
            return New(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding news by id: {self.news.id}") from re
