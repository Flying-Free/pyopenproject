import json
import os

from pyopenproject import model as att
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import AttachmentCommand


class Create(AttachmentCommand):

    def __init__(self, connection, filename, description, file_path):
        """Constructor for class Create, from AttachmentCommand.

        :param connection: The connection data
        :param filename: The name of the file
        :param description: The attachment description
        :param file_path: The path to the file
        """
        super().__init__(connection)
        self.filename = filename
        self.description = description
        with open(file=file_path, mode='rb') as f:
            self.file_content = f.read()
            self.file_path = os.path.abspath(f.name)

    def execute(self):
        try:
            metadata = {"fileName": self.filename, "description": {"raw": self.description}}
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}",
                                   files={
                                       'file': ('attachment', self.file_content),
                                       'metadata': (None, json.dumps(metadata))
                                   }
                                   ).execute()
            return att.Attachment(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating attachment : {self.filename}") from re
