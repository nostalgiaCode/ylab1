from fastapi import FastAPI

from menus_endpoints import router as menurouter
from submenus_endpoints import router as submenurouter
from dish_endpoints import router as dishrouter


def create_server(repositories=None):
    server = FastAPI(debug=True)
    server.include_router(menurouter)
    server.include_router(submenurouter)
    server.include_router(dishrouter)
    server.repositories = repositories
    return server