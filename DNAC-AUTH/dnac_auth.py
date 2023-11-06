import requests
DNAC_IP = "sandboxdnac.cisco.com"


# Define the API endpoint for authorization
DNAC_URL = f"https://{DNAC_IP}/dna/system/api/v1/auth/token"

# Define the client credentials (username and password)
username = "devnetuser"
password = "Cisco123!"

# # Define any additional parameters required by the authorization endpoint
# params = {
#     "grant_type": "password",  # This might vary based on the authorization flow
#     "client_id": "your_client_id",
#     "client_secret": "your_client_secret",
# }

# Make the POST request to obtain an authorization code
response = requests.post(DNAC_URL, auth=(username, password), verify=False)
# print ("We are going to find the response output here")
# print (response.content)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response, which may contain the authorization code

    response_data = response.json()
    DNAC_TOKEN = response_data.get("Token")
    if DNAC_TOKEN:
        print(f"Token: {DNAC_TOKEN}")
    else:
        print("Token not found in the response.")
else:
    print(f"Failed to obtain the token. Status code: {response.status_code}")
    print(response.text)  # Print the response content for debugging

  