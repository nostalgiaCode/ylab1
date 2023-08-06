import pytest


@pytest.fixture(scope='session')
def data():
    pytest.target_menu_id = None
    pytest.target_menu_title = 'My menu 1'
    pytest.target_menu_description = 'My menu description 1'
    pytest.updated_menu_title = 'My updated menu 1'
    pytest.updated_menu_description = 'My updated menu description 1'

    pytest.target_submenu_id = None
    pytest.target_submenu_title = 'My submenu 1'
    pytest.target_submenu_description = 'My submenu description 1'
    pytest.updated_submenu_title = 'My updated submenu 1'
    pytest.updated_submenu_description = 'My updated submenu description 1'

    pytest.target_dish_id = None
    pytest.target_dish_1_id = None
    pytest.target_dish_2_id = None
    pytest.target_dish_title = 'My dish 1'
    pytest.target_dish_description = 'My dish description 1'
    pytest.target_dish_price = '12.50'
    pytest.updated_dish_title = 'My updated dish 1'
    pytest.updated_dish_description = 'My updated dish description 1'
    pytest.updated_dish_price = '14.50'
