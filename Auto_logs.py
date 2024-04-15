import requests
import json
import random

def auto_run(field_id, page, pageSize, n):
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
    datas = {}
    data = json.loads(response.text)
    print(data)
    if 'items' in data and data['items']:
        datas['page'] = data['page']
        datas['page_size'] = data['page_size']
        datas['items'] = []
        for item in data['items']:
            item_data = {
                'id': item['id'],
                'name': item['name'],
                'order': item['order'],
                'pid': item['pid'],
                'created_date': item['created_date'],
                'last_modified_date': item['last_modified_date']
            }
            properties = []
            for x in item['properties']:
                properties.append({
                    'field_name': x['field_name'],
                    'field_id': x['field_id']
                })
            item_data['properties'] = properties
            datas['items'].append(item_data)
        
    with open(f"{n}.txt", "w") as f:
        f.write(json.dumps(datas, indent=4))

# for n in range(10):
#     auto_run(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), n)
auto_run(3,1,1,"data")