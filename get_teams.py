import sys
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/srcclr/v3"
headers = {"User-Agent": "Get Teams Example"}


if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/teams/84132", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Failed...")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()
        #for ts in data["_links"]:
        print (data["name"] + " --- " + data["id"])
    else:
        print(response.status_code)
