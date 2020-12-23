from business.impl.command.post.add_attachment import AddAttachment
from business.impl.command.post.list_attachments import ListAttachments
from business.post_service import PostService


class PostServiceImpl(PostService):

    def list_attachments(self, post):
        return ListAttachments(post).execute()

    def add_attachment(self, post, attachment):
        return AddAttachment(post, attachment).execute()
