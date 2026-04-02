#!/bin/bash

# 1. Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "Error: Docker no está instalado o no está en el PATH."
    echo "Puedes instalarlo usando el gestor de paquetes de tu sistema (ej. sudo pacman -S docker o sudo apt install docker.io)."
    exit 1
fi

echo "Docker detectado. Iniciando LibreTranslate..."

# 2. Ejecutar el contenedor
docker run -d --name libretranslate -p 5000:5000 -e LT_LOAD_ONLY=en,es libretranslate/libretranslate

# 3. Confirmación
if [ $? -eq 0 ]; then
    echo "¡Contenedor 'libretranslate' ejecutándose correctamente en el puerto 5000!"
else
    echo "Hubo un problema al intentar iniciar el contenedor (¿tal vez ya existe uno con ese nombre?)."
fi