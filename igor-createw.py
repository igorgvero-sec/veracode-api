import sys
import json
import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


api_base = "https://api.veracode.com/srcclr/v3"
headers = {"User-Agent": "Python HMAC Example"}


if __name__ == "__main__":

    try:
        contents = open('createw.json', 'rb').read()
    	print(contents)
	response = requests.post(api_base + "/workspaces", auth=RequestsAuthPluginVeracodeHMAC(), data=contents, headers=headers)
    except requests.RequestException as e:
        print("Failed...")
        print(e)
        sys.exit(1)

    if response.ok:
        #data = response.json()
        #print(data)
	#print(response)
        print(response.status_code)

    else:
        print(response.status_code)
