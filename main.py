from fastapi import FastAPI

from api.schemas import DishBase, MenuBase, SubmenuBase

import api.crud.menu
import api.crud.submenu
import api.crud.dish

app = FastAPI()

###МЕНЮ###

@app.get("/api/v1/menus")
async def get_all_menus():
    return api.crud.menu.get_all()

@app.get("/api/v1/menus/{target_menu_id}", status_code=200)
async def get_target_menu(target_menu_id: str):
    return api.crud.menu.get(target_menu_id)

@app.post("/api/v1/menus", status_code=201)
async def create_menu(menu: MenuBase):
    return api.crud.menu.post(menu)

@app.patch("/api/v1/menus/{target_menu_id}")
async def patch_target_menu(target_menu_id: str, menu:MenuBase):
    return api.crud.menu.patch(target_menu_id, menu)

@app.delete("/api/v1/menus/{target_menu_id}")
async def delete_target_menu(target_menu_id: str):
    return api.crud.menu.delete(target_menu_id)

###ПОДМЕНЮ

@app.get("/api/v1/menus/{target_menu_id}/submenus")
async def get_all_submenus(target_menu_id: str):
    return api.crud.submenu.get_all(target_menu_id)

@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}", status_code=200)
async def get_target_submenu(target_submenu_id: str):
    return api.crud.submenu.get(target_submenu_id)

@app.post("/api/v1/menus/{target_menu_id}/submenus", status_code=201)
async def create_submenu(target_menu_id: str, submenu:SubmenuBase):
    return api.crud.submenu.post(target_menu_id, submenu)

@app.patch("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}")
async def patch_target_menu(target_submenu_id: str, menu:SubmenuBase):
    return api.crud.submenu.patch(target_submenu_id, menu)

@app.delete("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}")
async def delete_target_submenu(target_submenu_id: str):
    return api.crud.submenu.delete(target_submenu_id)

## БЛЮДА

@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes")
async def get_all_dishes(target_submenu_id: str):
    return api.crud.dish.get_all(target_submenu_id)

@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}", status_code=200)
async def get_target_dish(target_dish_id: str):
    return api.crud.dish.get(target_dish_id)

@app.post("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes", status_code=201)
async def create_dish(target_menu_id: str, target_submenu_id: str, dish:DishBase):
    return api.crud.dish.post(target_menu_id, target_submenu_id, dish)

@app.patch("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}")
async def patch_target_menu(target_dish_id: str, dish:DishBase):
    return api.crud.dish.patch(target_dish_id, dish)

@app.delete("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}")
async def delete_target_submenu(target_dish_id: str):
    return api.crud.dish.delete(target_dish_id)