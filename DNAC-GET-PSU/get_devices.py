import requests
import json
import argparse


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

def get_all_devices(DNAC_IP, headers, limit=500):
    DNAC_GET_DEVICE_URL = f"https://{DNAC_IP}/dna/intent/api/v1/network-device"

    all_devices = []
    offset = 1

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
    
    return (all_devices)

# Usage:
# Assuming you have DNAC_IP and headers defined
all_devices_data = get_all_devices(DNAC_IP, headers, )
#print(all_devices_data)
#print(len(all_devices_data))

