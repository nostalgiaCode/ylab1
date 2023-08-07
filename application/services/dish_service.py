import json

from caching.cache import RedisRepo
from data.dish_repository import DishRepository
from data.schemas import DishBase, DishSchema


class DishService:
    def __init__(self, session, r):
        self.dish_repo = DishRepository(session)
        self.session = session
        self.red = RedisRepo(r)

    def get(self, menu_id: str, submenu_id: str, dish_id: str) -> dict:
        if self.red.read(key=menu_id, key2=submenu_id, key3=dish_id) is not None:
            print('Cache worked fine!')
            return self.red.read(key=menu_id, key2=submenu_id, key3=dish_id)
        else:
            dish = self.dish_repo.get(dish_id)
            self.red.save_dish(menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id, json_object=json.dumps(dish))
            return dish

    def list(self, menu_id: str, submenu_id: str) -> list:
        rstring = f'{menu_id}:{submenu_id}:submenus'
        if self.red.read(rstring) is not None:
            print('Cache worked fine!')
            return self.red.read(rstring)
        else:
            dishes = self.dish_repo.list(submenu_id=submenu_id)
            self.red.save_dish(menu_id=menu_id, submenu_id=submenu_id, dish_id='dishes', json_object=json.dumps(dishes))
            return dishes

    def add(self, menu_id: str, submenu_id: str, dishbase: DishBase) -> DishSchema:
        dish = self.dish_repo.add(menu_id=menu_id, submenu_id=submenu_id, title=dishbase.title,
                                  description=dishbase.description, price=dishbase.price)
        self.red.save_dish(menu_id=menu_id, submenu_id=submenu_id, dish_id=dish.id,
                           json_object=json.dumps(dish.serialize()))
        return dish.schema()

    def update(self, menu_id: str, submenu_id: str, dish_id: str, dishbase: DishBase) -> DishSchema:
        dish = self.dish_repo.update(menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id,
                                     title=dishbase.title, description=dishbase.description, price=dishbase.price)
        self.red.save_dish(menu_id=menu_id, submenu_id=submenu_id, dish_id=dish.id,
                           json_object=json.dumps(dish.serialize()))
        return dish.schema()

    def delete(self, menu_id: str, submenu_id: str, dish_id: str) -> dict:
        dish = self.dish_repo.delete(dish_id)
        self.red.invalidate_dish(menu_id=menu_id, submenu_id=submenu_id, dish_id=dish_id)
        return dish
