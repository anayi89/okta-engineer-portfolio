import requests

url = "OKTA_ORG_URL"
api_key = "OKTA_ADMIN_KEY"
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