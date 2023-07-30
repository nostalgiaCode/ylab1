from api.models import Submenu, session
from api.schemas import SubmenuBase
from api.utils import check_exception

def get_all(target_menu_id:str):
    all_submenus = session.query(Submenu).filter_by(menu_id=target_menu_id).all()
    return [get(all_submenus[index].id) for index in range(len(all_submenus))]
    
def get(target_submenu_id:str):
    check_exception(target_submenu_id=target_submenu_id)
    submenu = session.query(Submenu).filter_by(id=target_submenu_id).first()
    # return SubmenuSchema(id = submenu.id, title = submenu.title, description = submenu.description, 
    #                   dishes_count = session.query(Dish).filter(Submenu.id==submenu.id).join(Submenu.dish).count())
    return submenu.make_response()

def post(target_menu_id: str, input:SubmenuBase):
    check_exception(target_menu_id=target_menu_id)
    submenu = Submenu(**input.dict(), menu_id = target_menu_id)
    session.add(submenu)
    session.commit()
    # return SubmenuSchema(id = input.id, title = input.title, description = input.description, 
    #                   dishes_count = session.query(Dish).filter(Submenu.id==input.id).join(Submenu.dish).count())
    return submenu.make_response()

def patch(target_submenu_id: str, input:SubmenuBase):
    check_exception(target_submenu_id=target_submenu_id)
    submenu = session.query(Submenu).filter_by(id=target_submenu_id).first()
    submenu.title = input.title
    submenu.description = input.description
    session.add(submenu)
    session.commit()
    # return SubmenuSchema(id = submenu.id, title = submenu.title, description = submenu.description, 
    #                   dishes_count = session.query(Dish).filter(Submenu.id==submenu.id).join(Submenu.dish).count())
    return submenu.make_response()

def delete(target_submenu_id: str):
    check_exception(target_submenu_id=target_submenu_id)
    submenu = session.query(Submenu).filter_by(id=target_submenu_id).first()
    title = submenu.title
    session.delete(submenu)
    session.commit()
    return {"submenu deleted": title}
    
