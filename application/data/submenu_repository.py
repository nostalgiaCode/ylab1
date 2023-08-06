from data.models import Submenu as SubmenuModel
from utils.additional_methods import check_exception

class SubmenuRepository:
    def __init__(self, session):
        self.session = session

    def get(self, submenu_id: str):
        check_exception(submenu_id=submenu_id)
        submenu = self.session.query(SubmenuModel).filter_by(id=submenu_id).first()
        return submenu.dict()

    def list(self, menu_id: str):
        return [
            submenus.serialize() for submenus in self.session.query(SubmenuModel).filter_by(menu_id=menu_id).all()
        ]

    def add(self, menu_id: str, title: str, description: str):
        check_exception(menu_id=menu_id)
        submenu = SubmenuModel(menu_id = menu_id, title = title, description = description)
        self.session.add(submenu)
        self.session.commit()
        return submenu.dict()

    def update(self, submenu_id: str, menu_id: str, title: str, description: str):
        check_exception(submenu_id=submenu_id)
        submenu = self.session.query(SubmenuModel).filter_by(id=submenu_id).first()
        submenu.title = title
        submenu.description = description
        self.session.add(submenu)
        self.session.commit()
        return submenu.dict()

    def delete(self, submenu_id: str):
        check_exception(submenu_id=submenu_id)
        submenu = self.session.query(SubmenuModel).filter_by(id=submenu_id).first()
        title = submenu.title
        self.session.delete(submenu)
        self.session.commit()
        return {"submenu deleted": title}


