from fastapi import APIRouter

from data.models import session
from data.schemas import MenuBase
from data.menu_repository import *

router = APIRouter()

from redis_connection import r

from services.menu_service import MenuService

item = MenuService(session, r)

@router.get("/api/v1/menus/{menu_id}")
def menu_get(menu_id: str):
    return item.get(menu_id=menu_id)

@router.get("/api/v1/menus")
def menu_list():
    return item.list()

@router.post("/api/v1/menus", status_code=201)
def create_menu(menu: MenuBase):
    return item.add(menu)

@router.patch("/api/v1/menus/{target_menu_id}")
def menu_update(target_menu_id: str, menu: MenuBase):
    return item.update(target_menu_id, menu)

@router.delete("/api/v1/menus/{target_menu_id}")
def menu_delete(target_menu_id: str):
    return item.delete(target_menu_id)