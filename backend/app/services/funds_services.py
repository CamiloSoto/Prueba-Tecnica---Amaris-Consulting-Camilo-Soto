import uuid
from datetime import datetime
from app.db.dynamo import fondos_table, transacciones_table, clientes_table
from app.models.schemas import SuscripcionRequest, CancelacionRequest, Transaccion
from botocore.exceptions import ClientError
import boto3
import os

sns = boto3.client(
    "sns",
    region_name="us-east-1",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

def obtener_fondos():
    response = fondos_table.scan()
    return response.get("Items", [])

def obtener_cliente(cliente_id):
    response = clientes_table.get_item(Key={"id": cliente_id})
    return response.get("Item")

def obtener_fondo(fondo_id):
    response = fondos_table.get_item(Key={"id": fondo_id})
    return response.get("Item")

def guardar_transaccion(transaccion: Transaccion):
    item = transaccion.dict()
    # 🔐 Corrige formato de fecha para DynamoDB
    if isinstance(item["fecha"], datetime):
        item["fecha"] = item["fecha"].isoformat()
    transacciones_table.put_item(Item=item)

def notificar(medio, mensaje, destino):
    if medio == "email":
        sns.publish(Message=mensaje, Subject="Notificación de Fondo", TopicArn=os.getenv("SNS_EMAIL_TOPIC_ARN"))
    elif medio == "sms":
        sns.publish(Message=mensaje, PhoneNumber=destino)

def suscribir(request: SuscripcionRequest):
    cliente = obtener_cliente(request.cliente_id)
    fondo = obtener_fondo(request.fondo_id)

    if not cliente or not fondo:
        raise ValueError("Cliente o fondo no encontrados.")

    saldo = cliente["saldo"]
    monto_minimo = fondo["monto_minimo"]

    if saldo < monto_minimo:
        raise Exception(f"No tiene saldo disponible para vincularse al fondo {fondo['nombre']}.")

    # Actualizar saldo
    nuevo_saldo = saldo - monto_minimo
    try:
        clientes_table.update_item(
            Key={"id": cliente["id"]},
            UpdateExpression="SET saldo = :nuevo",
            ExpressionAttributeValues={":nuevo": nuevo_saldo}
        )
        
    except ClientError as e:
        raise Exception(f"Error actualizando saldo del cliente: {e.response['Error']['Message']}")

    # Crear transacción

    trans = Transaccion(
        id=str(uuid.uuid4()),
        tipo="apertura",
        cliente_id=request.cliente_id,
        fondo_id=request.fondo_id,
        monto=monto_minimo,
        fecha=datetime.now().isoformat(),
        notificado_por=request.notificacion
    )
    try:
        guardar_transaccion(trans)
    except Exception as e:
        clientes_table.update_item(
            Key={"id": cliente["id"]},
            UpdateExpression="SET saldo = :original",
            ExpressionAttributeValues={":original": saldo}
        )
        raise Exception(f"Error al guardar transacción. Se revirtió el saldo. Detalles: {str(e)}")

    # Notificar
    mensaje = f"Te has suscrito al fondo {fondo['nombre']} por {monto_minimo} COP."
    print(mensaje)
    notificar(request.notificacion, mensaje, cliente.get("telefono", ""))

    return trans

def cancelar(request: CancelacionRequest):
    cliente = obtener_cliente(request.cliente_id)
    fondo = obtener_fondo(request.fondo_id)

    if not cliente or not fondo:
        raise ValueError("Cliente o fondo no encontrados.")

    monto_retorno = fondo["monto_minimo"]
    saldo_original = cliente["saldo"]
    nuevo_saldo = saldo_original + monto_retorno
    
    if not cliente or not fondo:
        raise ValueError("Cliente o fondo no encontrados.")
    
    try:

        clientes_table.update_item(
            Key={"id": cliente["id"]},
            UpdateExpression="SET saldo = :nuevo",
            ExpressionAttributeValues={":nuevo": nuevo_saldo}
        )
    except ClientError as e:
        raise Exception(f"Error actualizando saldo: {e.response['Error']['Message']}")

    trans = Transaccion(
        id=str(uuid.uuid4()),
        tipo="cancelacion",
        cliente_id=request.cliente_id,
        fondo_id=request.fondo_id,
        monto=monto_retorno,
        fecha=datetime.now().isoformat(),
        notificado_por="email"  # Cancelación por defecto se notifica por email
    )
    try:
        guardar_transaccion(trans)
    except Exception as e:
        # Revertir el saldo si la transacción falla
        clientes_table.update_item(
            Key={"id": cliente["id"]},
            UpdateExpression="SET saldo = :original",
            ExpressionAttributeValues={":original": saldo_original}
        )
        raise Exception(f"Error al guardar transacción. Se revirtió el saldo. Detalles: {str(e)}")

    mensaje = f"Te has retirado del fondo {fondo['nombre']}. Se han reintegrado {monto_retorno} COP."
    notificar("email", mensaje, cliente.get("email", ""))

    return trans

def obtener_historial(cliente_id: str):
    response = transacciones_table.query(
        IndexName="cliente_id-index",
        KeyConditionExpression="cliente_id = :id",
        ExpressionAttributeValues={":id": cliente_id}
    )
    return response.get("Items", [])
