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




# Define Get device URL
DNAC_GET_DEVICE_URL = f"https://{DNAC_IP}/dna/intent/api/v1/network-device"
# print(DNAC_GET_DEVICE_URL)

# Send an HTTP GET request to the Cisco DNA Center APIs to get the list of switches
response = requests.get(DNAC_GET_DEVICE_URL, headers=headers, verify=False)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON to extract the list of switches
    devices = json.loads(response.content)["response"]
    #print(devices)
    switches = [device for device in devices if device['family'] == 'Switches and Hubs']

   # Print the list of switches
    switch_ids = []
    for switch in switches:
        switch_ids.append(f"{switch['id']}")
        #print(f"{switch['hostname']} ({switch['managementIpAddress']}) id {switch['id']}")
        
else:
    print(f"Failed to obtain the network device data. Status code: {response.status_code}")
    print(response.text)  # Print the response content for debugging

#print(switch_ids)



# Send an HTTP GET request to the Cisco DNA Center APIs to get the list of SFP on each switch
for switch_id in switch_ids:
    #Define URL for SFP API
    DNAC_GET_SFP_URL = f"https://{DNAC_IP}/dna/intent/api/v1/network-device/{switch_id}/equipment?type=SFP"
    #Request SFP
    response = requests.get(DNAC_GET_SFP_URL, headers=headers, verify=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON to extract the list of switches
        sfps = json.loads(response.content)["response"]
        # Print the list of SFP
        #print(switch_id)
        print({switch['hostname']})
        for sfp in sfps:
            print(f"serial number {sfp['serialNumber']}")

    else:
        print(f"Failed to obtain the sfp details on network device. Status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging
 