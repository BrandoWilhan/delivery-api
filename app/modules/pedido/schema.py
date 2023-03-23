from fastapi_camelcase import CamelModel
from typing import Optional
from app.modules.core.enum import EstadoPedido
from datetime import datetime as DateTime


class CreatePedidoSchema(CamelModel):
    cliente: Optional[str] = "Exemplo"
    produto: Optional[str]
    valor: Optional[float]
    entregue: Optional[bool]
    estado: Optional[EstadoPedido]
    timestamp: Optional[DateTime]

class GetPedidoSchema(CamelModel):
    id: int
    cliente: Optional[str]
    produto: Optional[str]
    valor: Optional[float]
    entregue: Optional[bool]
    estado: Optional[EstadoPedido]
    timestamp: Optional[DateTime]

    class Config:
        orm_mode = True