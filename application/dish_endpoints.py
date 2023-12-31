from data.models import session
from data.schemas import DishBase, DishSchema
from fastapi import APIRouter
from redis_connection import r
from services.dish_service import DishService

router = APIRouter()


item = DishService(session, r)


@router.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', status_code=200, response_model=dict)
def dish_get(menu_id: str, submenu_id: str, dish_id: str):
    return item.get(menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id)


@router.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes', response_model=list)
def dishes_list(menu_id: str, submenu_id: str):
    return item.list(menu_id=menu_id, submenu_id=submenu_id)


@router.post('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes', status_code=201, response_model=dict)
def submenu_add(menu_id: str, submenu_id: str, dishbase: DishBase):
    return item.add(menu_id=menu_id, submenu_id=submenu_id, dishbase=dishbase)


@router.patch('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=DishSchema)
def submenu_update(menu_id: str, submenu_id: str, dish_id: str, dishbase: DishBase):
    return item.update(menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id, dishbase=dishbase)


@router.delete('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=dict)
def submenu_delete(menu_id: str, submenu_id: str, dish_id: str):
    return item.delete(menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id)
