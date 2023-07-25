from fastapi import HTTPException

from api.models import Menu, Submenu, session
from api.schemas import SubmenuBase, SubmenuData
from api.utils import (count_for_many_submenus,
                       count_for_submenu)

def get_all(target_menu_id:str):
    query = session.query(Submenu).filter_by(menu_id=target_menu_id)
    return count_for_many_submenus(query.all())
    
def get(target_submenu_id:str):
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()###
    if query == None:
        raise HTTPException(status_code=404, detail="submenu not found")
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    data = SubmenuData(id = query.id, title = query.title, description = query.description)
    return count_for_submenu(data)

def post(target_menu_id: str, submenu:SubmenuBase):
    query = session.query(Menu).filter_by(id=target_menu_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="menu not found")
    query = Submenu(**submenu.dict(), menu_id = target_menu_id)
    session.add(query)
    session.commit()
    data = SubmenuData(id = query.id, title = query.title, description = query.description)
    return count_for_submenu(data)

def patch(target_submenu_id: str, menu:SubmenuBase):
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="submenu not found")
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    query.title = menu.title
    query.description = menu.description
    session.add(query)
    session.commit()
    data = SubmenuData(id = query.id, title = query.title, description = query.description)
    return count_for_submenu(data)

def delete(target_submenu_id: str):
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="submenu not found")
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    title = query.title
    session.delete(query)
    session.commit()
    return {"submenu deleted": title}
    
