from tortoise import fields
from tortoise.models import Model
from app.modules.core.enum import EstadoPedido

class Pedido(Model):
    """
    isso referencia um pedido
    """
    id = fields.IntField(pk=True)
    cliente = fields.CharField(max_length=50)
    produto = fields.CharField(max_length=50)
    valor = fields.FloatField()
    entregue = fields.BooleanField()
    estado = fields.IntEnumField(EstadoPedido)
    #:o pedido foi criado as
    timestamp = fields.DatetimeField(auto_now_add=True)
