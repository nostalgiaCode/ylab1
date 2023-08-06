from data.models import session
from data.schemas import SubmenuBase
from data.submenu_repository import *

from fastapi import APIRouter

router = APIRouter()

from redis_connection import r

from services.submenu_service import SubmenuService

item = SubmenuService(session, r)


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}", status_code=200) # +
def submenu_get(menu_id: str, submenu_id: str):
    return item.get(submenu_id=submenu_id)

@router.get("/api/v1/menus/{menu_id}/submenus") # +
def submenu_list(menu_id: str):
    return item.list(menu_id=menu_id)

@router.post("/api/v1/menus/{menu_id}/submenus", status_code=201) # +
def submenu_add(menu_id: str, submenu: SubmenuBase):
    return item.add(menu_id=menu_id, submenu=submenu)

@router.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}") # +
def submenu_update(menu_id: str, submenu_id: str, submenu:SubmenuBase):
    return item.update(menu_id=menu_id, submenu_id=submenu_id, submenu=submenu)

@router.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}")
def submenu_delete(menu_id: str, submenu_id: str):
    return item.delete(menu_id=menu_id, submenu_id=submenu_id)