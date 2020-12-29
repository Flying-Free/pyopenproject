import json

from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.status.status_command import StatusCommand
from model.status import Status


class FindAll(StatusCommand):

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}")
            for tEntry in json.loads(json_obj):
                yield Status(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all statuses") from re
