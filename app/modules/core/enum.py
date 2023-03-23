from enum import IntEnum

class EstadoPedido(IntEnum):
    RECEIVED = 1
    CONFIRMED = 2
    DISPATCHED = 3
    DELIVERED = 4
    CANCELED = 5