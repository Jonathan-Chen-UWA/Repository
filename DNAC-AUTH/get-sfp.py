    # import requests
    # import json

    # # Define the Cisco DNA Center IP address or hostname and authentication token
    # DNAC_IP = "is-dnac-002.net.uwa.edu.au"
    # DNAC_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmUzNzk4MmUxNmE4MzUwNDJlYjEyOTMiLCJhdXRoU291cmNlIjoiZXh0ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYxYjk5M2UwMTg2YWZlNTdjMTk5MzFiYyJdLCJ0ZW5hbnRJZCI6IjYxYjk5M2UwMTg2YWZlNTdjMTk5MzFiYSIsImV4cCI6MTY5ODk4NDQxOCwiaWF0IjoxNjk4OTgwODE4LCJqdGkiOiIxYzUxZTM3MC02MWVmLTQ1NGQtYjUxMC0zM2M1ZmYyY2ZiN2MiLCJ1c2VybmFtZSI6ImRuYWMtYWRtaW4ifQ.jjGlzOemUJwu5hFqLxJ69wrWl5aC19RR1O8xlYaGw3lmyuuXIVsrZNFJulceBXYVCFH_vTKFQn_CMDbaPvL5QyitwdX6QoV6FhqQz_yaA3XiPbMqaPMsjgL93TBe1Zyqnjx0VjNSJIWtqy4VoCku-wu8se_lCp5l-aB5BwKBb1-N1x_noA694_T66UrC4yJu5Kmfpi0_rJPvcBAwrpQZ6EwmXchWzLT05QRcDV98MkEo3Sk6EaJ2IzpqCshFqfZ2Ua4Q8_-VIQdXC9x7VeqEQEWMqux05vf17Q1xLpscQuH0zxzdh9K6TzB4jJmLGUbksmYN06-2yxduLO1SV7G9Ow"

    # # Define the request headers with the authentication token
    # headers = {
    #     "Content-Type": "application/json",
    #     "X-Auth-Token": DNAC_TOKEN
    # }

    # # Send an HTTP GET request to the Cisco DNA Center APIs to get the list of switches
    # response = requests.get(f"https://{DNAC_IP}/api/v1/sfp-details", headers=headers, verify=False)

    # # Print the list of sfp serial number
    # if response.status_code == 200:
    #     sfp_data = response.json()
    #     for sfp in sfp_data:
    #         serial_number = sfp.get("serialNumber")
    #         print(f"SFP Serial Number: {serial_number}")
    # else:
    #     print(f"API 请求失败，状态码: {response.status_code}")



import requests

# 认证令牌，确保替换为实际的令牌
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmUzNzk4MmUxNmE4MzUwNDJlYjEyOTMiLCJhdXRoU291cmNlIjoiZXh0ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYxYjk5M2UwMTg2YWZlNTdjMTk5MzFiYyJdLCJ0ZW5hbnRJZCI6IjYxYjk5M2UwMTg2YWZlNTdjMTk5MzFiYSIsImV4cCI6MTY5ODk4NDQxOCwiaWF0IjoxNjk4OTgwODE4LCJqdGkiOiIxYzUxZTM3MC02MWVmLTQ1NGQtYjUxMC0zM2M1ZmYyY2ZiN2MiLCJ1c2VybmFtZSI6ImRuYWMtYWRtaW4ifQ.jjGlzOemUJwu5hFqLxJ69wrWl5aC19RR1O8xlYaGw3lmyuuXIVsrZNFJulceBXYVCFH_vTKFQn_CMDbaPvL5QyitwdX6QoV6FhqQz_yaA3XiPbMqaPMsjgL93TBe1Zyqnjx0VjNSJIWtqy4VoCku-wu8se_lCp5l-aB5BwKBb1-N1x_noA694_T66UrC4yJu5Kmfpi0_rJPvcBAwrpQZ6EwmXchWzLT05QRcDV98MkEo3Sk6EaJ2IzpqCshFqfZ2Ua4Q8_-VIQdXC9x7VeqEQEWMqux05vf17Q1xLpscQuH0zxzdh9K6TzB4jJmLGUbksmYN06-2yxduLO1SV7G9Ow"

# 构建 API 请求
url = "https://is-dnac-002.net.uwa.edu.au/api/v1/sfp-details"  # 替换为正确的 API 端点
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": token
}

# 发送 API 请求
response = requests.get(url, headers=headers, verify=False)  # verify=False 可能需要根据你的 DNAC 证书设置

# 处理 API 响应
if response.status_code == 200:
    sfp_data = response.json()
    for sfp in sfp_data:
        serial_number = sfp.get("serialNumber")
        print(f"SFP Serial Number: {serial_number}")
else:
    print(f"API 请求失败，状态码: {response.status_code}")