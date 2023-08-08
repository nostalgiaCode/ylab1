import json

from caching.cache import RedisRepo
from data.schemas import SubmenuBase, SubmenuSchema
from data.submenu_repository import SubmenuRepository


class SubmenuService:
    def __init__(self, session, r):
        self.submenu_repo = SubmenuRepository(session)
        self.session = session

        self.red = RedisRepo(r)

    def get(self, menu_id: str, submenu_id) -> dict:
        try:
            if self.red.read(key=menu_id, key2=submenu_id) is not None:
                print('Cache worked fine!')
                return self.red.read(menu_id=menu_id, submenu_id=submenu_id)
            else:
                submenu = self.submenu_repo.get(submenu_id)
                self.red.save_submenu(menu_id=menu_id, submenu_id=submenu_id, json_object=json.dumps(submenu))
                return submenu
        except Exception:
            submenu = self.submenu_repo.get(submenu_id)
            return submenu

    def list(self, menu_id: str) -> list:
        try:
            rstring = f'{menu_id}:submenus'
            if self.red.read(rstring) is not None:
                print('Cache worked fine!')
                return self.red.read(rstring)
            else:
                submenus = self.submenu_repo.list(menu_id=menu_id)
                self.red.save_submenu(menu_id=menu_id, submenu_id='submenus', json_object=json.dumps(submenus))
                return submenus
        except Exception:
            submenus = self.submenu_repo.list(menu_id=menu_id)
            return submenus

    def add(self, menu_id: str, submenubase: SubmenuBase) -> SubmenuSchema:
        submenu = self.submenu_repo.add(menu_id=menu_id, title=submenubase.title, description=submenubase.description)
        try:
            self.red.save_submenu(menu_id=menu_id, submenu_id=submenu.id, json_object=json.dumps(submenu.serialize()))
        except Exception:
            pass
        return submenu.schema()

    def update(self, menu_id: str, submenu_id: str, submenu: SubmenuBase) -> SubmenuSchema:
        submenu = self.submenu_repo.update(menu_id=menu_id, submenu_id=submenu_id,
                                           title=submenu.title, description=submenu.description)
        try:
            self.red.save_submenu(menu_id=menu_id, submenu_id=submenu.id, json_object=json.dumps(submenu.serialize()))
        except Exception:
            pass
        return submenu.schema()

    def delete(self, menu_id: str, submenu_id: str) -> dict:
        submenu = self.submenu_repo.delete(submenu_id)
        try:
            self.red.invalidate_submenu(menu_id=menu_id, submenu_id=submenu_id)
        except Exception:
            pass
        return submenu
