from data.submenu_repository import SubmenuRepository
from caching.cache import RedisCache
import json
from data.schemas import SubmenuBase

class SubmenuService:
    def __init__(self, session, r):
        self.submenu_repo = SubmenuRepository(session)
        self.session = session
        self.red = RedisCache(r)

    def get(self, submenu_id):
        if self.red.cache_get(submenu_id) is not None:
            print("Cache worked fine!")
            return self.red.cache_get(submenu_id)
        else:
            submenu = self.submenu_repo.get(submenu_id).dict()
            self.red.cache_set(submenu_id, json.dumps(submenu))
            return submenu

    def list(self, menu_id: str):
        redisstring = "submenus on menu id : " + menu_id
        print(redisstring)
        if self.red.cache_get(redisstring) is not None:
            print("Cache worked fine!")
            return self.red.cache_get(redisstring)
        else:
            submenus = self.submenu_repo.list(menu_id=menu_id)
            self.red.cache_set(redisstring, json.dumps(submenus))
            return submenus

    def add(self, menu_id: str, submenu: SubmenuBase):
        redisstring = "submenus on menu id : " + menu_id
        submenu = self.submenu_repo.add(menu_id = menu_id, title = submenu.title, description = submenu.description)
        self.session.commit()
        self.red.cache_delete("menus")
        self.red.cache_delete(redisstring)
        return submenu

    def update(self, menu_id: str, submenu_id: str, submenu: SubmenuBase):
        submenu = self.submenu_repo.update(menu_id = menu_id, submenu_id=submenu_id,
                                            title = submenu.title, description = submenu.description)
        redisstring = "submenus on menu id : " + menu_id
        self.red.cache_delete(redisstring)
        self.red.cache_delete(submenu_id)
        return submenu

    def delete(self, menu_id: str, submenu_id: str):
        submenu = self.submenu_repo.delete(submenu_id)
        self.red.cache_delete("menus")
        self.red.cache_delete("submenus on menu id : " + menu_id)
        self.red.cache_delete(submenu_id)
        self.red.cache_delete(menu_id)
        return submenu
