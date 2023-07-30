import uuid

from sqlalchemy import (Column, ForeignKey, String,
                        create_engine, Numeric)
from sqlalchemy.engine import URL
from sqlalchemy.orm import relationship, sessionmaker

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="1234",
    host="pgsql", ###docker->pgsql ###pc->localhost
    database="postgres",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from api.schemas import MenuSchema, SubmenuSchema, DishSchema

class Menu(Base):
    __tablename__ = "Menu"

    id = Column(String,  default=lambda: str(uuid.uuid4()), unique=True, primary_key = True)
    title = Column(String)
    description = Column(String)
    submenu = relationship("Submenu", backref="menu", cascade="all,delete")

    def make_response(self):
        return MenuSchema(id = self.id, title = self.title, description = self.description, 
                      submenus_count = session.query(Submenu).filter(Menu.id==self.id).join(Menu.submenu).count(), 
                      dishes_count = session.query(Dish).filter(Menu.id==self.id).join(Menu.submenu).join(Submenu.dish).count())

class Submenu(Base):
    __tablename__ = "Submenu"

    id = Column(String,  default=lambda: str(uuid.uuid4()), unique=True, primary_key = True)
    menu_id = Column(String, ForeignKey('Menu.id'))
    title = Column(String)
    description = Column(String)
    dish = relationship("Dish", backref="submenu", cascade="all,delete")

    def make_response(self):
        return SubmenuSchema(id = self.id, title = self.title, description = self.description, 
                      dishes_count = session.query(Dish).filter(Submenu.id==self.id).join(Submenu.dish).count())

class Dish(Base):
    __tablename__ = "Dish"

    id = Column(String,  default=lambda: str(uuid.uuid4()), unique=True, primary_key = True)
    menu_id = Column(String, ForeignKey('Menu.id'))
    submenu_id = Column(String, ForeignKey('Submenu.id'))
    title = Column(String)
    description = Column(String)
    price = Column(Numeric(precision=10, scale=2))

    def make_response(self):
        return DishSchema(id = self.id, price = str(self.price), title = self.title, description = self.description)

Base.metadata.create_all(engine)