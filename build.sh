#!/usr/bin/env bash

echo "Instalando dependencias..."
pip install -r requirements.txt

# Se eliminan los comandos de makemigrations y migrate.
# Se elimina collectstatic ya que no hay archivos estáticos.