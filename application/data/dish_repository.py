from data.models import Dish as DishModel
from utils.additional_methods import check_exception

class DishRepository:
    def __init__(self, session):
        self.session = session

    def get(self, dish_id: str): #
        check_exception(dish_id=dish_id)
        dish = self.session.query(DishModel).filter_by(id=dish_id).first()
        return dish.dict()

    def list(self, submenu_id: str): #
        return [
            dishes.serialize() for dishes in self.session.query(DishModel).filter_by(submenu_id=submenu_id).all()
        ]

    def add(self, menu_id: str, submenu_id: str, title: str, description: str, price: str): #
        check_exception(submenu_id=submenu_id)
        dish = DishModel(menu_id = menu_id, submenu_id=submenu_id, title = title, description = description, price=price)
        self.session.add(dish)
        self.session.commit()
        return dish.dict()

    def update(self, menu_id: str, submenu_id: str, dish_id: str, title: str, description: str, price: str): #
        check_exception(dish_id=dish_id)
        dish = self.session.query(DishModel).filter_by(id=dish_id).first()
        dish.title = title
        dish.description = description
        dish.price = price
        self.session.add(dish)
        self.session.commit()
        return dish.dict()

    def delete(self, dish_id: str):
        check_exception(dish_id=dish_id)
        dish = self.session.query(DishModel).filter_by(id=dish_id).first()
        title = dish.title
        self.session.delete(dish)
        self.session.commit()
        return {"dish deleted": title}