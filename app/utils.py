from app.schemas import MenuData, MenuSchema, SubmenuData, SubmenuSchema
from app.models import Menu, Submenu, Dish, session

def count_for_menu(data: MenuData):
    submenus = session.query(Submenu).filter_by(menu_id=data.id)
    dishes = session.query(Dish).filter_by(menu_id=data.id)
    number_of_submenus = submenus.count()
    number_of_dishes = dishes.count()
    return MenuSchema(**data.dict(), submenus_count = number_of_submenus, dishes_count = number_of_dishes)

def count_for_many_menus(list):
    l = []
    for item in list:
        l.append(count_for_menu(MenuData(id = item.id, description = item.description, title = item.title)))
    return l

def count_for_submenu(data: SubmenuData):
    dishes = session.query(Dish).filter_by(submenu_id=data.id)
    number = dishes.count()
    return SubmenuSchema(**data.dict(), dishes_count = number)

def count_for_many_submenus(list):
    l = []
    for item in list:
        l.append(count_for_submenu(SubmenuData(id = item.id, description = item.description, title = item.title)))
    return l