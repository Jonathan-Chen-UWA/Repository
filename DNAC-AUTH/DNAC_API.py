import requests
import json

# Define the Cisco DNA Center IP address or hostname and authentication token
DNAC_IP = "is-dnac-002.net.uwa.edu.au"
DNAC_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmUzNzk4MmUxNmE4MzUwNDJlYjEyOTMiLCJhdXRoU291cmNlIjoiZXh0ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYxYjk5M2UwMTg2YWZlNTdjMTk5MzFiYyJdLCJ0ZW5hbnRJZCI6IjYxYjk5M2UwMTg2YWZlNTdjMTk5MzFiYSIsImV4cCI6MTY5ODk4NDQxOCwiaWF0IjoxNjk4OTgwODE4LCJqdGkiOiIxYzUxZTM3MC02MWVmLTQ1NGQtYjUxMC0zM2M1ZmYyY2ZiN2MiLCJ1c2VybmFtZSI6ImRuYWMtYWRtaW4ifQ.jjGlzOemUJwu5hFqLxJ69wrWl5aC19RR1O8xlYaGw3lmyuuXIVsrZNFJulceBXYVCFH_vTKFQn_CMDbaPvL5QyitwdX6QoV6FhqQz_yaA3XiPbMqaPMsjgL93TBe1Zyqnjx0VjNSJIWtqy4VoCku-wu8se_lCp5l-aB5BwKBb1-N1x_noA694_T66UrC4yJu5Kmfpi0_rJPvcBAwrpQZ6EwmXchWzLT05QRcDV98MkEo3Sk6EaJ2IzpqCshFqfZ2Ua4Q8_-VIQdXC9x7VeqEQEWMqux05vf17Q1xLpscQuH0zxzdh9K6TzB4jJmLGUbksmYN06-2yxduLO1SV7G9Ow"

# Define the request headers with the authentication token
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": DNAC_TOKEN
}

# Send an HTTP GET request to the Cisco DNA Center APIs to get the list of switches
response = requests.get(f"https://{DNAC_IP}/api/v1/network-device", headers=headers, verify=False)

# Parse the response JSON to extract the list of switches
switches = json.loads(response.content)["response"]

# Print the list of switches
for switch in switches:
    print(f"{switch['hostname']} ({switch['managementIpAddress']})")
