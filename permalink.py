import requests

url = "https://api.crunchbase.com/v4/data/entities/organizations/nvidia"

headers = {
    "accept": "application/json",
    "X-cb-user-key": "5ecfc303e1208e8617c895213d7c4926"
}

payload = {
    "field_ids": ["identifier", "name"]
}

response = requests.get(url, headers=headers)

print(response.text)
