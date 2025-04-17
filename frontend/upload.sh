#!/bin/bash

BUCKET_NAME="fondos-frontend-demo-camilo-20250416-1126pm"

# Directorio del build
BUILD_DIR="./dist"

# Verificar que el directorio build existe
if [ ! -d "$BUILD_DIR" ]; then
  echo "❌ El directorio $BUILD_DIR no existe. Asegúrate de ejecutar 'npm run build' antes."
  exit 1
fi

echo "🚀 Subiendo archivos desde $BUILD_DIR a S3 bucket: $BUCKET_NAME..."

# Subir el contenido con tipo de contenido detectado automáticamente
aws s3 sync $BUILD_DIR s3://$BUCKET_NAME/ --delete --acl bucket-owner-full-control

# Opcional: Forzar que todos los archivos .html tengan el content-type correcto
aws s3 cp s3://$BUCKET_NAME/index.html s3://$BUCKET_NAME/index.html --content-type "text/html" --metadata-directive REPLACE

echo "✅ Subida completada. Revisa la URL del sitio:"
echo "🌐 http://$BUCKET_NAME.s3-website-$(aws configure get region).amazonaws.com"
