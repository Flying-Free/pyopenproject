from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.post_request import PostRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.previewing.previewing_command import PreviewingCommand


class FromPlain(PreviewingCommand):

    def __init__(self, connection, text):
        super().__init__(connection)
        self.text = text

    def execute(self):
        try:
            return PostRequest(connection=self.connection,
                               context=f"{self.CONTEXT}/plain",
                               data=self.text,
                               headers={'Content-Type': 'text/plain'}).execute()
        except RequestError as re:
            raise BusinessError(f"Error transform text to markdown: {self.text}") from re
