from pydantic import BaseModel
from typing import Union

###

class MenuBase(BaseModel):
    title: str
    description: Union[str, None] = None

class MenuData(MenuBase):
    id: str

class MenuSchema(MenuData):
    submenus_count: int
    dishes_count: int

###

class SubmenuBase(BaseModel):
    title: str
    description: Union[str, None] = None

class SubmenuData(SubmenuBase):
    id: str

class SubmenuSchema(SubmenuData):
    dishes_count: int

# class MenuSchema(BaseModel):
#     title: str
#     description: Union[str, None] = None

#class MenuFull(MenuBase):


class DishBase(BaseModel):
    title: str
    description: Union[str, None] = None
    price: str