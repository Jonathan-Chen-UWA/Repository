import requests
import json
import argparse
from dnac_auth import authenticate, DNAC_IP

def get_all_switches(DNAC_IP, headers, limit=500):
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

    switch_hostnames = [device['hostname'] for device in all_devices if device['family'] == 'Switches and Hubs']
    return switch_hostnames

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

        # Get all switches
        all_switch_hostnames = get_all_switches(DNAC_IP, headers)
        print("All switches Hostnames:")
        print(all_switch_hostnames)

        # List all switches in the sites
        sites = [432, 683, 104, 503, 224, 711, 713, 4716, 710, 444, 139, 416, 427, 405, 344, 344, 402, 689, 413, 420, 687, 4601, 502]
        
        # Extract hostnames and check if they start with any site number
        site_switch_hostnames = [hostname for hostname in all_switch_hostnames if any(hostname.startswith(str(site)) for site in sites)]
          
        print("Switches hostname in the specified sites:")
        for site_switch_hostname in site_switch_hostnames:
            print(site_switch_hostname)
        print("Total Switches number in the specified sites:")
        print(len(site_switch_hostnames))
