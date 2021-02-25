from pyopenproject.business import CategoryService
from pyopenproject.business.services.impl.command import Find
from pyopenproject.business.services.impl.command import FindByContext


class CategoryServiceImpl(CategoryService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, category):
        return Find(self.connection, category).execute()

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()
