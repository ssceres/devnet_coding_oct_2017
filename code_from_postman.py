import requests

requests.packages.urllib3.disable_warnings()

url = "https://10.0.253.141/api/v1/ticket"

payload = "{\r\n \"username\" : \"admin\",\r\n \"password\" : \"P@ssw0rd\"\r\n }"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "5015916c-4cab-c1fc-bc08-e7a7c66f63d2"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)