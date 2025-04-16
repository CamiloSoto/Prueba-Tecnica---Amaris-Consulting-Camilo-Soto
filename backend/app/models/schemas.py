from pydantic import BaseModel
from typing import Literal
from datetime import datetime
import uuid

class Fondo(BaseModel):
    id: int
    nombre: str
    monto_minimo: int
    categoria: str

class SuscripcionRequest(BaseModel):
    cliente_id: str
    fondo_id: int
    notificacion: Literal["email", "sms"]

class CancelacionRequest(BaseModel):
    cliente_id: str
    fondo_id: int

class Transaccion(BaseModel):
    id: str
    tipo: Literal["apertura", "cancelacion"]
    cliente_id: str
    fondo_id: int
    monto: int
    fecha: datetime
    notificado_por: Literal["email", "sms"]
