import requests
from datetime import datetime
USERNAME = ""
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hr",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

now = datetime.now()
formatted_date = now.strftime("%Y%m%d")
print(formatted_date)

coding_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

pixel_config = {
    "date": formatted_date,
    "quantity": "1.0"
}

response = requests.post(url=coding_graph_endpoint, json=pixel_config, headers=headers)
print(response.text)