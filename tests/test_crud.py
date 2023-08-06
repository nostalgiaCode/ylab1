import pytest
from utils.functions import (
    delete_dish,
    delete_menu,
    delete_submenu,
    get_all_dishes,
    get_all_menus,
    get_all_submenus,
    get_dish,
    get_menu,
    get_submenu,
    patch_dish,
    patch_menu,
    patch_submenu,
    post_dish,
    post_menu,
    post_submenu,
)


@pytest.mark.usefixtures('data')
def test_menu_create():
    response = post_menu(pytest.target_menu_title, pytest.target_menu_description)
    pytest.target_menu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == pytest.target_menu_id
    assert response.json()['title'] == pytest.target_menu_title
    assert response.json()['description'] == pytest.target_menu_description


@pytest.mark.usefixtures('data')
def test_submenu_create():
    response = post_submenu(pytest.target_menu_id, pytest.target_submenu_title, pytest.target_submenu_description)
    pytest.target_submenu_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == pytest.target_submenu_id
    assert response.json()['title'] == pytest.target_submenu_title
    assert response.json()['description'] == pytest.target_submenu_description


@pytest.mark.usefixtures('data')
def test_dish_create():
    response = post_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_title,
                         pytest.target_dish_description, pytest.target_dish_price)
    pytest.target_dish_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == pytest.target_dish_id
    assert response.json()['title'] == pytest.target_dish_title
    assert response.json()['description'] == pytest.target_dish_description
    assert response.json()['price'] == pytest.target_dish_price


@pytest.mark.usefixtures('data')
def test_menu_get():
    response = get_menu(pytest.target_menu_id)
    assert response.status_code == 200
    assert response.json()['id'] == pytest.target_menu_id
    assert response.json()['title'] == pytest.target_menu_title
    assert response.json()['description'] == pytest.target_menu_description


@pytest.mark.usefixtures('data')
def test_submenu_get():
    response = get_submenu(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200
    assert response.json()['id'] == pytest.target_submenu_id
    assert response.json()['title'] == pytest.target_submenu_title
    assert response.json()['description'] == pytest.target_submenu_description


@pytest.mark.usefixtures('data')
def test_dish_get():
    response = post_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_title,
                         pytest.target_dish_description, pytest.target_dish_price)
    pytest.target_dish_id = response.json()['id']
    assert response.status_code == 201
    assert response.json()['id'] == pytest.target_dish_id
    assert response.json()['title'] == pytest.target_dish_title
    assert response.json()['description'] == pytest.target_dish_description
    assert response.json()['price'] == pytest.target_dish_price


@pytest.mark.usefixtures('data')
def test_menu_get_all():
    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() != []


@pytest.mark.usefixtures('data')
def test_submenu_get_all():
    response = get_all_submenus(pytest.target_menu_id)
    assert response.status_code == 200
    assert response.json() != []


@pytest.mark.usefixtures('data')
def test_dish_get_all():
    response = get_all_dishes(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200
    assert response.json() != []


@pytest.mark.usefixtures('data')
def test_menu_patch():
    response = patch_menu(pytest.target_menu_id, pytest.updated_menu_title, pytest.updated_menu_description)
    assert response.status_code == 200
    assert response.json()['title'] != pytest.target_menu_title
    assert response.json()['description'] != pytest.target_menu_description
    assert response.json()['title'] == pytest.updated_menu_title
    assert response.json()['description'] == pytest.updated_menu_description


@pytest.mark.usefixtures('data')
def test_submenu_patch():
    response = patch_submenu(pytest.target_menu_id, pytest.target_submenu_id,
                             pytest.updated_submenu_title, pytest.updated_submenu_description)
    assert response.status_code == 200
    assert response.json()['title'] != pytest.target_submenu_title
    assert response.json()['description'] != pytest.target_submenu_description
    assert response.json()['title'] == pytest.updated_submenu_title
    assert response.json()['description'] == pytest.updated_submenu_description


@pytest.mark.usefixtures('data')
def test_dish_patch():
    response = patch_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_id,
                          pytest.updated_dish_title, pytest.updated_dish_description, pytest.updated_dish_price)
    assert response.status_code == 200
    assert response.json()['title'] != pytest.target_dish_title
    assert response.json()['description'] != pytest.target_dish_description
    assert response.json()['price'] != pytest.target_dish_price
    assert response.json()['title'] == pytest.updated_dish_title
    assert response.json()['description'] == pytest.updated_dish_description
    assert response.json()['price'] == pytest.updated_dish_price


@pytest.mark.usefixtures('data')
def test_dish_remove():
    response = delete_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_id)
    assert response.status_code == 200


@pytest.mark.usefixtures('data')
def test_submenu_remove():
    response = delete_submenu(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200


@pytest.mark.usefixtures('data')
def test_menu_remove():
    response = delete_menu(pytest.target_menu_id)
    assert response.status_code == 200


@pytest.mark.usefixtures('data')
def test_menu_get_404():
    response = get_menu(pytest.target_menu_id)
    assert response.status_code == 404
    assert response.json()['detail'] == 'menu not found'


@pytest.mark.usefixtures('data')
def test_submenu_get_404():
    response = get_submenu(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 404
    assert response.json()['detail'] == 'submenu not found'


@pytest.mark.usefixtures('data')
def test_dish_get_404():
    response = get_dish(pytest.target_menu_id, pytest.target_submenu_id, pytest.target_dish_id)
    assert response.status_code == 404
    assert response.json()['detail'] == 'dish not found'


@pytest.mark.usefixtures('data')
def test_menu_get_all_empty():
    response = get_all_menus()
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.usefixtures('data')
def test_submenu_get_all_empty():
    response = get_all_submenus(pytest.target_menu_id)
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.usefixtures('data')
def test_dish_get_all_empty():
    response = get_all_dishes(pytest.target_menu_id, pytest.target_submenu_id)
    assert response.status_code == 200
    assert response.json() == []
