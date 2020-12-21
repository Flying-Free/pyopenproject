from business.impl.work_package.find_all import FindAll
from business.impl.work_package.find_by_context import FindByContext
from business.impl.work_package.find_by_id import FindById
from business.work_package_service import WorkPackageService


class WorkPackageServiceImpl(WorkPackageService):

    def find_all(self):
        return FindAll().execute

    def find_by_id(self, identifier):
        return FindById(self.identifier).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()

    # TODO: Review what params we need to create a new work package
    def new_work_package(self): raise NotImplementedError
