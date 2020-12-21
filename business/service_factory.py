from business.impl.activity_service_impl import ActivityServiceImpl
from business.impl.attachment_service_impl import AttachmentServiceImpl
from business.impl.category_service_impl import CategoryServiceImpl
from business.impl.custom_action_service_impl import CustomActionServiceImpl
from business.impl.custom_object_service_impl import CustomObjectServiceImpl
from business.impl.group_service_impl import GroupServiceImpl
from business.impl.membership_service_impl import MembershipServiceImpl
from business.impl.priority_service_impl import PriorityServiceImpl
from business.impl.project_service_impl import ProjectServiceImpl
from business.impl.relation_service_impl import RelationServiceImpl
from business.impl.revision_service_impl import RevisionServiceImpl
from business.impl.role_service_impl import RoleServiceImpl
from business.impl.schema_service_impl import SchemaServiceImpl
from business.impl.status_service_impl import StatusServiceImpl
from business.impl.time_entry_service_impl import TimeEntryServiceImpl
from business.impl.type_service_impl import TypeServiceImpl
from business.impl.user_service_impl import UserServiceImpl
from business.impl.version_service_impl import VersionServiceImpl
from business.impl.work_package_service_impl import WorkPackageServiceImpl


class ServiceFactory:

    @staticmethod
    def get_activity_service():
        return ActivityServiceImpl()

    @staticmethod
    def get_attachment_service():
        return AttachmentServiceImpl()

    @staticmethod
    def get_category_service():
        return CategoryServiceImpl()

    @staticmethod
    def get_custom_action():
        return CustomActionServiceImpl()

    @staticmethod
    def get_custom_object_service():
        return CustomObjectServiceImpl()

    @staticmethod
    def get_group_service():
        return GroupServiceImpl()

    @staticmethod
    def get_membership_service():
        return MembershipServiceImpl()

    @staticmethod
    def get_priority_service():
        return PriorityServiceImpl()

    @staticmethod
    def get_project_service():
        return ProjectServiceImpl()

    @staticmethod
    def get_relation_service():
        return RelationServiceImpl()

    @staticmethod
    def get_revision_service():
        return RevisionServiceImpl()

    @staticmethod
    def get_role_service():
        return RoleServiceImpl()

    @staticmethod
    def get_schema_service():
        return SchemaServiceImpl()

    @staticmethod
    def get_status_service():
        return StatusServiceImpl()

    @staticmethod
    def get_time_entry_service():
        return TimeEntryServiceImpl()

    @staticmethod
    def get_type_service():
        return TypeServiceImpl()

    @staticmethod
    def get_user_service():
        return UserServiceImpl()

    @staticmethod
    def get_version_service():
        return VersionServiceImpl()

    @staticmethod
    def get_work_package_service():
        return WorkPackageServiceImpl()
