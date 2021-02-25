from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import NewsCommand
from pyopenproject.model import New


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
