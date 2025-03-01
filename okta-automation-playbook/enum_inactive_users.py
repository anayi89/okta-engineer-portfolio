import requests

url = "https://dev-67574834.okta.com"
api_key = "00PgT4QKqojJlkVaSc-0cb1ZzO0PF7DwriMPQShNbB"
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