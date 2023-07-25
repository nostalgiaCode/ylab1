from fastapi import HTTPException

from api.models import Dish, Submenu, session
from api.schemas import DishBase, DishSchema
from api.utils import (fix_dish_price, fix_dishes_price)

def get_all(target_submenu_id: str):
    query = session.query(Dish).filter_by(submenu_id=target_submenu_id)
    return fix_dishes_price(query.all())

def get(target_dish_id: str):
    query = session.query(Dish).filter_by(id=target_dish_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="dish not found")
    data = DishSchema(id = query.id, price = query.price, title = query.title, description = query.description)
    return fix_dish_price(data)

def post(target_menu_id: str, target_submenu_id: str, dish:DishBase):
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="submenu not found")
    new_dish = Dish(**dish.dict(), menu_id = target_menu_id, submenu_id = target_submenu_id)
    session.add(new_dish)
    session.commit()
    data = DishSchema(id = new_dish.id, price = new_dish.price, title = new_dish.title, description = new_dish.description)
    return fix_dish_price(data)

def patch(target_dish_id: str, dish:DishBase):
    query = session.query(Dish).filter_by(id=target_dish_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="dish not found")
    query = session.query(Dish).filter_by(id=target_dish_id).first()
    query.title = dish.title
    query.description = dish.description
    query.price = dish.price
    
    session.add(query)
    session.commit()
    data = DishSchema(id = query.id, price = query.price, title = query.title, description = query.description)
    return fix_dish_price(data)

def delete(target_dish_id):
    query = session.query(Dish).filter_by(id=target_dish_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="dish not found")
    title = query.title
    session.delete(query)
    session.commit()
    return {"dish deleted": title}