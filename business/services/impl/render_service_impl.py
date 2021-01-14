from business.services.impl.command.render.to_markdown import ToMarkdown
from business.services.impl.command.render.to_plain import ToPlain
from business.services.render_service import RenderService


class DocumentServiceImpl(RenderService):

    def to_markdown(self, text):
        return ToMarkdown(text).execute()

    def to_markdown_by_context(self, context, text):
        return ToMarkdown(context, text).execute()

    def to_plain(self, context):
        return ToPlain(context).execute()
