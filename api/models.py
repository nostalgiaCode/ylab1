import uuid

from sqlalchemy import (Column, ForeignKey, String,
                        create_engine)
from sqlalchemy.engine import URL
from sqlalchemy.orm import relationship, sessionmaker

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="1234",
    host="localhost", ###docker->pgsql ###pc->localhost
    database="postgres",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Menu(Base):
    __tablename__ = "Menu"

    id = Column(String,  default=lambda: str(uuid.uuid4()), unique=True, primary_key = True)
    title = Column(String)
    description = Column(String)
    submenu = relationship("Submenu", backref="menu", cascade="all,delete")
    dish = relationship("Dish", backref="menu", cascade="all,delete")

class Submenu(Base):
    __tablename__ = "Submenu"

    id = Column(String,  default=lambda: str(uuid.uuid4()), unique=True, primary_key = True)
    menu_id = Column(String, ForeignKey('Menu.id'))
    title = Column(String)
    description = Column(String)
    dish = relationship("Dish", backref="submenu", cascade="all,delete")

class Dish(Base):
    __tablename__ = "Dish"

    id = Column(String,  default=lambda: str(uuid.uuid4()), unique=True, primary_key = True)
    menu_id = Column(String, ForeignKey('Menu.id'))
    submenu_id = Column(String, ForeignKey('Submenu.id'))
    title = Column(String)
    description = Column(String)
    price = Column(String)


Base.metadata.create_all(engine)