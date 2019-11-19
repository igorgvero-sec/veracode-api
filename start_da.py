import sys
import json
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/was/configservice/v1"
headers = {"User-Agent": "Start DA Scan Example", 'Content-type': 'application/json'}


if __name__ == "__main__":

    try:
        contents = open('da_scan.json', 'rb').read()
    	print(contents)
	response = requests.post(api_base + "/analyses", auth=RequestsAuthPluginVeracodeHMAC(), data=contents, headers=headers)
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
