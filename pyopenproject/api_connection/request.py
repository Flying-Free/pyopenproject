from abc import abstractmethod
from json.decoder import JSONDecodeError

import requests

from pyopenproject.api_connection.command import Command
from pyopenproject.api_connection.exceptions.request_exception import RequestError


class Request(Command):

    def __init__(self, connection, context, json=None, files=None, headers=None, data=None):
        """Constructor for class Request, from Command

        :param connection: The connection data
        :param context: The URL context for the request
        :param json: The JSON data
        :param files: The file/s to upload
        :param headers: The request headers
        :param data: The text/plain data
        """
        self.connection = connection
        self.headers = headers
        self.context = context
        self.json = json
        self.files = files
        self.data = data

    def execute(self):
        try:
            response = self._execute_request()
            response.raise_for_status()
            if response.content is not bytes():
                if 'application/hal+json' in response.headers['content-type']:
                    if response.json()["_type"] == "Error":
                        raise RequestError(f"Error Identifier: {response.json()['errorIdentifier']}\n"
                                           f"Message: {response.json()['message']}")
                    return response.json()
                elif 'image' in response.headers['Content-Type']:
                    return response.content
                elif 'text' in response.headers['Content-Type']:
                    return response.content.decode("utf-8")
        except requests.exceptions.Timeout as err:
            # Maybe set up for a retry, or continue in a retry loop
            raise RequestError(f"Timeout running request with the URL (Timeout):"
                               f" '{self.connection.url_base + self.context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.TooManyRedirects as err:
            # Tell the user their URL was bad and try a different one
            raise RequestError(f"Error running request with the URL (TooManyRedirects):"
                               f" '{self.connection.url_base + self.context}'." +
                               f"\n {response.text}") from err
        except JSONDecodeError as err:
            raise RequestError(f"Error running request with the URL (JSONDecodeError):"
                               f" '{self.connection.url_base + self.context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.HTTPError as err:
            # The response was an http error.
            raise RequestError(f"Error running request with the URL (HTTPError):"
                               f" '{self.connection.url_base + self.context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.RequestException as err:
            # catastrophic error. bail.
            raise SystemExit(err) from err

    @abstractmethod
    def _execute_request(self):
        raise NotImplementedError
