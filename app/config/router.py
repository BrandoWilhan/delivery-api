import fastapi

async def init_routers(app: fastapi.FastAPI):
    """
    this function is to initiate all routers in the app
    """
    from app.modules.pedido.router import router as pedido_router
    app.include_router(pedido_router, prefix="/pedidos", tags=["pedidos"])
    