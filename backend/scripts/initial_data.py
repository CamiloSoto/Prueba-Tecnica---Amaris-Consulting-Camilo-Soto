import boto3
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

fondos_table = dynamodb.Table("Fondos")
clientes_table = dynamodb.Table("Clientes")

fondos = [
    {"id": 1, "nombre": "FPV_EL CLIENTE_RECAUDADORA", "monto_minimo": 75000, "categoria": "FPV"},
    {"id": 2, "nombre": "FPV_EL CLIENTE_ECOPETROL", "monto_minimo": 125000, "categoria": "FPV"},
    {"id": 3, "nombre": "DEUDAPRIVADA", "monto_minimo": 50000, "categoria": "FIC"},
    {"id": 4, "nombre": "FDO-ACCIONES", "monto_minimo": 250000, "categoria": "FIC"},
    {"id": 5, "nombre": "FPV_EL CLIENTE_DINAMICA", "monto_minimo": 100000, "categoria": "FPV"},
]

cliente = {
    "id": str(uuid.uuid4()),
    "nombre": "Juan Pérez",
    "email": "juan.perez@cliente.com",
    "telefono": "+573001234567",
    "saldo": 500000
}

# Insertar fondos
for fondo in fondos:
    fondos_table.put_item(Item=fondo)

# Insertar cliente
clientes_table.put_item(Item=cliente)

print("✅ Fondos y cliente cargados exitosamente.")
print(f"🆔 Cliente creado con ID: {cliente['id']}")
