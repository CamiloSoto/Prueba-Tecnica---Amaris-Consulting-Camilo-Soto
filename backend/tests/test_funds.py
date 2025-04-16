import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import uuid
from datetime import datetime
from app.models.schemas import Transaccion

def test_transaccion_model_fields():
    trans_id = str(uuid.uuid4())
    now = datetime.now()
    
    trans = Transaccion(
        id=trans_id,
        tipo="apertura",
        cliente_id="123",
        fondo_id=1,
        monto=75000,
        fecha=now,
        notificado_por="email"
    )

    # Verificar tipos
    assert isinstance(trans.id, str)
    assert isinstance(uuid.UUID(trans.id), uuid.UUID)  # Verifica que sea UUID válido
    assert isinstance(trans.tipo, str)
    assert isinstance(trans.cliente_id, str)
    assert isinstance(trans.fondo_id, int)
    assert isinstance(trans.monto, (int, float))
    assert isinstance(trans.fecha, datetime)
    assert isinstance(trans.notificado_por, str)

    # Verificar valores
    assert trans.tipo == "apertura"
    assert trans.fondo_id == 1
    assert trans.notificado_por == "email"
    assert trans.monto == 75000
    assert trans.fecha == now
