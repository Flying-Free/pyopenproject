from abc import abstractmethod
from json.decoder import JSONDecodeError

import requests
from api_connection.command import Command
from api_connection.exceptions.request_exception import RequestError


class Request(Command):

    def __init__(self, connection, context, json=None, files=None):
        self.connection = connection
        self.context = context
        self.json = json
        self.files = files

    def execute(self):
        try:
            response = self._execute_request()
            if response.json()["_type"] == "Error":
                raise RequestError(f"Error Identifier: {response.json()['errorIdentifier']}\n"
                                   f"Message: {response.json()['message']}")
            return response.json()
        except requests.exceptions.Timeout as err:
            # Maybe set up for a retry, or continue in a retry loop
            raise RequestError(f"Timeout running request with the URL: '{self.connection.url_base + self.context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.TooManyRedirects as err:
            # Tell the user their URL was bad and try a different one
            raise RequestError(f"Error running request with the URL: '{self.connection.url_base + self.context}'." +
                               f"\n {response.text}") from err
        # TODO: Traceback (most recent call last):
        #   File "C:\Users\apadiernafer\Documents\GitHub\python-openproject-api\api_connection\request.py", line 20, in execute
        #     if response.json()["_type"] == "Error":
        #   File "C:\Python39\lib\site-packages\requests\models.py", line 900, in json
        #     return complexjson.loads(self.text, **kwargs)
        #   File "C:\Python39\lib\json\__init__.py", line 346, in loads
        #     return _default_decoder.decode(s)
        #   File "C:\Python39\lib\json\decoder.py", line 337, in decode
        #     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
        #   File "C:\Python39\lib\json\decoder.py", line 355, in raw_decode
        #     raise JSONDecodeError("Expecting value", s, err.value) from None
        # json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
        except JSONDecodeError as err:
            raise RequestError(f"Error running request with the URL: '{self.connection.url_base + self.context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.RequestException as err:
            # catastrophic error. bail.
            raise SystemExit(err) from err
        except requests.exceptions.HTTPError as err:
            # The response was an http error.
            raise SystemExit(err) from err

    @abstractmethod
    def _execute_request(self): raise NotImplementedError
