from business.services.impl.command.query.create import Create
from business.services.impl.command.query.create_form import CreateForm
from business.services.impl.command.query.delete import Delete
from business.services.impl.command.query.find import Find
from business.services.impl.command.query.find_all import FindAll
from business.services.impl.command.query.schema import Schema
from business.services.impl.command.query.star import Star
from business.services.impl.command.query.unstar import Unstar
from business.services.impl.command.query.update import Update
from business.services.query_service import QueryService


class QueryServiceImpl(QueryService):

    def update(self, query):
        return Update(query).execute()

    def find(self, query, offset, pageSize, filters, columns, sortBy, groupBy, showSums, timelineVisible,
             timelineLabels, timelineZoomLevel, highlightingMode, highlightedAttributes, showHierarchies):
        return Find(query, offset, pageSize, filters, columns, sortBy, groupBy, showSums, timelineVisible,
                    timelineLabels, timelineZoomLevel, highlightingMode, highlightedAttributes,
                    showHierarchies).execute()

    def delete(self, query):
        return Delete(query).execute()

    def star(self, query):
        return Star(query).execute()

    def unstar(self, query):
        return Unstar(query).execute()

    def find_all(self, filters):
        return FindAll(filters).execute()

    def create(self, query):
        return Create(query).execute()

    def create_form(self, form):
        return CreateForm(form).execute()

    def schema(self):
        return Schema().execute()
