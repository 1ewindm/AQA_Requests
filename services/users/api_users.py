import requests

from utils.helper import Helper
from services.users.payloads import Payloads
from services.users.endpoints import Endpoint
from config.headers import Headers


class UsersAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoint()
        self.headers = Headers()



    def create_user(self):

        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.create_users,
            json=self.payloads.create_user
        )
        print(response.json())
        assert response.status_code == 200, response.json()
