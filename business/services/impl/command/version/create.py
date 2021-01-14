import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.version.version_command import VersionCommand
from model.version import Version


class Create(VersionCommand):

    def __init__(self, version):
        self.version = version

    def execute(self):
        try:
            json_obj = Connection().post(f"{self.CONTEXT}", json.dumps(self.version.__dict__))
            return Version(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating version") from re
