import requests
import json
import sys
sys.path.append(r'C:\Python\Repository\DNAC-AUTH')

# Load DNAC_IP and DNAC_TOKEN from dnac-auth
from dnac_auth import DNAC_IP, DNAC_TOKEN

# Define the request headers with the authentication token
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": DNAC_TOKEN
}

# Define Get device URL
DNAC_GET_DEVICE_URL = f"https://{DNAC_IP}/dna/intent/api/v1/network-device/count"

response = requests.request('GET', DNAC_GET_DEVICE_URL, headers=headers, verify=False)

print(response.text.encode('utf8'))



