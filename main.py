from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.models import Dish, Menu, Submenu, session
from app.schemas import DishBase, MenuBase, MenuData, SubmenuBase, SubmenuData
from app.utils import (count_for_many_menus, count_for_many_submenus,
                       count_for_menu, count_for_submenu)

app = FastAPI()

###МЕНЮ###

@app.get("/api/v1/menus")
async def get_all_menus():
    menu_query = session.query(Menu)
    n = count_for_many_menus(menu_query.all())
    return n

@app.get("/api/v1/menus/{menu_Id}", status_code=200)
async def get_target_menu(menu_Id: str):
    query = session.query(Menu).filter_by(id=menu_Id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="menu not found")
    data = MenuData(id = query.id, title = query.title, description = query.description)
    n = count_for_menu(data)
    return n

@app.post("/api/v1/menus", status_code=201)
async def create_menu(menu: MenuBase):
    new_menu = Menu(**menu.dict())
    session.add(new_menu)
    session.commit()
    data = {"id": new_menu.id, "title": new_menu.title, "description": new_menu.description}
    return data

@app.patch("/api/v1/menus/{menu_Id}")
async def patch_target_menu(menu_Id: str, menu:MenuBase):
    menu_query = session.query(Menu).filter_by(id=menu_Id).first()
    menu_query.title = menu.title
    menu_query.description = menu.description
    session.add(menu_query)
    session.commit()
    data = {"id": menu_query.id, "title": menu_query.title, "description": menu_query.description}
    return data

@app.delete("/api/v1/menus/{menu_Id}")
async def delete_target_menu(menu_Id: str):
    menu_query = session.query(Menu).filter_by(id=menu_Id).first()
    session.delete(menu_query)
    session.commit()
    return {"menu deleted": menu_query.title}

###ПОДМЕНЮ

@app.get("/api/v1/menus/{target_menu_id}/submenus")
async def get_all_submenus(target_menu_id: str):
    query = session.query(Submenu).filter_by(menu_id=target_menu_id)
    n = count_for_many_submenus(query.all())
    return n

@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}", status_code=200)
async def get_target_submenu(target_submenu_id: str):
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="submenu not found")
    data = SubmenuData(id = query.id, title = query.title, description = query.description)
    n = count_for_submenu(data)
    return n

@app.post("/api/v1/menus/{target_menu_id}/submenus", status_code=201)
async def create_submenu(target_menu_id: str, submenu:SubmenuBase):
    query = session.query(Menu).filter_by(id=target_menu_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="menu not found")
    new_submenu = Submenu(**submenu.dict(), menu_id = target_menu_id)
    session.add(new_submenu)
    session.commit()
    data = {"id": new_submenu.id, "title": new_submenu.title, "description": new_submenu.description}
    return data

@app.patch("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}")
async def patch_target_menu(target_menu_id: str, target_submenu_id: str, menu:SubmenuBase):
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="submenu not found")
    menu_query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    menu_query.title = menu.title
    menu_query.description = menu.description
    session.add(menu_query)
    session.commit()
    data = {"id": menu_query.id, "title": menu_query.title, "description": menu_query.description}
    return data

@app.delete("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}")
async def delete_target_submenu(target_submenu_id: str):
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="submenu not found")
    menu_query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    session.delete(menu_query)
    session.commit()
    return {"submenu deleted": menu_query.title}

## БЛЮДА

@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes")
async def get_all_dishes(target_submenu_id: str):
    query = session.query(Dish).filter_by(submenu_id=target_submenu_id)
    return query.all()

@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}", status_code=200)
async def get_target_dish(target_dish_id: str):
    query = session.query(Dish).filter_by(id=target_dish_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="dish not found")
    return query

@app.post("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes", status_code=201)
async def create_dish(target_menu_id: str, target_submenu_id: str, dish:DishBase):
    query = session.query(Submenu).filter_by(id=target_submenu_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="submenu not found")
    new_submenu = Dish(**dish.dict(), menu_id = target_menu_id, submenu_id = target_submenu_id)
    session.add(new_submenu)
    session.commit()
    data = {"id": new_submenu.id, "title": new_submenu.title, "description": new_submenu.description, "price" : new_submenu.price}
    return data

@app.patch("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}")
async def patch_target_menu(target_dish_id: str, dish:DishBase):
    query = session.query(Dish).filter_by(id=target_dish_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="dish not found")
    query = session.query(Dish).filter_by(id=target_dish_id).first()
    query.title = dish.title
    query.description = dish.description
    query.price = dish.price
    
    session.add(query)
    session.commit()
    data = {"id": query.id, "title": query.title, "description": query.description, "price" : query.price}
    return data

@app.delete("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}")
async def delete_target_submenu(target_dish_id: str):
    query = session.query(Dish).filter_by(id=target_dish_id).first()
    if query == None:
        raise HTTPException(status_code=404, detail="dish not found")
    query = session.query(Dish).filter_by(id=target_dish_id).first()
    session.delete(query)
    session.commit()
    return {"dish deleted": query.title}