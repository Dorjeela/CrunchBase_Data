import requests
import json

url = "https://api.crunchbase.com/api/v4/searches/organizations"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-cb-user-key": "5ecfc303e1208e8617c895213d7c4926"
}

payload = {
    "field_ids": ["identifier", "name"]
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
data = response.json()

permalinks = [org['properties']['identifier']['permalink'] for org in data['entities']]

print(json.dumps(permalinks, indent=4))
