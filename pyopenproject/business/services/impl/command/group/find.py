from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import GroupCommand
from pyopenproject.model import Group


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
