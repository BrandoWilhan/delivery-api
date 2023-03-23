import logging
from functools import lru_cache
from typing import List

from decouple import config
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Setting(BaseSettings):
    TESTING: bool = config("TESTING", default=False, cast=bool)
    DB_URL = config("DB_URL")
    GENERATE_SCHEMAS = config("GENERATE_SCHEMAS", default=False)

    ALLOW_HEADERS: List = ["*"]
    ALLOW_METHODS: List = ["*"]
    ORIGINS: List = [
        "*",
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:3000",
    ]
    MODELS: List = [
        "aerich.models",
        "app.modules.pedido.model"
    ]



@lru_cache()
def get_settings():
    log.info("Loading Config Application.")
    return Setting()
