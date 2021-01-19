import model.attachment as att
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.post.post_command import PostCommand


class ListAttachments(PostCommand):

    def __init__(self, connection, post):
        super().__init__(connection)
        self.post = post

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.post.id}/attachments").execute()
            for attachment in json_obj["_embedded"]["elements"]:
                yield att.Attachment(attachment)
        except RequestError as re:
            raise BusinessError(f"Error getting the list of attachments of the post: {self.post.subject}") from re
