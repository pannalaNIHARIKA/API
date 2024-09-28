import requests
from datetime import datetime

USERNAME = "xxxx"
TOKEN = "xxxx"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPHID = "graph1"
# new_user_params = {
#     "token": "xxxx",
#     "username": "xxxx",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint,json=new_user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "coding graph",
#     "unit": "minutes",
#     "type": "int",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_update_endpoint = f"{graph_endpoint}/{GRAPHID}"
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes you have coded today?"),
}
response = requests.post(url=graph_update_endpoint, json=pixel_config, headers=headers)
print(response.text)
# pixel_parameters = {
#     "quantity": "60"
# }
# pixel_update_endpoint = f"{graph_update_endpoint}/20240619"
# response = requests.put(url=pixel_update_endpoint, json=pixel_parameters, headers=headers)
# print(response.text)
# response = requests.delete(pixel_update_endpoint, headers=headers)
# print(response.text)
