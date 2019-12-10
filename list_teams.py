import sys
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/srcclr/v3"
headers = {"User-Agent": "List Teams Example"}
# You can also filter with a parameter name and also sort by either name (default) or id

if __name__ == "__main__":

    try:
        response = requests.get(api_base + "/teams", auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
    except requests.RequestException as e:
        print("Failed...")
        print(e)
        sys.exit(1)

    if response.ok:
        data = response.json()

        for tms in data["_embedded"]["teams"]:
           print (tms["name"] + " --- " + tms["id"])
    else:
        print(response.status_code)
