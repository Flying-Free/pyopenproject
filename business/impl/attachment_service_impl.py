from business.attachment_service import AttachmentService
from business.impl.activity.find_by_context import FindByContext


class AttachmentServiceImpl(AttachmentService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
