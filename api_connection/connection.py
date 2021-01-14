import yaml
import requests
from requests.auth import HTTPBasicAuth

from api_connection.exceptions.request_exception import RequestError


class Connection:

    def __init__(self):
        with open("../config.yml", "r") as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

        self.url_base = cfg["api_conn"]["host"] + ":" + str(cfg["api_conn"]["port"])
        self.api_user = cfg["api_conn"]["user"]
        self.api_key = cfg["api_conn"]["password"]

    def __int__(self, url, user, password):
        self.url_base = url
        self.api_user = user
        self.api_key = password

    def get(self, context):
        try:
            response = requests.get(
                self.url_base + context,
                auth=HTTPBasicAuth(self.api_user, self.api_key)
            )
            return response.json()
        except requests.exceptions.Timeout as err:
            # Maybe set up for a retry, or continue in a retry loop
            raise RequestError(f"Timeout running GET with the URL: '{self.url_base + context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.TooManyRedirects as err:
            # Tell the user their URL was bad and try a different one
            raise RequestError(f"Error running GET with the URL: '{self.url_base + context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.RequestException as err:
            # catastrophic error. bail.
            raise SystemExit(err) from err
        except requests.exceptions.HTTPError as err:
            # The response was an http error.
            raise SystemExit(err) from err

    def post(self, context, body):
        try:
            response = requests.post(
                self.url_base + context,
                auth=HTTPBasicAuth(self.api_user, self.api_key),
                body=body
            )
            return response.json()
        except requests.exceptions.Timeout as err:
            # Maybe set up for a retry, or continue in a retry loop
            raise RequestError(f"Timeout running POST with the URL: '{self.url_base + context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.TooManyRedirects as err:
            # Tell the user their URL was bad and try a different one
            raise RequestError(f"Error running POST with the URL: '{self.url_base + context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.RequestException as err:
            # catastrophic error. bail.
            raise SystemExit(err)
        except requests.exceptions.HTTPError as err:
            # The response was an http error.
            raise SystemExit(err)

    def delete(self, context):
        try:
            response = requests.delete(
                self.url_base + context,
                auth=HTTPBasicAuth(self.api_user, self.api_key)
            )
            return response.json()
        except requests.exceptions.Timeout as err:
            # Maybe set up for a retry, or continue in a retry loop
            raise RequestError(f"Timeout running DELETE with the URL: '{self.url_base + context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.TooManyRedirects as err:
            # Tell the user their URL was bad and try a different one
            raise RequestError(f"Error running DELETE with the URL: '{self.url_base + context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.RequestException as err:
            # catastrophic error. bail.
            raise SystemExit(err)
        except requests.exceptions.HTTPError as err:
            # The response was an http error.
            raise SystemExit(err)

    def put(self, context, body):
        try:
            response = requests.put(
                self.url_base + context,
                auth=HTTPBasicAuth(self.api_user, self.api_key),
                body=body
            )
            return response.json()
        except requests.exceptions.Timeout as err:
            # Maybe set up for a retry, or continue in a retry loop
            raise RequestError(f"Timeout running PUT with the URL: '{self.url_base + context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.TooManyRedirects as err:
            # Tell the user their URL was bad and try a different one
            raise RequestError(f"Error running PUT with the URL: '{self.url_base + context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.RequestException as err:
            # catastrophic error. bail.
            raise SystemExit(err)
        except requests.exceptions.HTTPError as err:
            # The response was an http error.
            raise SystemExit(err)

    def patch(self, context, body):
        try:
            response = requests.patch(
                self.url_base + context,
                auth=HTTPBasicAuth(self.api_user, self.api_key),
                body=body
            )
            return response.json()
        except requests.exceptions.Timeout as err:
            # Maybe set up for a retry, or continue in a retry loop
            raise RequestError(f"Timeout running PATCH with the URL: '{self.url_base + context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.TooManyRedirects as err:
            # Tell the user their URL was bad and try a different one
            raise RequestError(f"Error running PATCH with the URL: '{self.url_base + context}'." +
                               f"\n {response.text}") from err
        except requests.exceptions.RequestException as err:
            # catastrophic error. bail.
            raise SystemExit(err)
        except requests.exceptions.HTTPError as err:
            # The response was an http error.
            raise SystemExit(err)
