import requests
import pytest
import json

from utils.crud import *
from delete_all_menus import *

target_menu_id = None
target_menu_title = "My menu 1"
target_menu_description = "My menu description 1"
updated_menu_title = "My updated menu 1"
updated_menu_description = "My updated menu description 1"

target_submenu_id = None
target_submenu_title = "My submenu 1"
target_submenu_description = "My submenu description 1"
updated_submenu_title = "My updated submenu 1"
updated_submenu_description = "My updated submenu description 1"

target_dish_id = None
target_dish_title = "My dish 1"
target_dish_description = "My dish description 1"
target_dish_price = "12.50"
updated_dish_title = "My updated dish 1"
updated_dish_description = "My updated dish description 1"
updated_dish_price = "14.50"

delete_all()

def test_menu():
    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() == []

    response = post_menu(target_menu_title, target_menu_description)
    target_menu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == target_menu_id
    assert response.json()['title'] == target_menu_title
    assert response.json()['description'] == target_menu_description 

    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() != []

    response = get_menu(target_menu_id)
    assert response.status_code == 200
    assert response.json()['id'] == target_menu_id
    assert response.json()['title'] == target_menu_title
    assert response.json()['description'] == target_menu_description

    response = patch_menu(target_menu_id, updated_menu_title, updated_menu_description)
    assert response.status_code == 200
    assert response.json()['title'] != target_menu_title
    assert response.json()['description'] != target_menu_description
    assert response.json()['title'] == updated_menu_title
    assert response.json()['description'] == updated_menu_description

    response = get_menu(target_menu_id)
    assert response.status_code == 200
    assert response.json()['title'] != target_menu_title
    assert response.json()['description'] != target_menu_description
    assert response.json()['title'] == updated_menu_title
    assert response.json()['description'] == updated_menu_description

    response = delete_menu(target_menu_id)
    assert response.status_code == 200

    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() == []

    response = get_menu(target_menu_id)
    assert response.status_code == 404
    assert response.json()['detail'] == "menu not found"

def test_submenu():
    response = post_menu(target_menu_title, target_menu_description)
    target_menu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == target_menu_id
    assert response.json()['title'] == target_menu_title
    assert response.json()['description'] == target_menu_description 

    response = get_all_submenus(target_menu_id)
    assert response.status_code == 200
    assert response.json() == []

    response = post_submenu(target_menu_id, target_submenu_title, target_submenu_description)
    target_submenu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == target_submenu_id
    assert response.json()['title'] == target_submenu_title
    assert response.json()['description'] == target_submenu_description 

    response = get_all_submenus(target_menu_id)
    assert response.status_code == 200
    assert response.json() != []

    response = get_submenu(target_menu_id, target_submenu_id)
    assert response.status_code == 200
    assert response.json()['id'] == target_submenu_id
    assert response.json()['title'] == target_submenu_title
    assert response.json()['description'] == target_submenu_description
    
    response = patch_submenu(target_menu_id, target_submenu_id, updated_submenu_title, updated_submenu_description)
    assert response.status_code == 200
    assert response.json()['title'] != target_submenu_title
    assert response.json()['description'] != target_submenu_description
    assert response.json()['title'] == updated_submenu_title
    assert response.json()['description'] == updated_submenu_description

    response = get_submenu(target_menu_id, target_submenu_id)
    assert response.status_code == 200
    assert response.json()['id'] == target_submenu_id
    assert response.json()['title'] == updated_submenu_title
    assert response.json()['description'] == updated_submenu_description

    response = delete_submenu(target_menu_id, target_submenu_id)
    assert response.status_code == 200

    response = get_all_submenus(target_menu_id)
    assert response.status_code == 200
    assert response.json() == []

    response = get_submenu(target_menu_id, target_submenu_id)
    assert response.status_code == 404
    assert response.json()['detail'] == "submenu not found"

    response = delete_menu(target_menu_id)
    assert response.status_code == 200

    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() == []

def test_dish():
    response = post_menu(target_menu_title, target_menu_description)
    target_menu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == target_menu_id
    assert response.json()['title'] == target_menu_title
    assert response.json()['description'] == target_menu_description 

    response = post_submenu(target_menu_id, target_submenu_title, target_submenu_description)
    target_submenu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == target_submenu_id
    assert response.json()['title'] == target_submenu_title
    assert response.json()['description'] == target_submenu_description 

    response = get_all_dishes(target_menu_id, target_submenu_id)
    assert response.status_code == 200
    assert response.json() == []

    response = post_dish(target_menu_id, target_submenu_id, target_dish_title, target_dish_description, target_dish_price)
    target_dish_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == target_dish_id
    assert response.json()['title'] == target_dish_title
    assert response.json()['description'] == target_dish_description 
    assert response.json()['price'] == target_dish_price 

    response = get_all_dishes(target_menu_id, target_submenu_id)
    assert response.status_code == 200
    assert response.json() != []

    response = get_dish(target_menu_id, target_submenu_id, target_dish_id)
    assert response.status_code == 200
    assert response.json()['id'] == target_dish_id
    assert response.json()['title'] == target_dish_title
    assert response.json()['description'] == target_dish_description 
    assert response.json()['price'] == target_dish_price 

    response = patch_dish(target_menu_id, target_submenu_id, target_dish_id, updated_dish_title, updated_dish_description, updated_dish_price)
    assert response.status_code == 200
    assert response.json()['title'] != target_dish_title
    assert response.json()['description'] != target_dish_description 
    assert response.json()['price'] != target_dish_price 
    assert response.json()['title'] == updated_dish_title
    assert response.json()['description'] == updated_dish_description 
    assert response.json()['price'] == updated_dish_price

    response = get_dish(target_menu_id, target_submenu_id, target_dish_id)
    assert response.status_code == 200
    assert response.json()['id'] == target_dish_id
    assert response.json()['title'] == updated_dish_title
    assert response.json()['description'] == updated_dish_description 
    assert response.json()['price'] == updated_dish_price

    response = delete_dish(target_menu_id, target_submenu_id, target_dish_id)
    assert response.status_code == 200

    response = get_all_dishes(target_menu_id, target_submenu_id)
    assert response.status_code == 200
    assert response.json() == []

    response = get_dish(target_menu_id, target_submenu_id, target_dish_id)
    assert response.status_code == 404
    assert response.json()['detail'] == 'dish not found'

    response = delete_submenu(target_menu_id, target_submenu_id)
    assert response.status_code == 200

    response = get_all_submenus(target_menu_id)
    assert response.status_code == 200
    assert response.json() == []

    response = delete_menu(target_menu_id)
    assert response.status_code == 200

    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() == []

def test_dishes_and_submenus_in_menu():
    response = post_menu(target_menu_title, target_menu_description)
    target_menu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == target_menu_id
    assert response.json()['title'] == target_menu_title
    assert response.json()['description'] == target_menu_description 

    response = post_submenu(target_menu_id, target_submenu_title, target_submenu_description)
    target_submenu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == target_submenu_id
    assert response.json()['title'] == target_submenu_title
    assert response.json()['description'] == target_submenu_description 

    response = post_dish(target_menu_id, target_submenu_id, target_dish_title, target_dish_description, target_dish_price)
    target_dish_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == target_dish_id
    assert response.json()['title'] == target_dish_title
    assert response.json()['description'] == target_dish_description 
    assert response.json()['price'] == target_dish_price 

    response = post_dish(target_menu_id, target_submenu_id, target_dish_title, target_dish_description, target_dish_price)
    target_dish_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == target_dish_id
    assert response.json()['title'] == target_dish_title
    assert response.json()['description'] == target_dish_description 
    assert response.json()['price'] == target_dish_price 

    response = get_menu(target_menu_id)
    assert response.status_code == 200
    assert response.json()['id'] == target_menu_id
    assert response.json()['submenus_count'] == 1
    assert response.json()['dishes_count'] == 2

    response = get_submenu(target_menu_id, target_submenu_id)
    assert response.status_code == 200
    assert response.json()['id'] == target_submenu_id
    assert response.json()['dishes_count'] == 2

    response = delete_submenu(target_menu_id, target_submenu_id)
    assert response.status_code == 200

    response = get_all_submenus(target_menu_id)
    assert response.status_code == 200
    assert response.json() == []

    response = get_all_dishes(target_menu_id, target_submenu_id)
    assert response.status_code == 200
    assert response.json() == []

    response = get_menu(target_menu_id)
    assert response.status_code == 200
    assert response.json()['id'] == target_menu_id
    assert response.json()['submenus_count'] == 0
    assert response.json()['dishes_count'] == 0

    response = delete_menu(target_menu_id)
    assert response.status_code == 200

    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() == []

delete_all()