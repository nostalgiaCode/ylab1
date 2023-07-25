from api.models import Dish, Menu, Submenu, session
from api.schemas import MenuData, MenuSchema, SubmenuData, SubmenuSchema, DishBase, DishSchema
from fastapi import HTTPException

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

def fix_dish_price(item: DishSchema):
    item.price = str(format(float(item.price), '.2f')) 
    return DishSchema(**item.dict())

def fix_dishes_price(list):
    l = []
    for item in list:
        l.append(fix_dish_price(DishSchema(id = item.id, price = item.price, description = item.description, title = item.title)))
    return l

def check_exception(target_menu_id=None, target_submenu_id=None, target_dish_id=None):
    if target_menu_id is not None:
        query = session.query(Menu).filter_by(id=target_menu_id).first()
        if query == None:
            raise HTTPException(status_code=404, detail="menu not found")
        return query
    elif target_submenu_id is not None:
        query = session.query(Submenu).filter_by(id=target_submenu_id).first()
        if query == None:
            raise HTTPException(status_code=404, detail="submenu not found")
        return query
    elif target_dish_id is not None:
        query = session.query(Dish).filter_by(id=target_dish_id).first()
        if query == None:
            raise HTTPException(status_code=404, detail="dish not found")
        return query

