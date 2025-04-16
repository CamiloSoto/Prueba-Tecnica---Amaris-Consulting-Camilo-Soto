from fastapi import FastAPI

app = FastAPI(title="Gestión de Fondos")

@app.get("/")
def root():
    return {"message": "API de Fondos operativa"}
