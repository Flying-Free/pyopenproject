import model.project as p
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand


class FindAvailable(MembershipCommand):

    def __init__(self, connection):
        """Constructor for class FindAvailable, from MembershipCommand

        :param connection: The connection data
        """
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/available_projects").execute()
            for tEntry in json_obj['_embedded']['elements']:
                yield p.Project(tEntry)
        except RequestError as re:
            raise BusinessError("Error finding the available memberships") from re
