from api.models import Menu, Submenu, session
from api.schemas import SubmenuBase, SubmenuData
from api.utils import (count_for_many_submenus,
                       count_for_submenu, check_exception)

def get_all(target_menu_id:str):
    query = session.query(Submenu).filter_by(menu_id=target_menu_id)
    return count_for_many_submenus(query.all())
    
def get(target_submenu_id:str):
    query = check_exception(target_submenu_id=target_submenu_id)
    return count_for_submenu(SubmenuData(id = query.id, title = query.title, description = query.description))

def post(target_menu_id: str, submenu:SubmenuBase):
    check_exception(target_menu_id=target_menu_id)
    query = Submenu(**submenu.dict(), menu_id = target_menu_id)
    session.add(query)
    session.commit()
    return count_for_submenu(SubmenuData(id = query.id, title = query.title, description = query.description))

def patch(target_submenu_id: str, menu:SubmenuBase):
    query = check_exception(target_submenu_id=target_submenu_id)
    query.title = menu.title
    query.description = menu.description
    session.add(query)
    session.commit()
    return count_for_submenu(SubmenuData(id = query.id, title = query.title, description = query.description))

def delete(target_submenu_id: str):
    query = check_exception(target_submenu_id=target_submenu_id)
    title = query.title
    session.delete(query)
    session.commit()
    return {"submenu deleted": title}
    
