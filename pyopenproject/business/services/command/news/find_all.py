from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.news.news_command import NewsCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model.new import New


class FindAll(NewsCommand):

    def __init__(self, connection, offset, page_size, filters, sort_by):
        super().__init__(connection)
        self.offset = offset
        self.page_size = page_size
        self.filters = filters
        self.sort_by = sort_by

    def execute(self):
        try:
            json_obj = GetRequest(connection=self.connection,
                                  context=str(URL(f"{self.CONTEXT}",
                                                  [
                                                      URLParameter
                                                      ("offset", self.offset),
                                                      URLParameter
                                                      ("pageSize", self.page_size),
                                                      Filters(
                                                          self.filters),
                                                      URLParameter
                                                      ("sortBy", self.sort_by)
                                                  ]))).execute()

            for news in json_obj['_embedded']['elements']:
                yield New(news)
        except RequestError as re:
            raise BusinessError("Error finding all news") from re
