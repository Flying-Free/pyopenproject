import os

from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.attachment.attachment_command import AttachmentCommand


class DownloadByContext(AttachmentCommand):

    def __init__(self, connection, attachment, folder):
        """Constructor for class DownloadByContext, from AttachmentCommand.

        :param connection: The connection data
        :param attachment: The attachment to download
        :param folder: The destination folder
        """
        super().__init__(connection)
        self.attachment = attachment
        self.folder = folder

    def execute(self):
        try:
            file_content = GetRequest(
                self.connection,
                f'{self.attachment.__dict__["_links"]["downloadLocation"]["href"]}').execute()
            filename = f"{self.folder}/{self.attachment.fileName}"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "wb") as f:
                f.write(file_content)

            return file_content
        except RequestError as re:
            raise BusinessError(f"Error downloading attachment by context: {self.CONTEXT}") from re
