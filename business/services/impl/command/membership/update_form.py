from contextlib import suppress

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.membership.membership_command import MembershipCommand
from model.form import Form


class UpdateForm(MembershipCommand):

    def __init__(self, connection, membership):
        super().__init__(connection)
        self.membership = membership

    def execute(self):
        try:
            membership_id = self.membership.id
            self.__remove_readonly_attributes()
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/{membership_id}/form",
                                   json=self.membership.__dict__).execute()
            return Form(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating membership form") from re

    def __remove_readonly_attributes(self):
        with suppress(KeyError):
            del self.membership.__dict__["_type"]
        with suppress(KeyError):
            del self.membership.__dict__["id"]
        with suppress(KeyError):
            del self.membership.__dict__["createdAt"]
        with suppress(KeyError):
            del self.membership.__dict__["updatedAt"]
        # with suppress(KeyError):
        #     del self.membership.__dict__["_embedded"]
        # with suppress(KeyError):
        #     del self.membership.__dict__["_links"]["self"]
        # with suppress(KeyError):
        #     del self.membership.__dict__["_links"]["schema"]
        # with suppress(KeyError):
        #     del self.membership.__dict__["_links"]["update"]
        # with suppress(KeyError):
        #     del self.membership.__dict__["_links"]["updateImmediately"]
