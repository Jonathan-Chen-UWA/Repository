import requests
import json
import argparse
import sys
sys.path.append(r'C:\Python\Repository\DNAC-GET-SFP\modules')


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

from get_devices import get_all_devices

all_devices = get_all_devices(DNAC_IP, headers)

# Get Switches from all_devices
switches = [all_device for all_device in all_devices if all_device['family'] == 'Switches and Hubs']

from get_sfp import get_sfp
spfs = get_sfp(switches, headers)

print(len(switches))

print(len(spfs))