from pyopenproject.business.services.impl.command import AddAttachment
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import ListAttachments
from pyopenproject.business.services.post_service import PostService


class PostServiceImpl(PostService):

    def __init__(self, connection):
        super().__init__(connection)

    def list_attachments(self, post):
        return list(ListAttachments(self.connection, post).execute())

    def add_attachment(self, post, attachment, file_path):
        return AddAttachment(self.connection, post, attachment, file_path).execute()

    def find(self, post):
        return Find(self.connection, post).execute()
