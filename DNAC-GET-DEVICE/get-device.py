import requests

url = "/dna/intent/api/v1/network-device"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

