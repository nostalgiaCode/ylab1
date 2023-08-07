from data.models import session
from data.schemas import SubmenuBase, SubmenuSchema
from fastapi import APIRouter
from redis_connection import r
from services.submenu_service import SubmenuService

router = APIRouter()


item = SubmenuService(session, r)


@router.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}', status_code=200, response_model=dict)
def submenu_get(menu_id: str, submenu_id: str):
    return item.get(menu_id=menu_id, submenu_id=submenu_id)


@router.get('/api/v1/menus/{menu_id}/submenus', response_model=list)
def submenu_list(menu_id: str):
    return item.list(menu_id=menu_id)


@router.post('/api/v1/menus/{menu_id}/submenus', status_code=201, response_model=dict)
def submenu_add(menu_id: str, submenubase: SubmenuBase):
    return item.add(menu_id=menu_id, submenubase=submenubase)


@router.patch('/api/v1/menus/{menu_id}/submenus/{submenu_id}', response_model=SubmenuSchema)
def submenu_update(menu_id: str, submenu_id: str, submenu: SubmenuBase):
    return item.update(menu_id=menu_id, submenu_id=submenu_id, submenu=submenu)


@router.delete('/api/v1/menus/{menu_id}/submenus/{submenu_id}', response_model=dict)
def submenu_delete(menu_id: str, submenu_id: str):
    return item.delete(menu_id=menu_id, submenu_id=submenu_id)
