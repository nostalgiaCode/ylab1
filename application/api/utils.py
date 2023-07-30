from api.models import Dish, Menu, Submenu, session
from fastapi import HTTPException

def check_exception(target_menu_id=None, target_submenu_id=None, target_dish_id=None):
    if target_menu_id is not None:
        query = session.query(Menu).filter_by(id=target_menu_id).first()
        if query == None:
            raise HTTPException(status_code=404, detail="menu not found")
    elif target_submenu_id is not None:
        query = session.query(Submenu).filter_by(id=target_submenu_id).first()
        if query == None:
            raise HTTPException(status_code=404, detail="submenu not found")
    elif target_dish_id is not None:
        query = session.query(Dish).filter_by(id=target_dish_id).first()
        if query == None:
            raise HTTPException(status_code=404, detail="dish not found")

