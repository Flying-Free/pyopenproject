from business.attachment_service import AttachmentService
from business.impl.command.attachment.download_by_context import DownloadByContext


class AttachmentServiceImpl(AttachmentService):

    def download_by_context(self, context):
        return DownloadByContext(context).execute()
