from business.revision_service import RevisionService


class RevisionServiceImpl(RevisionService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
