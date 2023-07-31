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
def test_dish_create(data):
    response = post_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_title, pytest.target_dish_description, pytest.target_dish_price)
    pytest.target_dish_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == pytest.target_dish_id
    assert response.json()['title'] == pytest.target_dish_title
    assert response.json()['description'] == pytest.target_dish_description 
    assert response.json()['price'] == pytest.target_dish_price 

@pytest.mark.usefixtures("data")
def test_menu_get(data):
    response = get_menu(pytest.target_menu_id)
    assert response.status_code == 200
    assert response.json()['id'] == pytest.target_menu_id
    assert response.json()['title'] == pytest.target_menu_title
    assert response.json()['description'] == pytest.target_menu_description

@pytest.mark.usefixtures("data")
def test_submenu_get(data):
    response = get_submenu(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200
    assert response.json()['id'] == pytest.target_submenu_id
    assert response.json()['title'] == pytest.target_submenu_title
    assert response.json()['description'] == pytest.target_submenu_description

@pytest.mark.usefixtures("data")
def test_dish_get(data):
    response = post_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_title, pytest.target_dish_description, pytest.target_dish_price)
    pytest.target_dish_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == pytest.target_dish_id
    assert response.json()['title'] == pytest.target_dish_title
    assert response.json()['description'] == pytest.target_dish_description 
    assert response.json()['price'] == pytest.target_dish_price 

@pytest.mark.usefixtures("data")
def test_menu_get_all(data):
    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() != []

@pytest.mark.usefixtures("data")
def test_submenu_get_all(data):
    response = get_all_submenus(pytest.target_menu_id)
    assert response.status_code == 200
    assert response.json() != []

@pytest.mark.usefixtures("data")
def test_dish_get_all(data):
    response = get_all_dishes(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200
    assert response.json() != []

@pytest.mark.usefixtures("data")
def test_menu_patch(data):
    response = patch_menu(pytest.target_menu_id, pytest.updated_menu_title, pytest.updated_menu_description)
    assert response.status_code == 200
    assert response.json()['title'] != pytest.target_menu_title
    assert response.json()['description'] != pytest.target_menu_description
    assert response.json()['title'] == pytest.updated_menu_title
    assert response.json()['description'] == pytest.updated_menu_description

@pytest.mark.usefixtures("data")
def test_submenu_patch(data):
    response = patch_submenu(pytest.target_menu_id, pytest.target_submenu_id, pytest.updated_submenu_title, pytest.updated_submenu_description)
    assert response.status_code == 200
    assert response.json()['title'] != pytest.target_submenu_title
    assert response.json()['description'] != pytest.target_submenu_description
    assert response.json()['title'] == pytest.updated_submenu_title
    assert response.json()['description'] == pytest.updated_submenu_description

@pytest.mark.usefixtures("data")
def test_dish_patch(data):
    response = patch_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_id, pytest.updated_dish_title, pytest.updated_dish_description, pytest.updated_dish_price)
    assert response.status_code == 200
    assert response.json()['title'] != pytest.target_dish_title
    assert response.json()['description'] != pytest.target_dish_description 
    assert response.json()['price'] != pytest.target_dish_price 
    assert response.json()['title'] == pytest.updated_dish_title
    assert response.json()['description'] == pytest.updated_dish_description 
    assert response.json()['price'] == pytest.updated_dish_price

@pytest.mark.usefixtures("data")
def test_dish_remove(data):
    response = delete_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_id)
    assert response.status_code == 200

@pytest.mark.usefixtures("data")
def test_submenu_remove(data):
    response = delete_submenu(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200

@pytest.mark.usefixtures("data")
def test_menu_remove(data):
    response = delete_menu(pytest.target_menu_id)
    assert response.status_code == 200

@pytest.mark.usefixtures("data")
def test_menu_get_404(data):
    response = get_menu(pytest.target_menu_id)
    assert response.status_code == 404
    assert response.json()['detail'] == "menu not found"

@pytest.mark.usefixtures("data")
def test_submenu_get_404(data):
    response = get_submenu(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 404
    assert response.json()['detail'] == "submenu not found"

@pytest.mark.usefixtures("data")
def test_dish_get_404(data):
    response = get_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_id)
    assert response.status_code == 404
    assert response.json()['detail'] == 'dish not found'

@pytest.mark.usefixtures("data")
def test_menu_get_all_empty(data):
    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.usefixtures("data")
def test_submenu_get_all_empty(data):
    response = get_all_submenus(pytest.target_menu_id)
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.usefixtures("data")
def test_dish_get_all_empty(data):
    response = get_all_dishes(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200
    assert response.json() == []