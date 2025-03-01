import requests

url = "OKTA_ORG_URL"
api_key = "OKTA_ADMIN_KEY"
headers = {
    "Authorization": "SSWS " + api_key,
    "Accept": "application/json",
    "Content-Type": "application/json"
}
users = requests.get(url + "/api/v1/users", headers=headers).json()
user_num = len(users)

# Enumerate all users that do not have an "ACTIVE" status
for i in range(user_num):
    user_login = users[i]["profile"]["login"]
    user_status = users[i]["status"]
    if users[i]["status"] == "ACTIVE":
        print(user_login + ", " + user_status)