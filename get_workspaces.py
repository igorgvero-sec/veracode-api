import sys
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/srcclr/v3"
headers = {"User-Agent": "Get Workspaces Example"}


if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/workspaces", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Failed...")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        for ws in data["_embedded"]["workspaces"]:
            print (ws["name"])
    else:
        print(response.status_code)
