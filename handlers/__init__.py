from aiogram import Router

from .user_handlers import router as user_router

router = Router(name=__name__)

router.include_routers(user_router)

__all__ = ["router"]
