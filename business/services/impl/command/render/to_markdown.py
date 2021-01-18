from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.render.render_command import RenderCommand


class ToMarkdown(RenderCommand):

    def __init__(self, connection, text):
        super().__init__(connection)
        self.text = text

    def execute(self):
        try:
            return PostRequest(connection=self.connection,
                               context=f"{self.CONTEXT}/markdown",
                               json=self.text).execute()
        except RequestError as re:
            raise BusinessError(f"Error transform text to markdown: {self.text}") from re
