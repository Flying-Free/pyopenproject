from business.services.impl.command.render.to_markdown import ToMarkdown
from business.services.impl.command.render.to_plain import ToPlain
from business.services.render_service import RenderService


class RenderServiceImpl(RenderService):

    # TODO: To review errors

    def __init__(self, connection):
        super().__init__(connection)

    def to_markdown(self, text):
        return ToMarkdown(self.connection, text).execute()

    def to_markdown_by_context(self, context, text):
        return ToMarkdown(self.connection, context, text).execute()

    def to_plain(self, context, text):
        return ToPlain(self.connection, context, text).execute()
