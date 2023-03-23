from .model import Pedido

class PedidoRepository():
    def __init__(self):  
        self.entity = Pedido()

    async def insert(self, payload: dict):
        return await self.entity.create(**payload)

    async def update(self, payload: dict, id: int):
        await self.entity.filter(id=id).update(**payload)
        return await self.entity.get_or_none(id=id)

    async def get_all(self):
        return await self.entity.all()

    async def get_by_id(self, id: int):
        return await self.entity.get_or_none(id=id)

    async def delete(self, id: int):
        pedido = await self.entity.get_or_none(id=id)
        await pedido.delete()
        return await self.entity.get_or_none(id=id)