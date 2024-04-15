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
    #print(response.text)
    datas = {}
    data = json.loads(response.text)
    if 'items' in data and data['items']:
        datas= []
        item_data = None
    for item in data['items']:
        item_data = {
        datas['page'] = data['page']
        datas['page_size'] = data['page_size']
        datas['id'] = item['id']
        datas['name'] = item['name']
        datas['order'] = item['order']
        datas['pid'] = item['pid']
        datas['created_date'] = item['created_date']
        datas['last_modified_date'] = item['last_modified_date']
        }
        properties = []
        for x in item['properties']:
            properties.append({
                'field_name': 
                x['field_name'], 
                'field_id':
                x['field_id']
            })
            item_data['properties'] = properties
            datas.append(item_data)
            print(item_date)
            datas['field_name'] = x['field_name']
            datas['field_id'] = x['field_id']
    with open(f"{n}.txt","w") as f:
        f.write(json.dumps(datas,indent=4))

for n in  range(10):
    auto_run(random.randint(1,10),random.randint(1,10),random.randint(1,10),n)