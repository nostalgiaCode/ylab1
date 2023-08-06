from data.menu_repository import MenuRepository
from data.submenu_repository import SubmenuRepository
from data.dish_repository import DishRepository
from data.repositories_registry import RepositoriesRegistry
from server import create_server

repositories_registry = RepositoriesRegistry(menu_repo=MenuRepository, submenu_repo=SubmenuRepository, dish_repo=DishRepository)

server = create_server(repositories=repositories_registry)