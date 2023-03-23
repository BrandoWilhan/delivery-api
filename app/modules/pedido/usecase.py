from .repository import PedidoRepository
from .schema import CreatePedidoSchema, GetPedidoSchema
from app.modules.core.utils import JsonIO

class GetOnePedidoUseCase():
    def __init__(self, id: int):
        self.__repository = PedidoRepository()
        self.__id = id

    async def __validate(self):
        pedido = await self.__repository.get_by_id(id=self.__id)
        #todo
        #if not pedido:
        #    raise InvalidData(detail="Pedido não encontrado.", status_code=404)
        return pedido

    def execute(self):
        pedido_dict = self.__validate()
        return pedido_dict


class GetAllPedidosUseCase():
    def __init__(self):
        self.__repository = PedidoRepository()

    async def execute(self):
        pedidos = await self.__repository.get_all()
        list_pedidos = [pedido.to_dict() for pedido in pedidos]
        return list_pedidos

class RegisterPedidoUseCase():
    def __init__(self, payload: CreatePedidoSchema):
        self.__payload = payload
        self.__repository = PedidoRepository()

    #todo
    #def __verify_payload(self):

    #todo
    #def __verify_pedido_exists(self, user_schema: dict):

    #todo
    #def __validate(self):

    async def __register_pedido(self, pedido_schema: dict):
        pedido = await self.__repository.insert(pedido_schema)
        return pedido

    async def execute(self):
        pedido = await self.__register_pedido(pedido_schema=self.__payload.dict())
        return GetPedidoSchema.from_orm(pedido)

class DelOnePedidoUseCase():
    def __init__(self, id: int):
        self.__repository = PedidoRepository()
        self.__id = id

    async def __validate(self):
        pedido = await self.__repository.get_by_id(id=self.__id)
        #todo
        #if not pedido:
        #    raise InvalidData(detail="Pedido não encontrado.", status_code=404)
        #else:
        if pedido:
            await self.__repository.delete(id=self.__id)
        else:
            return "falhou"
        return pedido

    async def execute(self):
        pedido_dict = await self.__validate()

        return pedido_dict


class UpdateStatePedidoUseCase():
    def __init__(self, payload: CreatePedidoSchema, id: int):
        self.__payload = payload
        self.__repository = PedidoRepository()
        self.__id = id

    async def __validate(self):
        pedido = await self.__repository.get_by_id(id=self.__id)
        #todo
        #if not pedido:
        #    raise InvalidData(detail="Pedido não encontrado.", status_code=404)
        #else:
        if pedido:
            await self.__repository.update(payload=self.__payload.dict(), id=self.__id)
        else:
            return "falhou"
        return pedido

    async def execute(self):
        pedido_dict = await self.__validate()

        return pedido_dict