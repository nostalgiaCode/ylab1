import requests
import pytest
import json

from utils.crud import *
from variables import data


@pytest.mark.usefixtures("data")
def test_menu_create(data): 
    response = post_menu(pytest.target_menu_title, pytest.target_menu_description)
    pytest.target_menu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == pytest.target_menu_id
    assert response.json()['title'] == pytest.target_menu_title
    assert response.json()['description'] == pytest.target_menu_description 

@pytest.mark.usefixtures("data")
def test_submenu_create(data): 
    response = post_submenu(pytest.target_menu_id, pytest.target_submenu_title, pytest.target_submenu_description)
    pytest.target_submenu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == pytest.target_submenu_id
    assert response.json()['title'] == pytest.target_submenu_title
    assert response.json()['description'] == pytest.target_submenu_description 

@pytest.mark.usefixtures("data")
def test_dish_1_create(data):
    response = post_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_title, pytest.target_dish_description, pytest.target_dish_price)
    pytest.target_dish_1_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == pytest.target_dish_1_id
    assert response.json()['title'] == pytest.target_dish_title
    assert response.json()['description'] == pytest.target_dish_description 
    assert response.json()['price'] == pytest.target_dish_price 

@pytest.mark.usefixtures("data")
def test_dish_2_create(data):
    response = post_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_title, pytest.target_dish_description, pytest.target_dish_price)
    pytest.target_dish_2_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == pytest.target_dish_2_id
    assert response.json()['title'] == pytest.target_dish_title
    assert response.json()['description'] == pytest.target_dish_description 
    assert response.json()['price'] == pytest.target_dish_price 

@pytest.mark.usefixtures("data")
def test_get_menu(data):
    response = get_menu(pytest.target_menu_id)
    assert response.status_code == 200
    assert response.json()['id'] == pytest.target_menu_id
    assert response.json()['submenus_count'] == 1
    assert response.json()['dishes_count'] == 2

@pytest.mark.usefixtures("data")
def test_get_submenu(data):
    response = get_submenu(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200
    assert response.json()['id'] == pytest.target_submenu_id
    assert response.json()['dishes_count'] == 2

@pytest.mark.usefixtures("data")
def test_delete_submenu(data):
    response = delete_submenu(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200

@pytest.mark.usefixtures("data")
def test_get_submenus_all(data):
    response = get_all_submenus(pytest.target_menu_id)
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.usefixtures("data")
def test_get_dishes_all(data):
    response = get_all_dishes(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.usefixtures("data")
def test_get_menu_empty(data):
    response = get_menu(pytest.target_menu_id)
    assert response.status_code == 200
    assert response.json()['id'] == pytest.target_menu_id
    assert response.json()['submenus_count'] == 0
    assert response.json()['dishes_count'] == 0

@pytest.mark.usefixtures("data")
def test_delete_menu(data):
    response = delete_menu(pytest.target_menu_id)
    assert response.status_code == 200

@pytest.mark.usefixtures("data")
def test_get_menus_all(data):
    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() == []