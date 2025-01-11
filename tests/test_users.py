from config.base_test import BaseTest
import os
from dotenv import load_dotenv
load_dotenv()

class TestUser(BaseTest):

    def test_create_users(self):
        self.api_users.create_user()

    def test_get_all_users(self):
        self.api_users.get_all_users()

    def test_get_user_by_id(self):
        # new_user = self.api_users.create_user()
        all_users = self.api_users.get_all_users()
        user = all_users.users[0]
        self.api_users.get_user_by_id(user.uuid)


    def test_check_add_new_user_in_list(self):
        new_user = self.api_users.create_user()
        all_users_list = self.api_users.get_all_users()
        assert new_user in all_users_list.users















