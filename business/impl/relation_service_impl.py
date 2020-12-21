from business.relation_service import RelationService

class RelationServiceImpl(RelationService):

    def find_by_context(self, context):
        return FindByContext(context).execute()
