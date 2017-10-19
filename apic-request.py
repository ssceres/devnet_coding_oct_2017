#Import necessary modules
import requests
import json

#Disable warnings
requests.packages.urllib3.disable_warnings()

# Variables
apic_em_ip = "https://10.0.253.141/api/v1"
api_call ="/ticket"

#Payload contains authentication information
payload = {"username":"admin","password":"P@ssw0rd"}

# Header information
headers = {"content-type" : "application/json"}

# Combine apic_em_ip and api_call variables into one variable call url
url = apic_em_ip + api_call

response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()

print("Authenticaton Token: " + response["response"]["serviceTicket"])