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
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=f"{self.CONTEXT}/{self.relation.id}",
                                    json=self.relation.__dict__).execute()
            return rel.Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating relation by id: {self.relation.id}") from re
