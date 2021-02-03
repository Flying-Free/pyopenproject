import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.version.version_command import VersionCommand
import model.version as v


class Update(VersionCommand):

    def __init__(self, connection, version):
        super().__init__(connection)
        self.version = version

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{self.version.id}",
                                    json=json.dumps(self.version.__dict__)).execute()
            return v.Version(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating version: {self.version.id}") from re
