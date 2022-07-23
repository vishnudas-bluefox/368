import requests

endpoint = " http://127.0.0.1:8000/api/mothali/4/update/"

data = {
    "userid": "id2",
    "title": "hjgdjhagdlgd;agd:",
}
# we can use put and patch method to update the entire section or edit few fields 
get_response = requests.patch(endpoint,json=data)

print(get_response.json())
# print(get_response.status_code)

    # "title": "raamaya maasam",
    # "media": "Desktop/mmoa.jpg",