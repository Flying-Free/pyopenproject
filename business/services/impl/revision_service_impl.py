from business.services.impl.command.revision.find import Find
from business.services.impl.command.revision.find_by_context import FindByContext
from business.services.revision_service import RevisionService


class RevisionServiceImpl(RevisionService):

    def find(self, revision):
        return Find(revision).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()
