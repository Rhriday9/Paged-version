import requests
import json
import random
def auto_run(field_id,page,pageSize,n):
    url = f"https://amd.qtestnet.com/api/v3/projects/125506/search/?test-runs/{field_id}/auto-test-logs&page={page}&pageSize={pageSize}"
    payload = json.dumps({
    "object_type": "test-cases",
    "fields": [
    "*"
    ],
  "query": "Name ~ .*"
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 0118f6f6-b946-4383-abc8-abc555580b4a'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    datas = {}
    data = json.loads(response.text)
    datas['page'] = data['page']
    datas['page_size'] = data['page_size']
    for item in data['items']:
        datas['id'] = item['id']
        datas['name'] = item['name']
        datas['order'] = item['order']
        datas['pid'] = item['pid']
        datas['created_date'] = item['created_date']
        datas['last_modified_date'] = item['last_modified_date']
        for x in item['properties']:
            datas['field_name'] = x['field_name']
            datas['field_id'] = x['field_id']
    with open(f"{n}.txt","w") as f:
        f.write(json.dumps(datas,indent=4))
        f.close()

for n in  range(10):
    auto_run(random.randint(1,10),random.randint(1,10),random.randint(1,10),n)