from business.category_service import CategoryService



class CategoryServiceImpl(CategoryService):

    def find_all(self):
        return FindAll().execute

    def find_by_id(self, identifier):
        return FindById(self.identifier).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()

    # TODO: Review what params we need to create a new category
    def new_category(self): raise NotImplementedError
