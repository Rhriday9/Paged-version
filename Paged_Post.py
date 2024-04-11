import requests
import json
base_url = "https://amd.qtestnet.com/api/v3/projects/125506/search/?"
#url = "https://amd.qtestnet.com/api/v3/projects/125506/search/?page=1&order=1&pageSize=1&includeExternalProperties=true"

#Testcase2
page = 1
order = 1
pageSize = 1
includeExternalProperties="true"
payload = json.dumps({
  "object_type": "test-cases",
  "fields": [
    "id",
    "pid",
    "name"
  ],
  "query": "'Name' ~ '%'"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 0118f6f6-b946-4383-abc8-abc555580b4a'
}
url = base_url+f"page={page}"+"&"+f"order={order}"+"&"+f"pageSize={pageSize}"+"&"+f"includeExternalProperties={includeExternalProperties}"
response = requests.request("POST", url, headers=headers, data=payload)
if response.status_code==200:
    datas=json.loads(response.text)
    print('status',response.status_code)
    print("page,",datas['page'])
    print("pageSize,",datas['page_size'])
    print("total,",datas['total'])
    print("pid,",datas['items'][0]['pid'])
    print("id,",datas['items'][0]['id'])
    print("name,",datas['items'][0]['name'])
    print("testcases status code is verified")
else: 
    print("testcases status code is coming not as expected")
print(response.text)
