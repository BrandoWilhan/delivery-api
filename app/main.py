from app.config.router import init_routers
from app.config.db import *
from fastapi import FastAPI



app = FastAPI()

@app.on_event("startup")
async def startup_routers():
    await init_routers(app)

@app.on_event("startup")
async def startup_routers():
    await connect_to_database()
