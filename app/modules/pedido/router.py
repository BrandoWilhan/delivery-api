from fastapi import APIRouter, status
from .schema import CreatePedidoSchema, GetPedidoSchema
from .usecase import GetAllPedidosUseCase, GetOnePedidoUseCase, RegisterPedidoUseCase, DelOnePedidoUseCase, UpdateStatePedidoUseCase

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=GetPedidoSchema)
async def read_pedidos():
    return await GetAllPedidosUseCase().execute()

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=GetPedidoSchema)
async def read_id(id: int):
    return await GetOnePedidoUseCase(id).execute()

@router.post("/insert", status_code=status.HTTP_201_CREATED, response_model=GetPedidoSchema)
async def insert_pedido(payload: CreatePedidoSchema):
    return await RegisterPedidoUseCase(payload).execute()

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=GetPedidoSchema)
async def delete_pedido(id: int):
    return await DelOnePedidoUseCase(id).execute()

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=GetPedidoSchema)
async def update(payload: CreatePedidoSchema, id: int):
    return await UpdateStatePedidoUseCase(payload, id).execute()