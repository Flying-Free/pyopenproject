from business.services.impl.activity_service_impl import ActivityServiceImpl
from business.services.impl.attachment_service_impl import AttachmentServiceImpl
from business.services.impl.budget_service_impl import BudgetServiceImpl
from business.services.impl.category_service_impl import CategoryServiceImpl
from business.services.impl.configuration_service_impl import ConfigurationServiceImpl
from business.services.impl.custom_action_service_impl import CustomActionServiceImpl
from business.services.impl.custom_object_service_impl import CustomObjectServiceImpl
from business.services.impl.grid_service_impl import GridServiceImpl
from business.services.impl.group_service_impl import GroupServiceImpl
from business.services.impl.help_texts_service_impl import HelpTextsServiceImpl
from business.services.impl.membership_service_impl import MembershipServiceImpl
from business.services.impl.priority_service_impl import PriorityServiceImpl
from business.services.impl.project_service_impl import ProjectServiceImpl
from business.services.impl.relation_service_impl import RelationServiceImpl
from business.services.impl.revision_service_impl import RevisionServiceImpl
from business.services.impl.role_service_impl import RoleServiceImpl
from business.services.impl.schema_service_impl import SchemaServiceImpl
from business.services.impl.status_service_impl import StatusServiceImpl
from business.services.impl.time_entry_service_impl import TimeEntryServiceImpl
from business.services.impl.type_service_impl import TypeServiceImpl
from business.services.impl.user_service_impl import UserServiceImpl
from business.services.impl.version_service_impl import VersionServiceImpl
from business.services.impl.work_package_service_impl import WorkPackageServiceImpl
from model.connection import Connection


class ServiceFactory:

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

    def get_grid_service(self):
        return GridServiceImpl(self.conn)

    def get_group_service(self):
        return GroupServiceImpl(self.conn)

    def get_help_texts_service(self):
        return HelpTextsServiceImpl(self.conn)

    def get_membership_service(self):
        return MembershipServiceImpl(self.conn)

    def get_priority_service(self):
        return PriorityServiceImpl(self.conn)

    def get_project_service(self):
        return ProjectServiceImpl(self.conn)

    def get_relation_service(self):
        return RelationServiceImpl(self.conn)

    def get_revision_service(self):
        return RevisionServiceImpl(self.conn)

    def get_role_service(self):
        return RoleServiceImpl(self.conn)

    def get_schema_service(self):
        return SchemaServiceImpl(self.conn)

    def get_status_service(self):
        return StatusServiceImpl(self.conn)

    def get_time_entry_service(self):
        return TimeEntryServiceImpl(self.conn)

    def get_type_service(self):
        return TypeServiceImpl(self.conn)

    def get_user_service(self):
        return UserServiceImpl(self.conn)

    def get_version_service(self):
        return VersionServiceImpl(self.conn)

    def get_work_package_service(self):
        return WorkPackageServiceImpl(self.conn)
