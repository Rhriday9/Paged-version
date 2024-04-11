import requests
import json
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 0118f6f6-b946-4383-abc8-abc555580b4a'
}
page=1
url=f'https://amd.qtestnet.com/api/v3/projects/129172/test-cases?page={page}'
response = requests.request("GET", url, headers=headers)
if response.status_code==200:
    print(response.text)
