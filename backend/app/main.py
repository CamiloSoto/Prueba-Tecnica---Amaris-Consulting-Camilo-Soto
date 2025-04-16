from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.funds_routes import router as funds_routes

app = FastAPI(title="Gestión de Fondos")

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(funds_routes, prefix="/funds", tags=["Funds"])

@app.get("/")
def root():
    return {"message": "API de Fondos operativa"}
