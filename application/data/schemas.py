from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: str | None = None


class MenuData(MenuBase):
    id: str


class MenuSchema(MenuData):
    submenus_count: int
    dishes_count: int


class SubmenuBase(BaseModel):
    title: str
    description: str | None = None


class SubmenuData(SubmenuBase):
    id: str


class SubmenuSchema(SubmenuData):
    dishes_count: int


class DishBase(BaseModel):
    title: str
    description: str | None = None
    price: str


class DishSchema(DishBase):
    id: str
