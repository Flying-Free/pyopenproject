from business.services.impl.command.previewing.to_markdown import ToMarkdown
from business.services.impl.command.previewing.to_markdown_by_context import ToMarkdownByContext
from business.services.impl.command.previewing.to_plain import ToPlain
from business.services.previewing_service import PreviewingService


class PreviewingServiceImpl(PreviewingService):

    def __init__(self, connection):
        super().__init__(connection)

    def to_markdown(self, text):
        return ToMarkdown(self.connection, text).execute()

    def to_markdown_by_context(self, context, text):
        return ToMarkdownByContext(self.connection, context, text).execute()

    def to_plain(self, context, text):
        return ToPlain(self.connection, context, text).execute()
