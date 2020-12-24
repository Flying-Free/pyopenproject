from api_connection.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.impl.command.post.post_command import PostCommand
from model.post import Post


class Find(PostCommand):

    def __init__(self, post):
        self.post = post

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.post.id}")
            return Post(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding post by id: {self.post.id}") from re
