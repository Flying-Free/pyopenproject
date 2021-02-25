from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import MembershipCommand
from pyopenproject.model import Form


class CreateForm(MembershipCommand):

    def __init__(self, connection, membership):
        """Constructor for class CreateForm, from MembershipCommand

        :param connection: The connection data
        :param membership: The membership to create the form
        """
        super().__init__(connection)
        self.membership = membership

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/form",
                                   json=self.membership.__dict__).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating form from membership "
                                f"'{self.membership.__dict__['_links']['self']['href']}'") from re
