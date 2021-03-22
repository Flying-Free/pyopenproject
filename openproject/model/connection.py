import json


class Connection:
    """
    Class Configuration,
    represents the connection realized with the web application
    """
    def __init__(self, url, apikey, user=None):
        """Constructor for class Connection
        :param url: The application url
        :param apikey: The apikey
        :param user: The user (optional)
        """
        self.url_base = url
        self.api_user = "apikey" if user is None else user
        self.api_key = apikey

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
