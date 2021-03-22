from pyopenproject.business.post_service import PostService
from pyopenproject.business.services.command.post.add_attachment import AddAttachment
from pyopenproject.business.services.command.post.find import Find
from pyopenproject.business.services.command.post.list_attachments import ListAttachments


class PostServiceImpl(PostService):

    def __init__(self, connection):
        super().__init__(connection)

    def list_attachments(self, post):
        return list(ListAttachments(self.connection, post).execute())

    def add_attachment(self, post, attachment, file_path):
        return AddAttachment(self.connection, post, attachment, file_path).execute()

    def find(self, post):
        return Find(self.connection, post).execute()
