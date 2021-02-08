import json

import model.user as usr
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.patch_request import PatchRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.user.user_command import UserCommand


class Update(UserCommand):

    def __init__(self, connection, user):
        super().__init__(connection)
        self.user = user

    def execute(self):
        try:
            json_obj = PatchRequest(connection=self.connection,
                                    context=f"{self.CONTEXT}/{self.user.id}",
                                    json=self.user.__dict__,
                                    headers={"Content-Type": "application/json"}
                                    ).execute()
            return usr.User(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating user by id: {self.user.id}") from re
