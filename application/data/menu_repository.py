from data.models import Menu as MenuModel
from utils.additional_methods import check_exception

class MenuRepository:
    def __init__(self, session):
        self.session = session

    def get(self, menu_id: str):
        check_exception(menu_id=menu_id)
        menu = self.session.query(MenuModel).filter_by(id=menu_id).first()
        return menu.dict()

    def list(self):
        return [
            menus.serialize() for menus in self.session.query(MenuModel).all()
        ]

    def add(self, title: str, description: str):
        menu = MenuModel(title = title, description = description)
        self.session.add(menu)
        self.session.commit()
        return menu.dict()

    def update(self, menu_id: str, title: str, description: str):
        check_exception(menu_id=menu_id)
        menu = self.session.query(MenuModel).filter_by(id=menu_id).first()
        menu.title = title
        menu.description = description
        self.session.add(menu)
        self.session.commit()
        return menu.dict()

    def delete(self, menu_id: str):
        check_exception(menu_id=menu_id)
        menu = self.session.query(MenuModel).filter_by(id=menu_id).first()
        title = menu.title
        self.session.delete(menu)
        self.session.commit()
        return {"menu deleted": title}


