import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.status.status_command import StatusCommand
from model.status import Status


class FindAll(StatusCommand):

    def __init__(self, connection):
        super().__init__(connection)

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}").execute()
            for tEntry in json.loads(json_obj):
                yield Status(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all statuses") from re
