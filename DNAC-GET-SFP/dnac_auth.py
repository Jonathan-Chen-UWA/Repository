import requests
import argparse

DNAC_IP = "is-dnac-002.net.uwa.edu.au"
DNAC_URL = f"https://{DNAC_IP}/dna/system/api/v1/auth/token"

def authenticate(username, password):
    response = requests.post(DNAC_URL, auth=(username, password), verify=False)

    if response.status_code == 200:
        response_data = response.json()
        DNAC_TOKEN = response_data.get("Token")
        if DNAC_TOKEN:
            return DNAC_TOKEN  # Return the token if authentication is successful
        else:
            print("Token not found in the response.")
    else:
        print(f"Failed to obtain the token. Status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Authenticate with Cisco DNA Center API')
    parser.add_argument('-username', required=True, help='Username for authentication')
    parser.add_argument('-password', required=True, help='Password for authentication')

    args = parser.parse_args()
    token = authenticate(args.username, args.password)  # Store the returned token

    if token:
        print(f"Token: {token}")