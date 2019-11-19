import sys
import json
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

# Workspace - 87ede3a7-941d-4442-beee-2e122de58f1d
# team- 84132

api_base = "https://api.veracode.com/srcclr/v3"
headers = {"User-Agent": "Create Workspace Example"}


if __name__ == "__main__":

    try:
        response = requests.put(api_base + "/workspaces/87ede3a7-941d-4442-beee-2e122de58f1d/teams/84132", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Failed...")
        print(e)
        sys.exit(1)

    if response.ok:
        print(response.status_code)

    else:
        print(response.status_code)
        print(response.content)
