import json

from caching.cache import RedisRepo
from data.menu_repository import MenuRepository
from data.schemas import MenuBase, MenuSchema


class MenuService:
    def __init__(self, session, r):
        self.menu_repo = MenuRepository(session)
        self.session = session

        self.red = RedisRepo(r)

    def get(self, menu_id) -> dict:
        try:
            if self.red.read(menu_id) is not None:
                return self.red.read(menu_id)
            else:
                menu = self.menu_repo.get(menu_id)
                self.red.save_menu(menu_id, json.dumps(menu))
                return menu
        except Exception:
            menu = self.menu_repo.get(menu_id)
            return menu

    def list(self) -> list:
        try:
            if self.red.read('menus') is not None:
                return self.red.read('menus')
            else:
                menus = self.menu_repo.list()
                self.red.save_menu('menus', json.dumps(menus))
                return menus
        except Exception:
            menus = self.menu_repo.list()
            return menus

    def add(self, menubase: MenuBase) -> MenuSchema:
        menu = self.menu_repo.add(title=menubase.title, description=menubase.description)
        try:
            self.red.save_menu(menu.id, json.dumps(menu.serialize()))
        except Exception:
            pass
        return menu.schema()

    def update(self, menu_id: str, menu: MenuBase) -> MenuSchema:
        menu = self.menu_repo.update(menu_id=menu_id, title=menu.title, description=menu.description)
        try:
            self.red.save_menu(menu.id, json.dumps(menu.serialize()))
        except Exception:
            pass
        return menu.schema()

    def delete(self, menu_id: str) -> dict:
        menu = self.menu_repo.delete(menu_id)
        try:
            self.red.invalidate_menu(menu_id)
        except Exception:
            pass
        return menu
