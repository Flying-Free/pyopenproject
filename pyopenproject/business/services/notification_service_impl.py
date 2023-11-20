from pyopenproject.business.notification_service import NotificationService
from pyopenproject.business.services.command.notification.find_all import FindAll


class NotificationServiceImpl(NotificationService):

    def __init__(self, connection):
        """Constructor for class NotificationServiceImpl, from NotificationService

        :param connection: The connection data
        """
        super().__init__(connection)

    def find(self, notification_id):
        """
            Finds a notificacion by nofitication ID
        Args:
            notification_id (int): The notification that is searched by id
        """
        pass

    def find_all(self, offset=None, page_size=None, filters=None,
                 sort_by=None, group_by=None):
        """
        Returns a collection of notifications based on parameters

        Args:
            offset (int, optional): Page number inside the requested. Defaults to None.
            page_size (int, optional): Number of elements to display. Defaults to None.
            filters (str(JSON), optional): id | project | readIAN | reason | resourceId | resourceType. Defaults to None.
            sort_by (str(JSON), optional): id | reason | readIAn. Defaults to None.
            group_by (str, optional): _description_. Defaults to None.

        Returns:
            Notification: notificacion object with the results
        """
        return FindAll(self.connection, offset, page_size, filters, sort_by, group_by).execute()

    def read_all(filter=None):
        pass

    def unread_all(filter=None):
        pass

    def read_notification(notification_id=None):
        pass

    def unread_notification(notification_id=None):
        pass

    def unread_notification(notification_id=None):
        pass

    def find_notification_detail(
            notification_id=None, detail_id=None):
        pass
