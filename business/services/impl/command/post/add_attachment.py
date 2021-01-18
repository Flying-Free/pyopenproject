import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.post.post_command import PostCommand


class AddAttachment(PostCommand):

    def __init__(self, connection, post, attachment):
        super().__init__(connection)
        self.post = post
        self.attachment = attachment

    def execute(self):
        try:
            PostRequest(connection=self.connection,
                        context=f"{self.CONTEXT}/{self.post.id}/attachments",
                        json=json.dumps(self.attachment.__dict__)).execute()
        except RequestError as re:
            raise BusinessError(f"Error adding new attachment: {self.attachment.title}") from re
