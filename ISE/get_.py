import requests
from requests.auth import HTTPBasicAuth

# Cisco ISE API details
ise_base_url = 'https://is-ise-010.uniwa.uwa.edu.au:9060/ers'
username = 'naadmin'
password = 'L3tm31n0k'

# Disable warnings for unverified HTTPS requests (optional)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Function to make a GET request to Cisco ISE API
def get_ise_identity_groups():
    endpoint = '/config/identitygroup'
    url = f'{ise_base_url}{endpoint}'
    
    response = requests.get(url, auth=HTTPBasicAuth(username, password), headers={'Accept': 'application/json'}, verify=False)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')
        print(f'Response: {response.text}')
        return None

# Example usage: Get all identity groups
identity_groups = get_ise_identity_groups()
if identity_groups:
    print('Identity Groups:')
    for group in identity_groups.get('SearchResult', {}).get('resources', []):
        print(f"ID: {group['id']}, Name: {group['name']}")