from business.services.impl.command.post.add_attachment import AddAttachment
from business.services.impl.command.post.find import Find
from business.services.impl.command.post.list_attachments import ListAttachments
from business.services.post_service import PostService


class PostServiceImpl(PostService):

    def __init__(self, connection):
        super().__init__(connection)

    def list_attachments(self, post):
        return ListAttachments(self.connection, post).execute()

    def add_attachment(self, post, attachment):
        return AddAttachment(self.connection, post, attachment).execute()

    def find(self, post):
        return Find(self.connection, post).execute()
