from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import GetRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import PostCommand
from pyopenproject.model import Post


class Find(PostCommand):

    def __init__(self, connection, post):
        super().__init__(connection)
        self.post = post

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}/{self.post.id}").execute()
            return Post(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding post by id: {self.post.id}") from re
