from data.models import Dish, Menu, Submenu, session
from fastapi import HTTPException


def check_exception(menu_id=None, submenu_id=None, dish_id=None) -> None:
    if menu_id is not None:
        query = session.query(Menu).filter_by(id=menu_id).first()
        if query is None:
            raise HTTPException(status_code=404, detail='menu not found')
    elif submenu_id is not None:
        query = session.query(Submenu).filter_by(id=submenu_id).first()
        if query is None:
            raise HTTPException(status_code=404, detail='submenu not found')
    elif dish_id is not None:
        query = session.query(Dish).filter_by(id=dish_id).first()
        if query is None:
            raise HTTPException(status_code=404, detail='dish not found')
