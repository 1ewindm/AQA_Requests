import os

HOST = "https://dev-gs.qa-playground.com/api/v1" #if os.environ ["STAGE"] == "qa" else "https://release-gs.qa-playground.com/api/v1"


class Endpoint:

    create_user = f"{HOST}/users"
    get_all_users = f"{HOST}/users"
    get_user_by_id = lambda self, uuid: f"{HOST}/users/{uuid}"