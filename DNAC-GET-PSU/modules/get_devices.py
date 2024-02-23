import requests
import json
import argparse


from dnac_auth import DNAC_IP

def get_all_devices(DNAC_IP, headers):
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
    
    return (all_devices)

