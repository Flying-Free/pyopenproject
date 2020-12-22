from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.status.status_command import StatusCommand
from model.status import Status


class FindById(StatusCommand):

    def __init__(self, identifier):
        self.identifier = identifier

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.identifier}")
            return Status(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding status by id: {self.identifier}") from re
