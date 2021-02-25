from pyopenproject.business.services.impl.command import Create
from pyopenproject.business.services.impl.command import CreateForm
from pyopenproject.business.services.impl.command import Delete
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import FindAll
from pyopenproject.business.services.impl.command import FindByContext
from pyopenproject.business.services.impl.command import Schema
from pyopenproject.business.services.impl.command import Star
from pyopenproject.business.services.impl.command import Unstar
from pyopenproject.business.services.impl.command import Update
from pyopenproject.business.services.query_service import QueryService


class QueryServiceImpl(QueryService):

    def __init__(self, connection):
        super().__init__(connection)

    def find_by_context(self, context):
        return FindByContext(connection=self.connection, context=context).execute()

    def update(self, query):
        return Update(self.connection, query).execute()

    def find(self, query, offset=None, page_size=None, filters=None, columns=None, sort_by=None, group_by=None,
             show_sums=None, timeline_visible=None, timeline_labels=None, timeline_zoom_level=None,
             highlighting_mode=None, highlighted_attributes=None, show_hierarchies=None):
        return Find(self.connection, query, offset, page_size, filters, columns, sort_by, group_by,
                    show_sums, timeline_visible, timeline_labels, timeline_zoom_level,
                    highlighting_mode, highlighted_attributes, show_hierarchies).execute()

    def delete(self, query):
        return Delete(self.connection, query).execute()

    def star(self, query):
        return Star(self.connection, query).execute()

    def unstar(self, query):
        return Unstar(self.connection, query).execute()

    def find_all(self, filters=None):
        return list(FindAll(self.connection, filters).execute())

    def create(self, query):
        return Create(self.connection, query).execute()

    def create_form(self, form):
        return CreateForm(self.connection, form).execute()

    def schema(self):
        return Schema(self.connection).execute()
