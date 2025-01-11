import os
from dotenv import load_dotenv

load_dotenv()

class Headers:

    basic = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
    }
    create_users = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": f"{os.getenv('X_TASK_ID')}"
    }