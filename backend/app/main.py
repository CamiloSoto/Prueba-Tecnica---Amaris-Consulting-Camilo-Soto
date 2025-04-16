from fastapi import FastAPI
from app.routes.funds_routes import router as funds_routes

app = FastAPI(title="Gestión de Fondos")

app.include_router(funds_routes, prefix="/fondos", tags=["Fondos"])

@app.get("/")
def root():
    return {"message": "API de Fondos operativa"}
