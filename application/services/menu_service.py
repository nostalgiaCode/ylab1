from data.menu_repository import MenuRepository
from caching.cache import RedisCache
import json
from data.schemas import MenuBase

class MenuService:
    def __init__(self, session, r):
        self.menu_repo = MenuRepository(session)
        self.session = session
        self.red = RedisCache(r)

    def get(self, menu_id):
        if self.red.cache_get(menu_id) is not None:
            print("Cache worked fine!")
            return self.red.cache_get(menu_id)
        else:
            menu = self.menu_repo.get(menu_id).dict()
            self.red.cache_set(menu_id, json.dumps(menu))
            return menu

    def list(self):
        if self.red.cache_get("menus") is not None:
            print("Cache worked fine!")
            return self.red.cache_get("menus")
        else:
            menus = self.menu_repo.list()
            self.red.cache_set("menus", json.dumps(menus))
            return menus

    def add(self, menu: MenuBase):
        menu = self.menu_repo.add(title = menu.title, description = menu.description)
        self.session.commit()
        self.red.cache_delete("menus")

        return menu

    def update(self, target_menu_id: str, menu: MenuBase):
        menu = self.menu_repo.update(target_menu_id, title = menu.title, description = menu.description)

        self.red.cache_delete("menus")
        self.red.cache_delete(target_menu_id)

        return menu

    def delete(self, target_menu_id: str):
        menu = self.menu_repo.delete(target_menu_id)

        self.red.cache_delete("menus")
        self.red.cache_delete(target_menu_id)

        return menu
