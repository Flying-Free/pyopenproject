from model.connection import Connection
from api_connection.exceptions.request_exception import RequestError
from business.exception.business_error import BusinessError
from business.services.impl.command.group.group_command import GroupCommand
from model.group import Group


class Find(GroupCommand):

    def __init__(self, group):
        self.group = group

    def execute(self):
        try:
            json_obj = Connection().get(f"{self.CONTEXT}/{self.group.id}")
            return Group(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error finding group by id: {self.group.id}") from re
