from business.services.attachment_service import AttachmentService
from business.services.impl.command.attachment.create import Create
from business.services.impl.command.attachment.delete import Delete
from business.services.impl.command.attachment.download_by_context import DownloadByContext
from business.services.impl.command.attachment.find import Find
from business.services.impl.command.attachment.find_all import FindAll


class AttachmentServiceImpl(AttachmentService):

    def create(self, attachment):
        return Create(attachment).execute()

    def delete(self, attachment):
        return Delete(attachment).execute()

    def find(self, attachment):
        return Find(attachment).execute()

    def find_all(self):
        return FindAll().execute()

    def download_by_context(self, context):
        return DownloadByContext(context).execute()

