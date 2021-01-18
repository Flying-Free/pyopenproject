from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.attachment.attachment_command import AttachmentCommand


class DownloadByContext(AttachmentCommand):

    def __init__(self, connection, context):
        super().__init__(connection)
        self.context = context

    def execute(self):
        try:
            GetRequest(self.connection, f"{self.context}").execute()
        except RequestError as re:
            raise BusinessError(f"Error downloading attachment by context: {self.context}") from re
