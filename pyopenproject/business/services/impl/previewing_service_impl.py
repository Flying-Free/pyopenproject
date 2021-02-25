from pyopenproject.business.services.impl.command import FromMarkdown
from pyopenproject.business.services.impl.command import FromPlain
from pyopenproject.business.services.previewing_service import PreviewingService


class PreviewingServiceImpl(PreviewingService):

    def __init__(self, connection):
        super().__init__(connection)

    def from_markdown(self, text, context=None):
        return FromMarkdown(self.connection, text, context).execute()

    def from_plain(self, text):
        return FromPlain(self.connection, text).execute()
