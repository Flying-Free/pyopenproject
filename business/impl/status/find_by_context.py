from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.status.status_command import StatusCommand
from src.extract.model.status import Status


class FindByContext(StatusCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.context}")
            return Status(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding status by context: {self.context}") from re
