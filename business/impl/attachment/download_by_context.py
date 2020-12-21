from src.extract.api_connection.connection import Connection
from src.extract.api_connection.exceptions.request_exception import RequestError
from src.extract.business.exception.business_error import BusinessError
from src.extract.business.impl.attachment.attachment_command import AttachmentCommand


class DownloadByContext(AttachmentCommand):

    def __init__(self, context):
        self.context = context

    def execute(self):
        try:
            Connection().get(f"{self.context}")
        except RequestError as re:
            raise BusinessError(f"Error downloading attachment by context: {self.context}") from re
