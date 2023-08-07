from data.dish_repository import DishRepository
from data.menu_repository import MenuRepository
from data.repositories_registry import RepositoriesRegistry
from data.submenu_repository import SubmenuRepository
from server import create_server

repositories_registry = RepositoriesRegistry(
    menu_repo=MenuRepository, submenu_repo=SubmenuRepository, dish_repo=DishRepository)

server = create_server(repositories=repositories_registry)
