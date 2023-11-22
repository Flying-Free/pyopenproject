from abc import ABCMeta, abstractmethod

from pyopenproject.business.abstract_service import AbstractService


class NotificationService(AbstractService):
    """
    Class Notification service
    implements all notification services
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        super().__init__(connection)

    @abstractmethod
    def find(self, notification_id): raise NotImplementedError

    @abstractmethod
    def find_all(self, offset=None, page_size=None, filters=None,
                 sort_by=None, group_by=None): raise NotImplementedError

    @abstractmethod
    def read_all(filter=None): raise NotImplementedError

    @abstractmethod
    def unread_all(filter=None): raise NotImplementedError

    @abstractmethod
    def read_notification(notification_id=None): raise NotImplementedError

    @abstractmethod
    def unread_notification(notification_id=None): raise NotImplementedError

    @abstractmethod
    def unread_notification(notification_id=None): raise NotImplementedError

    @abstractmethod
    def find_notification_detail(
        notification_id=None, detail_id=None): raise NotImplementedError
