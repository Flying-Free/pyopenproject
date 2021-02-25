from pyopenproject.business import AttachmentService
from pyopenproject.business.services.impl.command import Create
from pyopenproject.business.services.impl.command import Delete
from pyopenproject.business.services.impl.command import DownloadByContext
from pyopenproject.business.services.impl.command import Find


class AttachmentServiceImpl(AttachmentService):

    def __init__(self, connection):
        super().__init__(connection)

    def create(self, filename, description, file_path):
        return Create(self.connection, filename, description, file_path).execute()

    def delete(self, attachment):
        return Delete(self.connection, attachment).execute()

    def find(self, attachment):
        return Find(self.connection, attachment).execute()

    def download_by_context(self, attachment, folder):
        return DownloadByContext(self.connection, attachment, folder).execute()
