from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.news.news_command import NewsCommand
from model.new import New


class FindAll(NewsCommand):

    def __init__(self, connection, offset, pageSize, filters, sortBy):
        super().__init__(connection)
        self.offset = offset
        self.pageSize = pageSize
        self.filters = filters
        self.sortBy = sortBy

    def execute(self):
        try:
            json_obj = GetRequest(connection=self.connection,
                                  context=f"{self.CONTEXT}?{self.offset},{self.pageSize},{self.filters},{self.sortBy}")\
                .execute()
            for news in json_obj._embedded.elements:
                yield New(news)
        except RequestError as re:
            raise BusinessError(f"Error finding all news") from re
