import os
from base64 import b64encode

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class BaseClient:
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.headers_with_basic_auth = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"{self.basic_auth(os.environ.get('USERNAME'), os.environ.get('PASSWORD'))}",
        }

    @staticmethod
    def basic_auth(username, password):
        token = b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
        return f"Basic {token}"
