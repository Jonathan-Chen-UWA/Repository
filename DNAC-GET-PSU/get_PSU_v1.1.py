# This version generates the data and transfer the data to the excel spreadsheet.


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




def get_powersupply(switch_id, switch_hostname):
    DNAC_GET_PSU_URL = f"https://{DNAC_IP}/dna/intent/api/v1/network-device/{switch_id}/equipment?type=PowerSupply"
    response = requests.get(DNAC_GET_PSU_URL, headers=headers, verify=False)
    psus = json.loads(response.content).get("response", [])
    
    # Debug
    print(psus)

    # Create a list to hold power supply data
    psu_data = []
    
    for psu in psus:
        if 'productId' in psu and psu['productId'] != "":
            # Append a dictionary for each PSU to the list
            # This line of code checks two things:
            #1. 'productId' is a key in the psu dictionary (i.e., the productId field exists).
            #2. The value associated with the productId key in the psu dictionary is an empty string ("").
            psu_data.append({
                'Hostname': switch_hostname,
                'Name': psu.get('name', ''),
                'Description': psu.get('description', ''),
                'Serial Number': psu.get('serialNumber', ''),
                'Product ID': psu.get('productId', '')
            })

    #Debug DataFrame Construction
    df = pd.DataFrame(psu_data)
    print(df)

    # Convert the list of dictionaries into a DataFrame
    return pd.DataFrame(psu_data)

# Assume your existing code for getting all devices and filtering for switches here

# Initialize an empty DataFrame
all_psu_data = pd.DataFrame()



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


# Loop through switches and collect PSU data
for switch in switches:
    switch_id = f"{switch['id']}"
    switch_hostname = switch['hostname']
    switch_psu_data = get_powersupply(switch_id, switch_hostname)

    if 'Name' in switch_psu_data.columns:
        switch_psu_data = switch_psu_data.sort_values(by='Name')
    else:
        print(f"'Name' column not found in the DataFrame for switch {switch_hostname}")

    all_psu_data = pd.concat([all_psu_data, switch_psu_data], ignore_index=True)

    # Replace duplicates with empty string in 'Hostname' column
    duplicates = all_psu_data.duplicated(subset=['Hostname'], keep='first')
    all_psu_data.loc[duplicates, 'Hostname'] = ""


# Export the DataFrame to an Excel file
excel_filename = "PSU_Data.xlsx"
all_psu_data.to_excel(excel_filename, index=False)

print(f"Data exported to {excel_filename}")