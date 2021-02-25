from pyopenproject import model as rel
from pyopenproject.api_connection.exceptions import RequestError
from pyopenproject.api_connection.requests import PostRequest
from pyopenproject.business.exception import BusinessError
from pyopenproject.business.services.impl.command import RelationCommand


class UpdateForm(RelationCommand):

    def __init__(self, connection, relation, form):
        super().__init__(connection)
        self.relation = relation
        self.form = form

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=f"{self.CONTEXT}/{self.relation.id}/form",
                                   json=self.form).execute()
            return rel.Relation(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating form for relation {self.relation.name}") from re
