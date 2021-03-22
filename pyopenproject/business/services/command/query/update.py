from contextlib import suppress

from pyopenproject.api_connection.exceptions.request_exception import RequestError
from pyopenproject.api_connection.requests.patch_request import PatchRequest
from pyopenproject.business.exception.business_error import BusinessError
from pyopenproject.business.services.command.query.query_command import QueryCommand
from pyopenproject.model.query import Query


class Update(QueryCommand):

    def __init__(self, connection, query):
        super().__init__(connection)
        self.query = query

    def execute(self):
        try:
            query_id = self.query.id
            self.__remove_readonly_attributes()
            json_obj = PatchRequest(connection=self.connection,
                                    headers={"Content-Type": "application/json"},
                                    context=f"{self.CONTEXT}/{query_id}",
                                    json=self.query.__dict__).execute()
            return Query(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error updating query by id: {self.query.id}") from re

    def __remove_readonly_attributes(self):
        with suppress(KeyError): del self.query.__dict__["_links"]["self"]
        with suppress(KeyError): del self.query.__dict__["_links"]["user"]
        with suppress(KeyError): del self.query.__dict__["_links"]["project"]
        with suppress(KeyError): del self.query.__dict__["_links"]["columns"]
        with suppress(KeyError): del self.query.__dict__["_links"]["highlightedAttributes"]
        with suppress(KeyError): del self.query.__dict__["_links"]["sortBy"]
        with suppress(KeyError): del self.query.__dict__["_links"]["groupBy"]
        with suppress(KeyError): del self.query.__dict__["_links"]["results"]
        with suppress(KeyError): del self.query.__dict__["_links"]["schema"]

        with suppress(KeyError): del self.query.__dict__["id"]
        with suppress(KeyError): del self.query.__dict__["name"]
        with suppress(KeyError): del self.query.__dict__["filters"]
        with suppress(KeyError): del self.query.__dict__["sums"]
        with suppress(KeyError): del self.query.__dict__["timelineVisible"]
        with suppress(KeyError): del self.query.__dict__["timelineLabels"]
        with suppress(KeyError): del self.query.__dict__["highlightingMode"]
        with suppress(KeyError): del self.query.__dict__["showHierarchies"]
        with suppress(KeyError): del self.query.__dict__["hidden"]
        with suppress(KeyError): del self.query.__dict__["public"]
        with suppress(KeyError): del self.query.__dict__["starred"]
        with suppress(KeyError): del self.query.__dict__["createdAt"]
        with suppress(KeyError): del self.query.__dict__["updatedAt"]
