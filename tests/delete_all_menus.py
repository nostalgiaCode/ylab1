import requests
import pytest
import json

# url = "http://python:80/api/v1/menus" -> docker
url = "http://127.0.0.1:8000/api/v1/menus" #->from local to docker

def delete_all(url):   
    response = requests.get(url)
    delete_list = []
    list = response.json()

    for i in range(len(list)):
        id = list[i]['id']
        delete_list.append(id)

    for i in delete_list:
        requests.delete(url+"/"+i)

delete_all(url)
print(requests.get(url).json())