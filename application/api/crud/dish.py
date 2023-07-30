from api.models import Dish, session
from api.schemas import DishBase
from api.utils import check_exception

def get_all(target_submenu_id: str):
    all_dishes=session.query(Dish).filter_by(submenu_id=target_submenu_id).all()
    return [get(all_dishes[index].id) for index in range(len(all_dishes))]

def get(target_dish_id: str):
    check_exception(target_dish_id=target_dish_id)
    dish = session.query(Dish).filter_by(id=target_dish_id).first()
    # return DishSchema(id = dish.id, price = str(dish.price), title = dish.title, description = dish.description)
    return dish.make_response()

def post(target_menu_id: str, target_submenu_id: str, input:DishBase):
    check_exception(target_submenu_id=target_submenu_id)
    dish = Dish(**input.dict(), menu_id = target_menu_id, submenu_id = target_submenu_id)
    session.add(dish)
    session.commit()
    # return DishSchema(id = dish.id, price = str(dish.price), title = dish.title, description = dish.description)
    return dish.make_response()

def patch(target_dish_id: str, input:DishBase):
    check_exception(target_dish_id=target_dish_id)
    dish = session.query(Dish).filter_by(id=target_dish_id).first()
    dish.title = input.title
    dish.description = input.description
    dish.price = input.price
    session.add(dish)
    session.commit()
    # return DishSchema(id = dish.id, price = str(dish.price), title = dish.title, description = dish.description)
    return dish.make_response()

def delete(target_dish_id):
    check_exception(target_dish_id=target_dish_id)
    dish = session.query(Dish).filter_by(id=target_dish_id).first()
    title = dish.title
    session.delete(dish)
    session.commit()
    return {"dish deleted": title}