import json

import redis  # type: ignore


def keygenerator(key: str, key2: None | str = None, key3: None | str = None) -> str:
    if key2 is None and key3 is None:
        return key
    elif key3 is None:
        return f'{key}:{key2}'
    else:
        return f'{key}:{key2}:{key3}'


class RedisBase:
    def __init__(self, redis: redis.Redis):
        self.r = redis
        self.tte = 30

    def delete(self, key: str):
        self.r.delete(key)

    def delete_all(self, key: str):
        for key in self.r.scan_iter(f'*{key}*'):
            self.r.delete(key)

    def read(self, key: str, key2: None | str = None, key3: None | str = None) -> bytes | float | int | str | None:
        key = keygenerator(key=key, key2=key2, key3=key3)
        value = self.r.get(key)
        if value is not None:
            return json.loads(value)
        else:
            return None

    # def save(self, key: str, json_object: json):
    def save(self, key: str, json_object: bytes | float | int | str):
        self.r.set(key, json_object)


class Invalidate(RedisBase):
    def invalidate_menu(self, menu_id: str):
        self.delete_all(menu_id)
        self.delete('menus')

    def invalidate_submenu(self, menu_id: str, submenu_id: str):
        self.delete(menu_id)
        self.delete(f'{menu_id}:submenus')
        self.delete_all(submenu_id)

    def invalidate_dish(self, menu_id: str, submenu_id: str, dish_id: str):
        self.delete(menu_id)
        self.delete(submenu_id)
        self.delete(f'{menu_id}:{submenu_id}:dishes')
        self.delete_all(dish_id)


class RedisRepo(Invalidate):
    def save_menu(self, menu_id: str, json_object: bytes | float | int | str):
        key = f'{menu_id}'
        self.invalidate_menu('menus')
        self.save(key, json_object)

    def save_submenu(self, menu_id: str, submenu_id: str, json_object: bytes | float | int | str):
        key = f'{menu_id}:{submenu_id}'
        self.save(key, json_object)
        self.invalidate_menu(menu_id)

    def save_dish(self, menu_id: str, submenu_id: str, dish_id: str, json_object: bytes | float | int | str):
        key = f'{menu_id}:{submenu_id}:{dish_id}'
        self.save(key, json_object)
        self.invalidate_submenu(menu_id, submenu_id)
