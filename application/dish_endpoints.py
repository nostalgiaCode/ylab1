from data.models import session
from data.schemas import DishBase
from data.dish_repository import *

from fastapi import APIRouter

router = APIRouter()

from redis_connection import r

from services.dish_service import DishService

item = DishService(session, r)


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", status_code=200) #
def dish_get(menu_id: str, submenu_id: str, dish_id: str):
    return item.get(dish_id=dish_id)

@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes") #
def dishes_list(menu_id: str, submenu_id: str):
    return item.list(submenu_id=submenu_id)

@router.post("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes", status_code=201) #
def submenu_add(menu_id: str, submenu_id: str, dish: DishBase):
    return item.add(menu_id=menu_id, submenu_id=submenu_id, dish=dish)

@router.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}") #
def submenu_update(menu_id: str, submenu_id: str, dish_id: str, dish:DishBase):
    return item.update(menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id, dish=dish)

@router.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def submenu_delete(menu_id: str, submenu_id: str, dish_id: str):
    return item.delete(menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id)