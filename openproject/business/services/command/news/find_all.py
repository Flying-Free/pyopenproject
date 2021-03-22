from openproject.api_connection.exceptions.request_exception import RequestError
from openproject.api_connection.requests.get_request import GetRequest
from openproject.business.exception.business_error import BusinessError
from openproject.business.services.command.find_list_command import FindListCommand
from openproject.business.services.command.news.news_command import NewsCommand
from openproject.business.util.filters import Filters
from openproject.business.util.url import URL
from openproject.business.util.url_parameter import URLParameter
from openproject.model.new import New


class FindAll(NewsCommand):

    def __init__(self, connection, offset, page_size, filters, sort_by):
        super().__init__(connection)
        self.filters = filters
        self.sort_by = sort_by

    def execute(self):
        try:
            request = GetRequest(connection=self.connection,
                                  context=str(URL(f"{self.CONTEXT}",
                                                  [
                                                      Filters(
                                                          self.filters),
                                                      URLParameter
                                                      ("sortBy", self.sort_by)
                                                  ])))
            return FindListCommand(self.connection, request, New).execute()
            # for news in json_obj['_embedded']['elements']:
            #     yield New(news)
        except RequestError as re:
            raise BusinessError("Error finding all news") from re
