# This version is original version only display the output.


import requests
import json
import argparse
import pandas as pd

from dnac_auth import authenticate, DNAC_IP


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Authenticate with Cisco DNA Center API')
    parser.add_argument('-username', required=True, help='Username for authentication')
    parser.add_argument('-password', required=True, help='Password for authentication')

    args = parser.parse_args()
    token = authenticate(args.username, args.password)  # Store the returned token

    if token:
        headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": token  # Use the obtained token in subsequent requests
        }




def get_powersupply(switch_id):
    DNAC_GET_PSU_URL = f"https://{DNAC_IP}/dna/intent/api/v1/network-device/{switch_id}/equipment?type=PowerSupply"
    response = requests.get(DNAC_GET_PSU_URL, headers=headers, verify=False)
    ###print(response.text)  # Debugging: See the raw response

    try:
        psus = json.loads(response.content).get("response", [])
        # Assuming 'response' is the correct key, adjust based on actual structure
    except json.JSONDecodeError:
        print("Failed to decode JSON response.")
        return

    
    if not isinstance(psus, list):
        print("Unexpected data structure for PSUs:", type(psus))
        return  # Exit if the structure is not what we expect

    for psu in psus:
        if 'productId' in psu and psu['productId'] != "":  
            #This line of code checks two things:
            #1. 'productId' is a key in the psu dictionary (i.e., the productId field exists).
            #2. The value associated with the productId key in the psu dictionary is an empty string ("").
            print(f"{psu['name']}")
            print(f"{psu['productId']}")
    print()




# Get all devices information all_devices
DNAC_GET_DEVICE_URL = f"https://{DNAC_IP}/dna/intent/api/v1/network-device"

all_devices = []
offset = 1
limit=500

while True:
    params = {
        'offset': offset,
        'limit': limit
    }
    response = requests.get(DNAC_GET_DEVICE_URL, headers=headers, params=params, verify=False)

    if response.status_code == 200:
        devices_data = response.json().get("response", [])
        if not devices_data:
            break  # No more devices to retrieve, exit the loop
        
        all_devices.extend(devices_data)
        offset += limit  # Increment the offset for the next request
    else:
        print(f"Failed to retrieve devices. Status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging
        break

# Get Switches from all_devices
switches = [all_device for all_device in all_devices if all_device['family'] == 'Switches and Hubs']


# Print the list of switches
for switch in switches:
    switch_id = f"{switch['id']}"
    print(f"#################")
    print(f"###{switch['hostname']}")
    print(f"#################")
    get_powersupply(switch_id)
