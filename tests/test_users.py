from config.base_test import BaseTest
import os
from dotenv import load_dotenv
load_dotenv()

class TestUser(BaseTest):

    def test_create_users(self):
        new_user = self.api_users.create_user()
        all_users_list = self.api_users.get_all_users()
        assert new_user in all_users_list.users
        created_user = self.api_users.get_user_by_id(new_user.uuid)
        print(created_user)













