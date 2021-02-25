import json

from pyopenproject import model as att
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import PostCommand


class AddAttachment(PostCommand):

    def __init__(self, connection, post, attachment, file_path):
        super().__init__(connection)
        self.post = post
        self.attachment = attachment
        with open(file_path, 'rb') as f:
            self.file_content = f.read()

    def execute(self):
        try:
            metadata = {"fileName": self.attachment.fileName, "description": {"raw": self.attachment.description}}
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}/{self.post.id}/attachments",
                                   files={'file': ('attachment', self.file_content),
                                          'metadata': (None, json.dumps(metadata))
                                          }).execute()
            return att.Attachment(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating attachment : {self.attachment.fileName}") from re
