from data.models import Menu as MenuDB
from utils.additional_methods import check_exception


class MenuRepository:
    def __init__(self, session):
        self.session = session

    def get(self, menu_id: str) -> dict:
        check_exception(menu_id=menu_id)
        menu = self.session.query(MenuDB).filter_by(id=menu_id).first()
        return menu.serialize()

    def list(self) -> list:
        return [
            menus.serialize() for menus in self.session.query(MenuDB).all()
        ]

    def add(self, title: str, description: str):
        menu: MenuDB = MenuDB(title=title, description=description)
        self.session.add(menu)
        self.session.commit()
        return menu

    def update(self, menu_id: str, title: str, description: str):
        check_exception(menu_id=menu_id)
        menu: MenuDB = self.session.query(MenuDB).filter_by(id=menu_id).first()
        menu.title = title
        menu.description = description
        self.session.add(menu)
        self.session.commit()
        return menu

    def delete(self, menu_id: str) -> dict:
        check_exception(menu_id=menu_id)
        menu: MenuDB = self.session.query(MenuDB).filter_by(id=menu_id).first()
        title = menu.title
        self.session.delete(menu)
        self.session.commit()
        return {'menu deleted': title}
