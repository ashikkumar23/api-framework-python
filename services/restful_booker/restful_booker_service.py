import json

from services.base_service import BaseClient
from config import BASE_URI
from utils.request import APIRequest


class RestfulBookerClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.base_url = BASE_URI
        self.request = APIRequest()

    def create_booking(self, payload):
        return self.request.post_request(
            self.base_url, json.dumps(payload), self.headers
        )

    def get_booking(self, booking_id):
        url = f"{BASE_URI}/{booking_id}"
        return self.request.get_request(url, self.headers)

    def update_booking(self, booking_id, payload):
        url = f"{BASE_URI}/{booking_id}"
        return self.request.put_request(
            url, json.dumps(payload), self.headers_with_basic_auth
        )

    def delete_booking(self, booking_id):
        url = f"{BASE_URI}/{booking_id}"
        return self.request.delete_request(url, self.headers_with_basic_auth)
