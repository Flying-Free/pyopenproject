from pyopenproject.openproject import OpenProject

A_KEY = "5a5eee010163426c5475191847949825467de6ecb148e44763661c9cc62e35b7"

op = OpenProject(url="http://192.168.102.178:8080", api_key=A_KEY)
user = op.get_notification_service().find_all()
print(user)
