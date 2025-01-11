import requests
from config.base_test import BaseTest

base = BaseTest()
HOST = "https://dev-gs.qa-playground.com/api/v1"

response = requests.post(
    url =f"{HOST}/setup",
    headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL215a290cWJvY2t6dnphY2NjdWJ6LnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJmMmNkYTc5OC1iNWRiLTRhOGItOTk1NC1jZDczOGI2MWZhODEiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzM3MDMzODA5LCJpYXQiOjE3MzY0MzM4MDksImVtYWlsIjoibGV3aW4uZG1pdHJ5MTFAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnaXRodWIiLCJwcm92aWRlcnMiOlsiZ2l0aHViIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2F2YXRhcnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3UvMTY0MzA4NDg2P3Y9NCIsImVtYWlsIjoibGV3aW4uZG1pdHJ5MTFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vYXBpLmdpdGh1Yi5jb20iLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6IjFld2luZG0iLCJwcm92aWRlcl9pZCI6IjE2NDMwODQ4NiIsInN1YiI6IjE2NDMwODQ4NiIsInVzZXJfbmFtZSI6IjFld2luZG0ifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTczNjQzMzgwOX1dLCJzZXNzaW9uX2lkIjoiZDBiOWQ5NTgtNjEwZC00OWNjLWEzYzAtZDViMTA1MjUzOTY5IiwiaXNfYW5vbnltb3VzIjpmYWxzZX0.ARRn6Uu6gJR0i0pkMmeUWoxJcTBWcVXe4epA074pQk8"}

)
print(response.status_code)

def test_add_new_user():
    # Step 1: Prepare request payload
    payload = {
        "email": "newuser@example.com",
        "password": "Password123",
        "name": "New User",
        "nickname": "newuser"
    }

    # Step 2: Send POST request to create a new user
    response = requests.post(f"{HOST}/users",
                             headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL215a290cWJvY2t6dnphY2NjdWJ6LnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJmMmNkYTc5OC1iNWRiLTRhOGItOTk1NC1jZDczOGI2MWZhODEiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzM3MDMzODA5LCJpYXQiOjE3MzY0MzM4MDksImVtYWlsIjoibGV3aW4uZG1pdHJ5MTFAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnaXRodWIiLCJwcm92aWRlcnMiOlsiZ2l0aHViIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2F2YXRhcnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3UvMTY0MzA4NDg2P3Y9NCIsImVtYWlsIjoibGV3aW4uZG1pdHJ5MTFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOi8vYXBpLmdpdGh1Yi5jb20iLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6IjFld2luZG0iLCJwcm92aWRlcl9pZCI6IjE2NDMwODQ4NiIsInN1YiI6IjE2NDMwODQ4NiIsInVzZXJfbmFtZSI6IjFld2luZG0ifSwicm9sZSI6ImF1dGhlbnRpY2F0ZWQiLCJhYWwiOiJhYWwxIiwiYW1yIjpbeyJtZXRob2QiOiJvYXV0aCIsInRpbWVzdGFtcCI6MTczNjQzMzgwOX1dLCJzZXNzaW9uX2lkIjoiZDBiOWQ5NTgtNjEwZC00OWNjLWEzYzAtZDViMTA1MjUzOTY5IiwiaXNfYW5vbnltb3VzIjpmYWxzZX0.ARRn6Uu6gJR0i0pkMmeUWoxJcTBWcVXe4epA074pQk8",
"X-Task-Id": "API-3"},
                             json=payload)
    assert response.status_code == 200
    print(response.json())

