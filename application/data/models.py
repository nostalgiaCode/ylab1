import uuid

from data.schemas import DishSchema, MenuSchema, SubmenuSchema
from settings import *
from sqlalchemy import Column, ForeignKey, Numeric, String, create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

url = URL.create(
    drivername='postgresql',
    username=POSTGRESUSERNAME,
    password=POSTGRESPASSWORD,
    host=POSTGRESHOST,  # docker->pgsql ###pc->localhost
    database=POSTGRESDB,
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class Menu(Base):
    __tablename__ = 'Menu'

    id = Column(String, default=lambda: str(uuid.uuid4()), unique=True, primary_key=True)
    title = Column(String)
    description = Column(String)
    submenu = relationship('Submenu', backref='menu', cascade='all,delete')

    def dict(self):
        return MenuSchema(id=self.id, title=self.title, description=self.description,
                          submenus_count=session.query(Submenu).filter(Menu.id == self.id).join(Menu.submenu).count(),
                          dishes_count=session.query(Dish).filter(Menu.id == self.id).join(Menu.submenu).join(Submenu.dish).count())

    def serialize(self):
        return {
            "id" : self.id,
            "title": self.title,
            "description": self.description,
            "submenus_count": session.query(Submenu).filter(Menu.id == self.id).join(Menu.submenu).count(),
            "dishes_count": session.query(Dish).filter(Menu.id == self.id).join(Menu.submenu).join(Submenu.dish).count()
        }

class Submenu(Base):
    __tablename__ = 'Submenu'

    id = Column(String, default=lambda: str(uuid.uuid4()), unique=True, primary_key=True)
    menu_id = Column(String, ForeignKey('Menu.id'))
    title = Column(String)
    description = Column(String)
    dish = relationship('Dish', backref='submenu', cascade='all,delete')

    def dict(self):
        return SubmenuSchema(id=self.id, title=self.title, description=self.description,
                             dishes_count=session.query(Dish).filter(Submenu.id == self.id).join(Submenu.dish).count())

    def serialize(self):
        return {
            "id" : self.id,
            "menu_id": self.menu_id,
            "title": self.title,
            "description": self.description,
            "dishes_count": session.query(Dish).filter(Submenu.id == self.id).join(Submenu.dish).join(Submenu.dish).count()
        }

class Dish(Base):
    __tablename__ = 'Dish'

    id = Column(String, default=lambda: str(uuid.uuid4()), unique=True, primary_key=True)
    menu_id = Column(String, ForeignKey('Menu.id'))
    submenu_id = Column(String, ForeignKey('Submenu.id'))
    title = Column(String)
    description = Column(String)
    price = Column(Numeric(precision=10, scale=2))

    def dict(self):
        return DishSchema(id=self.id, price=str(self.price), title=self.title, description=self.description)

    def serialize(self):
        return {
            "id" : self.id,
            "menu_id": self.menu_id,
            "submenu_id": self.submenu_id,
            "title": self.title,
            "description": self.description,
            "price": str(self.price)
        }
    

Base.metadata.create_all(engine)
