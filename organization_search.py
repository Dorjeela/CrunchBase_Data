import requests
import json

url = "https://api.crunchbase.com/api/v4/searches/organizations"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-cb-user-key": "5ecfc303e1208e8617c895213d7c4926"
}

# Basic JSON payload with minimal criteria
payload = {
    "field_ids": ["identifier", "name"],
    "limit": 5
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(json.dumps(response.json(), indent=4))
