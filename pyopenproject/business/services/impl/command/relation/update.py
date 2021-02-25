from pyopenproject import model as rel
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PatchRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import RelationCommand


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
