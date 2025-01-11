import requests

from utils.helper import Helper
from services.users.payloads import Payloads
from services.users.endpoints import Endpoint
from config.headers import Headers
from services.users.models.user_model import UserModel, AllUserModel


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
        assert response.status_code == 200, response.json()
        model = UserModel(**response.json())
        return model


    def get_all_users(self):
        response = requests.get(
            url=self.endpoints.get_all_users,
            headers=self.headers.create_users,
        )
        assert response.status_code == 200, response.json()
        model = AllUserModel(**response.json())
        return model

    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.create_users,
        )
        assert response.status_code == 200, response.json()
        model = UserModel(**response.json())
        return model








