from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.render.render_command import RenderCommand


class ToMarkdownByContext(RenderCommand):

    def __init__(self, context, text):
        self.context = context
        self.text = text

    def execute(self):
        try:
            return Connection().post(f"{self.CONTEXT}/markdown?{self.context}", self.text)
        except RequestError as re:
            raise BusinessError(f"Error transform text to markdown: {self.text}") from re
