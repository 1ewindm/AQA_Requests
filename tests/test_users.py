from config.base_test import BaseTest
import os
from dotenv import load_dotenv
load_dotenv()

class TestUser(BaseTest):

    def test_create_users(self):
        self.api_users.create_user()

