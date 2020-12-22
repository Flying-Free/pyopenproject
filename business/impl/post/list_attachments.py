from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.post.post_command import PostCommand


class ListAttachments(PostCommand):

    def __init__(self, context, identifier):
        self.context = context
        self.identifier = identifier

    def execute(self):
        try:
            Connection().get(f"{self.context}/{self.identifier}/attachments")
        except RequestError as re:
            raise BusinessError(f"Error downloading attachment by context: {self.context}") from re
