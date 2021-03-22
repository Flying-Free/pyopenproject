from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.get_request import GetRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.find_list_command import FindListCommand
from src.business.services.command.membership.membership_command import MembershipCommand
from src.model.project import Project


class FindAvailable(MembershipCommand):

    def __init__(self, connection):
        """Constructor for class FindAvailable, from MembershipCommand

        :param connection: The connection data
        """
        super().__init__(connection)

    def execute(self):
        try:
            request = GetRequest(self.connection, f"{self.CONTEXT}/available_projects")
            return FindListCommand(self.connection, request, Project).execute()
            # for tEntry in json_obj['_embedded']['elements']:
            #     yield p.Project(tEntry)
        except RequestError as re:
            raise BusinessError("Error finding the available memberships") from re
