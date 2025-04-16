from fastapi import APIRouter, HTTPException
from app.models.schemas import SuscripcionRequest, CancelacionRequest, Transaccion
from app.services import funds_services

router = APIRouter()

@router.get("/")
def listar_fondos():
    return funds_services.obtener_fondos()

@router.post("/suscribir", response_model=Transaccion)
def suscribir_fondo(request: SuscripcionRequest):
    try:
        return funds_services.suscribir(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/cancelar", response_model=Transaccion)
def cancelar_fondo(request: CancelacionRequest):
    try:
        return funds_services.cancelar(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/historial/{cliente_id}")
def historial(cliente_id: str):
    try:
        return funds_services.obtener_historial(cliente_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
