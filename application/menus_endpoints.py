from data.models import session
from data.schemas import MenuBase, MenuSchema
from fastapi import APIRouter
from redis_connection import r
from services.menu_service import MenuService

router = APIRouter()


item = MenuService(session, r)


@router.get('/api/v1/menus/{menu_id}', response_model=dict)
def menu_get(menu_id: str):
    return item.get(menu_id=menu_id)


@router.get('/api/v1/menus', response_model=list)
def menu_list():
    return item.list()


@router.post('/api/v1/menus', status_code=201, response_model=dict)
def create_menu(menu: MenuBase):
    return item.add(menu)


@router.patch('/api/v1/menus/{menu_id}', response_model=MenuSchema)
def menu_update(menu_id: str, menu: MenuBase):
    return item.update(menu_id, menu)


@router.delete('/api/v1/menus/{menu_id}', response_model=dict)
def menu_delete(menu_id: str):
    return item.delete(menu_id)
