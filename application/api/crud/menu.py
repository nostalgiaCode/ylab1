from api.models import Menu, session
from api.schemas import MenuBase, MenuData
from api.utils import (count_for_many_menus,
                       count_for_menu, check_exception)

def get_all():
    menu_query = session.query(Menu)
    return count_for_many_menus(menu_query.all())
    
def get(target_menu_id: str):
    query = check_exception(target_menu_id)
    return count_for_menu(MenuData(id = query.id, title = query.title, description = query.description))

def post(menu: MenuBase):
    query = Menu(**menu.dict())
    session.add(query)
    session.commit()
    return count_for_menu(MenuData(id = query.id, title = query.title, description = query.description))

def patch(target_menu_id: str, menu:MenuBase):
    query = check_exception(target_menu_id)
    query.title = menu.title
    query.description = menu.description
    session.add(query)
    session.commit()
    return count_for_menu(MenuData(id = query.id, title = query.title, description = query.description))

def delete(target_menu_id: str):
    query = check_exception(target_menu_id)
    title = query.title
    session.delete(query)
    session.commit()
    return {"menu deleted": title}
    
