from business.impl.attachment.download_by_context import DownloadByContext
from business.impl.post.add_attachment import AddAttachment
from business.impl.post.list_attachments import ListAttachments


class PostServiceImpl(PostService):

    def list_attachments(self, context, identifier, body):
        return ListAttachments(context, identifier, body).execute()

    def add_attachment(self, context, identifier, body):
        return AddAttachment(context, identifier, body).execute()
