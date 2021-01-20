import json


class Connection:

    def __init__(self, url, apikey, user=None):
        self.url_base = url
        self.api_user = "apikey" if user is None else user
        self.api_key = apikey

    def __str__(self):
        return json.dumps(self.__dict__)
