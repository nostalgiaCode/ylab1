import requests
import pytest
import json

url = "http://127.0.0.1:8000/api/v1/menus"
response = requests.get(url)
delete_list = []
list = response.json()

for i in range(len(list)):
    id = list[i]['id']
    delete_list.append(id)

for i in delete_list:
    requests.delete(url+"/"+i)

response = requests.get(url).json()
print(response)