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

# Enumerate all users
for i in range(user_num):
    user_id = users[i]["id"]
    user_login = users[i]["profile"]["login"]
    admin_roles = requests.get(url + "/api/v1/users/" + user_id + "/roles", headers=headers).json()
    admin_roles_num = len(admin_roles)
    # Enumerate all users' admin roles
    user_role = admin_roles[j]["label"]
    for j in range (admin_roles_num):
        print(user_login + ", " + user_role)