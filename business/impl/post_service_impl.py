from business.impl.command.post.add_attachment import AddAttachment
from business.impl.command.post.list_attachments import ListAttachments


class PostServiceImpl(PostService):

    def list_attachments(self, context, identifier, body):
        return ListAttachments(context, identifier, body).execute()

    def add_attachment(self, context, identifier, body):
        return AddAttachment(context, identifier, body).execute()
