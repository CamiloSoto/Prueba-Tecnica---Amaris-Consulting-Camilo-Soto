# Prueba Tecnica Camilo Soto

# 💼 Plataforma de Gestión de Fondos

Aplicación web para suscripción, cancelación y consulta de transacciones en fondos de inversión. Desarrollada con **FastAPI**, **React**, **DynamoDB** y desplegable con **CloudFormation**.

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
