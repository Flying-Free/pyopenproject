from business.category_service import CategoryService
from business.impl.command.category.find import Find
from business.impl.command.category.find_by_context import FindByContext


class CategoryServiceImpl(CategoryService):

    def find(self, category):
        return Find(category).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()
