from api.models import Menu, session
from api.schemas import MenuBase
from api.utils import check_exception

def get_all():
    all_menus = session.query(Menu).all()
    return [get(all_menus[index].id) for index in range(len(all_menus))]
    
def get(target_menu_id: str):
    check_exception(target_menu_id)
    menu = session.query(Menu).filter_by(id=target_menu_id).first()
    # return MenuSchema(id = menu.id, title = menu.title, description = menu.description, 
    #                   submenus_count = session.query(Submenu).filter(Menu.id==menu.id).join(Menu.submenu).count(), 
    #                   dishes_count = session.query(Dish).filter(Menu.id==menu.id).join(Menu.submenu).join(Submenu.dish).count())
    return menu.make_response()

def post(input: MenuBase): 
    menu = Menu(**input.dict())
    session.add(menu)
    session.commit()
    # return MenuSchema(id = menu.id, title = menu.title, description = menu.description, 
    #                   submenus_count = session.query(Submenu).filter(Menu.id==menu.id).join(Menu.submenu).count(), 
    #                   dishes_count = session.query(Dish).filter(Menu.id==menu.id).join(Menu.submenu).join(Submenu.dish).count())
    return menu.make_response()

def patch(target_menu_id: str, input:MenuBase):
    check_exception(target_menu_id)
    menu = session.query(Menu).filter_by(id=target_menu_id).first()
    menu.title = input.title
    menu.description = input.description
    session.add(menu)
    session.commit()
    # return MenuSchema(id = menu.id, title = menu.title, description = menu.description, 
    #                   submenus_count = session.query(Submenu).filter(Menu.id==menu.id).join(Menu.submenu).count(), 
    #                   dishes_count = session.query(Dish).filter(Menu.id==menu.id).join(Menu.submenu).join(Submenu.dish).count())
    return menu.make_response()

def delete(target_menu_id: str):
    check_exception(target_menu_id)
    menu = session.query(Menu).filter_by(id=target_menu_id).first()
    title = menu.title
    session.delete(menu)
    session.commit()
    return {"menu deleted": title}
    
