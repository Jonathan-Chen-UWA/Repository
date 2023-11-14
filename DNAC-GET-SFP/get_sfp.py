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
DNAC_GET_DEVICE_URL = f"https://{DNAC_IP}/dna/intent/api/v1/network-device"
# print(DNAC_GET_DEVICE_URL)

# Send an HTTP GET request to the Cisco DNA Center APIs to get the list of switches
response = requests.get(DNAC_GET_DEVICE_URL, headers=headers, verify=False)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON to extract the list of switches
    switches = json.loads(response.content)["response"]

    # Print the list of switches
    for switch in switches:
        SWITCH_ID = f"{switch['id']}"
        print(f"{switch['hostname']} ({switch['managementIpAddress']}) id {SWITCH_ID}")
        


else:
    print(f"Failed to obtain the network device data. Status code: {response.status_code}")
    print(response.text)  # Print the response content for debugging




