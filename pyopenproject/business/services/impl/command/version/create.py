from pyopenproject import model as v
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import VersionCommand


class Create(VersionCommand):

    def __init__(self, connection, version):
        """Constructor for Create, from VersionCommand

        :param connection: The connection data
        :param version: The version to create
        """
        super().__init__(connection)
        self.version = version

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}",
                                   json=self.version.__dict__).execute()
            return v.Version(json_obj)
        except RequestError as re:
            raise BusinessError("Error creating version") from re
