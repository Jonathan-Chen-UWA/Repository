import requests
import json
import argparse
import pandas as pd
import os


from dnac_auth import authenticate, DNAC_IP



# Define the parameter for username and password 
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



# Get Switches from all_devices
from get_devices import get_all_devices
all_devices = get_all_devices(DNAC_IP, headers)
switches = [all_device for all_device in all_devices if all_device['family'] == 'Switches and Hubs']



# Get sfp list and attach switch hostname to it
from get_sfp import get_sfp
sfps = get_sfp(switches, headers)



# Get the current working directory
current_directory = os.getcwd()

# File path to the Excel file in the current directory
file_path = os.path.join(current_directory, 'inventory.xlsx')

# Load the Excel file
inventory_df = pd.read_excel(file_path, sheet_name='Inventory')  # Replace 'Inventory' with your sheet name

# Check if 'serialNumber' from 'sfps' exists in 'Serial Number' column of the inventory
for sfp in sfps:
    if sfp['serialNumber'] not in inventory_df['Serial Number'].values:
        print(f"Serial number {sfp['serialNumber']} on {sfp['switch_hostname']} is not in the inventory.")













""" 
print(len(switches))

print(len(sfps))

print(sfps[:3])

"""