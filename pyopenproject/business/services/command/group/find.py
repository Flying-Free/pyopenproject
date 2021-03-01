from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.group.group_command import GroupCommand
from pyopenproject.model.group import Group


class Find(GroupCommand):

    def __init__(self, connection, group):
        """Constructor for class Find, from GroupCommand.

        :param connection: The connection data
        :param group: The group to find
        """
        super().__init__(connection)
        self.group = group

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.group.id}").execute()
            return Group(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding group by id: {self.group.id}") from re
