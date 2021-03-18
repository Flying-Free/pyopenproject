from contextlib import suppress

from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.patch_request import PatchRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.relation.relation_command import RelationCommand
from pyopenproject.model import relation as rel


class Update(RelationCommand):

    def __init__(self, connection, relation):
        super().__init__(connection)
        self.relation = relation

    def execute(self):
        try:
            relation_id = self.relation.id
            self.__remove_readonly_attributes()
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=f"{self.CONTEXT}/{relation_id}",
                                    json=self.relation.__dict__).execute()
            return rel.Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating relation by id: {relation_id}") from re

    def __remove_readonly_attributes(self):
        with suppress(KeyError): del self.relation.__dict__["_links"]["self"]
        with suppress(KeyError): del self.relation.__dict__["_links"]["schema"]
        with suppress(KeyError): del self.relation.__dict__["_links"]["from"]
        with suppress(KeyError): del self.relation.__dict__["_links"]["to"]
        with suppress(KeyError): del self.relation.__dict__["id"]
        with suppress(KeyError): del self.relation.__dict__["name"]
        with suppress(KeyError): del self.relation.__dict__["reverseType"]
