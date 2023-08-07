from data.models import Submenu as SubmenuDB
from utils.additional_methods import check_exception


class SubmenuRepository:
    def __init__(self, session):
        self.session = session

    def get(self, submenu_id: str) -> dict:
        check_exception(submenu_id=submenu_id)
        submenu = self.session.query(SubmenuDB).filter_by(id=submenu_id).first()
        return submenu.serialize()

    def list(self, menu_id: str) -> list:
        return [
            submenus.serialize() for submenus in self.session.query(SubmenuDB).filter_by(menu_id=menu_id).all()
        ]

    def add(self, menu_id: str, title: str, description: str):
        check_exception(menu_id=menu_id)
        submenu = SubmenuDB(menu_id=menu_id, title=title, description=description)
        self.session.add(submenu)
        self.session.commit()
        return submenu

    def update(self, submenu_id: str, menu_id: str, title: str, description: str):
        check_exception(submenu_id=submenu_id)
        submenu = self.session.query(SubmenuDB).filter_by(id=submenu_id).first()
        submenu.title = title
        submenu.description = description
        self.session.add(submenu)
        self.session.commit()
        return submenu

    def delete(self, submenu_id: str) -> dict:
        check_exception(submenu_id=submenu_id)
        submenu = self.session.query(SubmenuDB).filter_by(id=submenu_id).first()
        title = submenu.title
        self.session.delete(submenu)
        self.session.commit()
        return {'submenu deleted': title}
