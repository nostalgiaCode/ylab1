import requests
import json

# host = "http://127.0.0.1:8000/api/v1/menus/" -> localhost
host = "http://python:80/api/v1/menus/"

def get_menu(target_menu_id):
    url = host + target_menu_id
    return requests.get(url)

def get_submenu(target_menu_id, target_submenu_id):
    url = host + target_menu_id + "/submenus/" + target_submenu_id
    return requests.get(url)  
  
def get_dish(target_menu_id, target_submenu_id, target_dish_id):
    url = host + target_menu_id + "/submenus/" + target_submenu_id + "/dishes/" + target_dish_id
    return requests.get(url)

def get_all_menus():
    url = host
    return requests.get(url)

def get_all_submenus(target_menu_id):
    url = host + target_menu_id + "/submenus/"
    return requests.get(url)

def get_all_dishes(target_menu_id, target_submenu_id):
    url = host + target_menu_id + "/submenus/" + target_submenu_id + "/dishes"
    return requests.get(url)

def post_menu(target_menu_title, target_menu_description):
    url = host
    
    params = {
    "title": target_menu_title,
    "description": target_menu_description
}
    return requests.post(url, json=params)

def post_submenu(target_menu_id, target_submenu_title, target_submenu_description):
    url = host + target_menu_id + "/submenus"
    
    params = {
    "title": target_submenu_title,
    "description": target_submenu_description
}
    return requests.post(url, json=params)

def post_dish(target_menu_id, target_submenu_id, target_dish_title, target_dish_description, target_dish_price):
    url = host + target_menu_id + "/submenus/" + target_submenu_id + "/dishes"
    params = {
    "title": target_dish_title,
    "description": target_dish_description,
    "price": target_dish_price
}
    return requests.post(url, json=params)

def patch_menu(target_menu_id, target_menu_title, target_menu_description):
    url = host + target_menu_id
    params = {
    "title": target_menu_title,
    "description": target_menu_description
}
    return requests.patch(url, json=params)

def patch_submenu(target_menu_id, target_submenu_id, target_submenu_title, target_submenu_description):
    url = host + target_menu_id + "/submenus/" + target_submenu_id
    params = {
    "title": target_submenu_title,
    "description": target_submenu_description
}
    return requests.patch(url, json=params)

def patch_dish(target_menu_id, target_submenu_id, target_dish_id, target_dish_title, target_dish_description, target_dish_price):
    url = host + target_menu_id + "/submenus/" + target_submenu_id + "/dishes/" + target_dish_id
    params = {
    "title": target_dish_title,
    "description": target_dish_description,
    "price": target_dish_price
}
    return requests.patch(url, json=params)

def delete_menu(target_menu_id):
    url = host + target_menu_id
    return requests.delete(url)

def delete_submenu(target_menu_id, target_submenu_id):
    url = host + target_menu_id + "/submenus/" + target_submenu_id
    return requests.delete(url)

def delete_dish(target_menu_id, target_submenu_id, target_dish_id):
    url = host + target_menu_id + "/submenus/" + target_submenu_id + "/dishes/" + target_dish_id
    return requests.delete(url)