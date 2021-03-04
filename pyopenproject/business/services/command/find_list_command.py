from pyopenproject.api_connection.requests.get_request import GetRequest
from pyopenproject.business.services.command.command import Command


class FindListCommand(Command):

    def __init__(self, connection, request, class_type):
        self.connection = connection
        self.request = request
        self.class_type = class_type

    def execute(self):
        return self.next_page_objects(obj_list=[], json_obj=self.request.execute())

    def next_page_objects(self, obj_list, json_obj):
        for obj in json_obj["_embedded"]["elements"]:
            obj_list.append(self.class_type(obj))

        if 'nextByOffset' in json_obj["_links"]:
            json_obj = GetRequest(self.connection, json_obj["_links"]["nextByOffset"]["href"]).execute()
            self.next_page_objects(obj_list, json_obj)
        return obj_list
