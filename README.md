# 💼 Prueba Tecnica Camilo Alejandro Soto Vega

Aplicación web para suscripción, cancelación y consulta de transacciones en fondos de inversión. Desarrollada con **FastAPI**, **React**, **DynamoDB** y desplegable con **CloudFormation**.

---

## 📌 Respuestas Parte 1 – Análisis técnico

### a. Tecnologías utilizadas y justificación

- **FastAPI (Python)**: framework ágil, rápido y con documentación automática, ideal para APIs REST.
- **DynamoDB (AWS NoSQL)**: servicio serverless, escalable y sin administración de infraestructura, ideal para la estructura de fondos y transacciones.
- **React + TailwindCSS**: permite un frontend interactivo, moderno y rápido de desarrollar.
- **Amazon SNS**: facilita el envío de notificaciones por email o SMS con mínima configuración.
- **CloudFormation**: permite despliegue reproducible y versionado de la infraestructura.
- **GitHub + Pytest**: para control de versiones y aseguramiento de calidad.

### b. Modelo de datos NoSQL

#### `Clientes`

```json
{
  "id": "uuid",
  "nombre": "string",
  "email": "string",
  "telefono": "string",
  "saldo": 500000
}
```

#### `Fondos`

```json
{
  "id": "number",
  "nombre": "string",
  "monto_minimo": "number",
  "categoria": "string"
}
```

#### `Transacciones`

```json
{
  "id": "uuid",
  "tipo": "apertura | cancelacion",
  "cliente_id": "uuid",
  "fondo_id": "number",
  "monto": "number",
  "fecha": "timestamp",
  "notificado_por": "sms | email"
}
```
### c. Aplicación Web
La solución completa se encuentra implementada en este repositorio.

El backend está desarrollado en FastAPI con lógica de negocio detallada y el frontend React permite listar fondos, suscribirse y ver historial.

El despliegue se realiza vía AWS CloudFormation y S3.

## 📌 Parte 2 - Consulta SQL
```sql
SELECT DISTINCT c.nombre
FROM Cliente c
JOIN Inscripción i ON c.id = i.idCliente
JOIN Disponibilidad d ON i.idProducto = d.idProducto
JOIN Visitan v ON c.id = v.idCliente AND d.idSucursal = v.idSucursal;

```
---

## 🚀 Tecnologías utilizadas

- **Backend**: FastAPI + DynamoDB + Boto3
- **Frontend**: React + TailwindCSS + Axios
- **Infraestructura**: AWS CloudFormation
- **Notificaciones**: Amazon SNS (email / SMS)
- **Pruebas**: pytest

---

## 🧱 Estructura del proyecto

```text
backend/
├── app/
│ ├── main.py
│ ├── models/
│ ├── services/
│ ├── routes/
│ └── db/
├── scripts/
│ └── cargar_datos_iniciales.py
├── tests/
├── requirements.txt
├── template.yaml
└── README.md

frontend/
├── src/
│ ├── pages/
│ ├── config/
│ └── App.jsx
```

## ⚙️ Backend - FastAPI

### 🔧 Instalación

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ▶️ Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:
http://localhost:8000/docs

### 🧪 Pruebas

```bash
pytest tests/
```

### 💾 Cargar datos iniciales

```bash
python scripts/initial_data.py
```

Esto cargará:

- 5 fondos predefinidos.
- 1 cliente con saldo COP $500,000.
- Mostrará el ID del cliente.

### ☁️ Despliegue con CloudFormation

```bash
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name FondosStack \
  --capabilities CAPABILITY_NAMED_IAM
```

Incluye:

- 3 tablas DynamoDB
- SNS para notificaciones

## 💻 Frontend - React

### ⚙️ Configuración

```bash
cd frontend
npm install
```

### ▶️ Ejecutar

```
npm run dev
```

Accede a:
http://localhost:4200

---

### 📚 Funcionalidades

- 🔍 Listado de fondos.
- 📨 Suscripción con selección de notificación (email / SMS).
- 📜 Historial de transacciones del cliente.

### 📌 Recomendaciones

- Usar el ID generado en cargar_datos_iniciales.py como cliente de prueba.
- Para notificaciones SMS, debe estar habilitado el número en el sandbox de SNS.
