from api.models import Dish, Submenu, session
from api.schemas import DishBase, DishSchema
from api.utils import (fix_dish_price, fix_dishes_price, check_exception)

def get_all(target_submenu_id: str):
    return fix_dishes_price(session.query(Dish).filter_by(submenu_id=target_submenu_id).all())

def get(target_dish_id: str):
    query = check_exception(target_dish_id=target_dish_id)
    return fix_dish_price(DishSchema(id = query.id, price = query.price, title = query.title, description = query.description))

def post(target_menu_id: str, target_submenu_id: str, dish:DishBase):
    check_exception(target_submenu_id=target_submenu_id)
    new_dish = Dish(**dish.dict(), menu_id = target_menu_id, submenu_id = target_submenu_id)
    session.add(new_dish)
    session.commit()
    return fix_dish_price(DishSchema(id = new_dish.id, price = new_dish.price, title = new_dish.title, description = new_dish.description))

def patch(target_dish_id: str, dish:DishBase):
    query = check_exception(target_dish_id=target_dish_id)
    query.title = dish.title
    query.description = dish.description
    query.price = dish.price
    
    session.add(query)
    session.commit()
    return fix_dish_price(DishSchema(id = query.id, price = query.price, title = query.title, description = query.description))

def delete(target_dish_id):
    query = check_exception(target_dish_id=target_dish_id)
    title = query.title
    session.delete(query)
    session.commit()
    return {"dish deleted": title}