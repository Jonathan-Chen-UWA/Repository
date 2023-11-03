import requests

url = "https://is-dnac-002.net.uwa.edu.au/dna/system/api/v1/auth/token"

payload = {}
headers = {
  'Authorization': 'Basic ZG5hYy1hZG1pbjpScThkTUplNzFBSGM='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
