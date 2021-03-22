from src.api_connection.exceptions.request_exception import RequestError
from src.api_connection.requests.post_request import PostRequest
from src.business.exception.business_error import BusinessError
from src.business.services.command.version.version_command import VersionCommand
from src.model import version as v


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
