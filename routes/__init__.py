from .auth import router as auth_router
from .views import router as views_router

__all__ = [
    "auth_router",
    "views_router"
]