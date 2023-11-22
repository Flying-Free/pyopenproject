from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.find_list_command import FindListCommand
from pyopenproject.business.services.command.notification.notification_command import NotificationCommand
from pyopenproject.business.util.filters import Filters
from pyopenproject.business.util.url import URL
from pyopenproject.business.util.url_parameter import URLParameter
from pyopenproject.model.notification import Notification


class FindAll(NotificationCommand):

    def __init__(self, connection, offset, page_size, filters,
                 sort_by, group_by):
        super().__init__(connection)
        self.offset = offset
        self.page_size = page_size
        self.filters = filters
        self.group_by = group_by
        self.sort_by = sort_by

    def execute(self):
        try:
            request = GetRequest(self.connection,
                                 str(URL(f"{self.CONTEXT}",
                                         [
                                             Filters(
                                                 self.filters),
                                             URLParameter(
                                                 "groupBy", self.group_by),
                                             URLParameter(
                                                 "sortBy", self.sort_by),
                                             URLParameter(
                                                 "offset", self.offset),
                                             URLParameter(
                                                 "pageSize", self.page_size),
                                         ])
                                     ))
            return FindListCommand(self.connection, request, Notification).execute()

        except RequestError as re:
            raise BusinessError(
                f"Error finding notifications:{re.args}")
