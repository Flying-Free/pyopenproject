import json

import model.attachment as att
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.post.post_command import PostCommand


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
