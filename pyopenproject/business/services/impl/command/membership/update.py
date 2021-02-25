from contextlib import suppress

from pyopenproject import model as mem
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PatchRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import MembershipCommand


class Update(MembershipCommand):

    def __init__(self, connection, membership):
        super().__init__(connection)
        self.membership = membership

    def execute(self):
        try:
            membership_id = self.membership.id
            self.__remove_readonly_attributes()
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=f"{self.CONTEXT}/{membership_id}",
                                    json=self.membership.__dict__).execute()
            return mem.Membership(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating membership by id: {self.membership.id}") from re

    def __remove_readonly_attributes(self):
        with suppress(KeyError):
            del self.membership.__dict__["_type"]
        with suppress(KeyError):
            del self.membership.__dict__["id"]
        with suppress(KeyError):
            del self.membership.__dict__["createdAt"]
        with suppress(KeyError):
            del self.membership.__dict__["updatedAt"]
        with suppress(KeyError):
            del self.membership.__dict__["_links"]
