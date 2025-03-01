import requests

url = "https://dev-67574834.okta.com"
api_key = "00PgT4QKqojJlkVaSc-0cb1ZzO0PF7DwriMPQShNbB"
headers = {
    "Authorization": "SSWS " + api_key,
    "Accept": "application/json",
    "Content-Type": "application/json"
}
apps = requests.get(url + "/api/v1/apps", headers=headers).json()
app_num = len(apps)

# Enumerate all apps by their IAM protocol (SAML, OIDC, etc.)
for i in range(app_num):
    print(apps[i]["name"] + ", " + apps[i]["signOnMode"])