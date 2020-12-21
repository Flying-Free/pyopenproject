from business.impl.work_package.find_all import FindAll
from business.impl.work_package.find_by_context import FindByContext
from business.impl.work_package.find_by_id import FindById
from business.version_service import VersionService


class VersionServiceImpl(VersionService):

    def find_all(self):
        return FindAll().execute

    def find_by_id(self, identifier):
        return FindById(self.identifier).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()

    # TODO: Review what params we need to create a new version
    def new_version(self): raise NotImplementedError
