from fastapi import FastAPI
from loguru import logger
from tortoise import Tortoise
from tortoise.contrib.starlette import register_tortoise

from .settings import get_settings

settings = get_settings()

""" This config is for generate migrations.bkp by aerich """
TORTOISE_ORM = {
    "connections": {"default": settings.DB_URL},
    "apps": {
        "models": {
            "models": settings.MODELS,
            "default_connection": "default",
        },
    },
}


async def init_db(app: FastAPI):
    """This function is to configuration database credentials"""
    register_tortoise(
        app=app,
        db_url=settings.DB_URL if not settings.TESTING else settings.DB_TEST_URL,
        generate_schemas=settings.GENERATE_SCHEMAS,
        modules={"models": settings.MODELS},
    )


async def connect_to_database() -> None:
    logger.info("Initialize Tortoise...")
    await Tortoise.init(
        db_url=settings.DB_URL if not settings.TESTING else settings.DB_TEST_URL,
        modules={"models": settings.MODELS},
    )


async def close_connection_database() -> None:
    logger.info("Closing Tortoise...")
    await Tortoise.close_connections()
