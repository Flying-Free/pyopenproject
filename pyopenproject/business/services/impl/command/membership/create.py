from pyopenproject import model as mem
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import MembershipCommand


class Create(MembershipCommand):

    def __init__(self, connection, membership):
        """Constructor for class Create, from MembershipCommand
        :param connection: The connection data
        :param membership: The membership to create
        """
        super().__init__(connection)
        self.membership = membership

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   json=self.membership.__dict__).execute()
            return mem.Membership(json_obj)
        except RequestError as re:
            raise BusinessError("Error creating membership") from re
