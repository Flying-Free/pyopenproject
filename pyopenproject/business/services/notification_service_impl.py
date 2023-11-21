from pyopenproject.business.notification_service import NotificationService
from pyopenproject.business.services.command.notification.find_all import FindAll
from pyopenproject.business.services.command.notification.find import Find
from pyopenproject.business.services.command.notification.read_all import ReadAll
from pyopenproject.business.services.command.notification.unread_all import UnReadAll
from pyopenproject.business.services.command.notification.read import Read
from pyopenproject.business.services.command.notification.unread import UnRead

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
        return Find(self.connection, notification_id).execute()

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

    def read_all(self, filters=None):
        """
        Marks the whole notification collection as read. The collection contains only elements the authenticated user can see, and can be further reduced with filters.
        Args:
            filters (dict(JSON), optional): Filters. Defaults to None.

        Returns:
            str: If the resource was created returns the response (204), else throw an error
        """
        return ReadAll(self.connection, filters).execute()

    def unread_all(self, filters=None):
        """
        Marks the whole notification collection as unread. The collection contains only elements the authenticated user can see, and can be further reduced with filters.
        Args:
            filters (list, optional): A list of dictionaries of filtres. Defaults to None.

        Returns:
            _type_: _description_
        """
        return UnReadAll(self.connection, filters).execute()

    def read_notification(notification_id=None, filters=None):
        """
        Marks the given notification as read.
        Args:
            notification_id (integer, optional): _description_. Defaults to None.
            filters (list, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        return Read(self.connection, notification_id, filters)

    def unread_notification(notification_id=None):
        """

        Args:
            notification_id (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        return UnRead(self.connection, notification_id, filters)

    def find_notification_detail(
            notification_id=None, detail_id=None):
        pass
