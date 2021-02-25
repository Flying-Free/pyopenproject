from business.services.category_service import CategoryService
from business.services.impl.command.category.find import Find
from business.services.impl.command.category.find_by_context import FindByContext


class CategoryServiceImpl(CategoryService):

    def __init__(self, connection):
        super().__init__(connection)

    def find(self, category):
        return Find(self.connection, category).execute()

    def find_by_context(self, context):
        return FindByContext(self.connection, context).execute()
