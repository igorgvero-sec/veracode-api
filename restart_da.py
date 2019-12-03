import sys
import json
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/was/configservice/v1"
headers = {"User-Agent": "Restart DA Scan Example", 'Content-type': 'application/json'}


if __name__ == "__main__":

    try:
        contents = open('da_rescan.json', 'rb').read()
        print(contents)
        response = requests.put(api_base + "/analyses/294179c7084394f182fb6ec167f3d18e?method=PATCH", auth=RequestsAuthPluginVeracodeHMAC(), data=contents, headers=headers)
    except requests.RequestException as e:
        print("Failed...")
        print(e)
        sys.exit(1)

    if response.ok:
        print(response.status_code)
        print(response.content)

    else:
        print(response.status_code)
        print(response.content)