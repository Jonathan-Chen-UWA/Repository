import requests
import json
import argparse


from dnac_auth import DNAC_IP


def get_sfp(switches, headers):
    sfps = []
    for switch in switches:
        switch_id = f"{switch['id']}"
        DNAC_GET_SFP_URL = f"https://{DNAC_IP}/dna/intent/api/v1/network-device/{switch_id}/equipment?type=SFP"
        #Request SFP
        response = requests.get(DNAC_GET_SFP_URL, headers=headers, verify=False)
        sfps_data = json.loads(response.content)["response"]
        for item in sfps_data:
            item['switch_hostname'] = f"{switch['hostname']}" 
        sfps.extend(sfps_data)
    return sfps