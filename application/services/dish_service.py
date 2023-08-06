from data.dish_repository import DishRepository
from caching.cache import RedisCache
import json
from data.schemas import DishBase


class DishService:
    def __init__(self, session, r): #
        self.dish_repo = DishRepository(session)
        self.session = session
        self.red = RedisCache(r)
 
    def get(self, dish_id): #
        if self.red.cache_get(dish_id) is not None:
            print("Cache worked fine!")
            return self.red.cache_get(dish_id)
        else:
            dish = self.dish_repo.get(dish_id).dict()
            self.red.cache_set(dish_id, json.dumps(dish))
            return dish

    def list(self, submenu_id: str): #
        redisstring = "dishes on submenu id : " + submenu_id
        if self.red.cache_get(redisstring) is not None:
            print("Cache worked fine!")
            return self.red.cache_get(redisstring)
        else:
            dishes = self.dish_repo.list(submenu_id=submenu_id)
            self.red.cache_set(redisstring, json.dumps(dishes))
            return dishes

    def add(self, menu_id: str, submenu_id: str, dish: DishBase): #
        dish = self.dish_repo.add(menu_id = menu_id, submenu_id=submenu_id, title = dish.title, description = dish.description, price=dish.price)
        self.session.commit()
        ###
        self.red.cache_delete("menus")
        self.red.cache_delete(menu_id)
        self.red.cache_delete("submenus on menu id : " + menu_id)
        self.red.cache_delete("dishes on submenu id : " + submenu_id)
        return dish

    def update(self, menu_id: str, submenu_id: str, dish_id: str, dish: DishBase): #
        dish = self.dish_repo.update(menu_id = menu_id, submenu_id=submenu_id, dish_id=dish_id,
                                            title = dish.title, description = dish.description, price=dish.price)
        self.red.cache_delete("menus")
        self.red.cache_delete(menu_id)
        self.red.cache_delete("submenus on menu id : " + menu_id)
        self.red.cache_delete("dishes on submenu id : " + submenu_id)
        self.red.cache_delete(dish_id)
        return dish

    def delete(self, menu_id: str, submenu_id: str, dish_id: str):
        dish = self.dish_repo.delete(dish_id)
        self.red.cache_delete("menus")
        self.red.cache_delete(menu_id)
        self.red.cache_delete("submenus on menu id : " + menu_id)
        self.red.cache_delete("dishes on submenu id : " + submenu_id)
        self.red.cache_delete(dish_id)
        return dish
