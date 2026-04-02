#!/usr/bin/python3
import requests
import os
import json

TOKEN = os.getenv("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
try:
    peticion = requests.get(url, timeout=10)
    respuesta = json.loads(peticion.text)
    if respuesta.get("ok") and respuesta.get("result"):
        chat_id = respuesta["result"][0]["message"]["chat"]["id"]
        print (chat_id)
    else:
        print ("El historial está vacío. Envíale un mensaje a tu bot en Telegram y vuelve a intentar.")

except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")
except KeyError as e:
    print(f"Error procesando el JSON. Falta la clave: {e}")
