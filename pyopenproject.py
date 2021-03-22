from src.business.services.activity_service_impl import ActivityServiceImpl
from src.business.services.attachment_service_impl import AttachmentServiceImpl
from src.business.services.budget_service_impl import BudgetServiceImpl
from src.business.services.category_service_impl import CategoryServiceImpl
from src.business.services.configuration_service_impl import ConfigurationServiceImpl
from src.business.services.custom_action_service_impl import CustomActionServiceImpl
from src.business.services.custom_object_service_impl import CustomObjectServiceImpl
from src.business.services.document_service_impl import DocumentServiceImpl
from src.business.services.grid_service_impl import GridServiceImpl
from src.business.services.group_service_impl import GroupServiceImpl
from src.business.services.help_texts_service_impl import HelpTextsServiceImpl
from src.business.services.membership_service_impl import MembershipServiceImpl
from src.business.services.news_service_impl import NewsServiceImpl
from src.business.services.post_service_impl import PostServiceImpl
from src.business.services.previewing_service_impl import PreviewingServiceImpl
from src.business.services.principal_service_impl import PrincipalServiceImpl
from src.business.services.priority_service_impl import PriorityServiceImpl
from src.business.services.project_service_impl import ProjectServiceImpl
from src.business.services.query_service_impl import QueryServiceImpl
from src.business.services.relation_service_impl import RelationServiceImpl
from src.business.services.revision_service_impl import RevisionServiceImpl
from src.business.services.role_service_impl import RoleServiceImpl
from src.business.services.root_service_impl import RootServiceImpl
from src.business.services.schema_service_impl import SchemaServiceImpl
from src.business.services.status_service_impl import StatusServiceImpl
from src.business.services.time_entry_service_impl import TimeEntryServiceImpl
from src.business.services.type_service_impl import TypeServiceImpl
from src.business.services.user_preferences_service_impl import UserPreferencesServiceImpl
from src.business.services.user_service_impl import UserServiceImpl
from src.business.services.version_service_impl import VersionServiceImpl
from src.business.services.wiki_page_service_impl import WikiPageServiceImpl
from src.business.services.work_package_service_impl import WorkPackageServiceImpl
from src.model.connection import Connection


class OpenProject:

    def __init__(self, url, api_key, user=None):
        self.conn = Connection(url=url, apikey=api_key) \
            if user is None \
            else Connection(url=url, user=user, apikey=api_key)

    def get_activity_service(self):
        return ActivityServiceImpl(self.conn)

    def get_attachment_service(self):
        return AttachmentServiceImpl(self.conn)

    def get_budget_service(self):
        return BudgetServiceImpl(self.conn)

    def get_category_service(self):
        return CategoryServiceImpl(self.conn)

    def get_configuration_service(self):
        return ConfigurationServiceImpl(self.conn)

    def get_custom_action_service(self):
        return CustomActionServiceImpl(self.conn)

    def get_custom_object_service(self):
        return CustomObjectServiceImpl(self.conn)

    def get_document_service(self):
        return DocumentServiceImpl(self.conn)

    def get_grid_service(self):
        return GridServiceImpl(self.conn)

    def get_group_service(self):
        return GroupServiceImpl(self.conn)

    def get_help_texts_service(self):
        return HelpTextsServiceImpl(self.conn)

    def get_membership_service(self):
        return MembershipServiceImpl(self.conn)

    def get_news_service(self):
        return NewsServiceImpl(self.conn)

    def get_post_service(self):
        return PostServiceImpl(self.conn)

    def get_previewing_service(self):
        return PreviewingServiceImpl(self.conn)

    def get_principal_service(self):
        return PrincipalServiceImpl(self.conn)

    def get_priority_service(self):
        return PriorityServiceImpl(self.conn)

    def get_project_service(self):
        return ProjectServiceImpl(self.conn)

    def get_query_service(self):
        return QueryServiceImpl(self.conn)

    def get_relation_service(self):
        return RelationServiceImpl(self.conn)

    def get_revision_service(self):
        return RevisionServiceImpl(self.conn)

    def get_role_service(self):
        return RoleServiceImpl(self.conn)

    def get_root_service(self):
        return RootServiceImpl(self.conn)

    def get_schema_service(self):
        return SchemaServiceImpl(self.conn)

    def get_status_service(self):
        return StatusServiceImpl(self.conn)

    def get_time_entry_service(self):
        return TimeEntryServiceImpl(self.conn)

    def get_type_service(self):
        return TypeServiceImpl(self.conn)

    def get_user_preferences_service(self):
        return UserPreferencesServiceImpl(self.conn)

    def get_user_service(self):
        return UserServiceImpl(self.conn)

    def get_version_service(self):
        return VersionServiceImpl(self.conn)

    def get_wiki_page_service(self):
        return WikiPageServiceImpl(self.conn)

    def get_work_package_service(self):
        return WorkPackageServiceImpl(self.conn)
