import requests

endpoint = " http://127.0.0.1:8000/api/mothali/"

data = {
    "userid":"id6",
    "title":"thihgdjhgd",
    "content":"Mannaram company ux.ksjdhksgdgdlhgdhgdniversity:",
    "media": "medkjshdkia url here",
}

get_response = requests.post(endpoint,json=data)


print(get_response.json())
# print(get_response.status_code)