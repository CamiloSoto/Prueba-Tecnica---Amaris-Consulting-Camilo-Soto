## Configurar entorno virtual

```bash
py -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn boto3 pydantic[dotenv]
pip install pytest
```
## Despliegue aws
```
aws cloudformation deploy --template-file template.yaml --stack-name FondosStack --capabilities CAPABILITY_NAMED_IAM
```
## Cargar Data
```bash
python scripts/initial_data.py
```
