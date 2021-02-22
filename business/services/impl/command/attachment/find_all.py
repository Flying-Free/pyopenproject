import model.attachment as att
from business.services.impl.command.abstract_find_all import AbstractFindAll


class FindAll(AbstractFindAll):

    def __init__(self, connection):
        """
        Constructor for class DownloadByContext, from AttachmentCommand

        :param connection: The connection data
        """
        super().__init__(connection)

    def cast(self, endpoint):
        return att.Attachment(endpoint)

    def request_url(self):
        return f"{self.CONTEXT}"
