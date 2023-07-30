import requests
import pytest
import json

def delete_all():
    url = "http://python:80/api/v1/menus"
    response = requests.get(url)
    delete_list = []
    list = response.json()

    for i in range(len(list)):
        id = list[i]['id']
        delete_list.append(id)

    for i in delete_list:
        requests.delete(url+"/"+i)