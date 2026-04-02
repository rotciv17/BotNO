#!/usr/bin/python3
import asyncio
import json
import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    filters,
    MessageHandler,
)

# Configuración (usa variables de entorno para seguridad)
TOKEN = os.getenv("TELEGRAM_TOKEN")          # Tu token del bot
ALLOWED_CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID"))  # Tu chat_id (solo tú puedes usarlo)

URL_API = "https://naas.isalman.dev/no"
TIMEOUT = 3

# Configura logging básico
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def traducir_libre(texto, idioma_origen="en", idioma_destino="es"):
    url = "http://localhost:5000/translate"
    
    payload = {
        "q": texto,
        "source": idioma_origen,
        "target": idioma_destino,
        "format": "text"
    }
    
    try:
        respuesta = requests.post(url, json=payload, timeout=3)
        respuesta.raise_for_status()  # Lanza error si no es 200
        return respuesta.json()["translatedText"]
    except Exception as e:
        return f"Error: {str(e)}"

async def check_no(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /no o /check: consulta la API y responde"""
    chat_id = update.effective_chat.id
    
    # Seguridad: solo permite a tu chat_id
    if chat_id != ALLOWED_CHAT_ID:
        await update.message.reply_text("No tienes permiso para usar este bot.")
        return
    
    await update.message.reply_text("Consultando... ⏳")
    
    try:
        respuesta = await asyncio.to_thread(
            lambda: requests.get(URL_API, timeout=TIMEOUT)
        )
        # Nota: usamos asyncio.to_thread porque requests es sincrono
        
        status = respuesta.status_code
        
        try:
            datos = respuesta.json()
            texto = json.dumps(datos, indent=2, ensure_ascii=False)
        except:
            texto = respuesta.text[:2000]
        
        emoji = "🟢" if status == 200 else "🔴" if status >= 400 else "🟡"
        tra = traducir_libre(datos['reason'])
        mensaje = (f"English: {datos['reason']} \nSpanish: {tra}")
        
        await update.message.reply_text(mensaje, parse_mode="Markdown")
        logger.info(f"Consulta exitosa desde chat {chat_id}")
        
    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        await update.message.reply_text(error_msg)
        logger.error(error_msg)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /start"""
    await update.message.reply_text(
        "¡Hola! Usa /no o /check para saber como decir no"
    )

def main():
    if not TOKEN or not ALLOWED_CHAT_ID:
        print("Error: Configura TELEGRAM_TOKEN y TELEGRAM_CHAT_ID en variables de entorno.")
        return

    # Construye la aplicación
    application = ApplicationBuilder().token(TOKEN).build()

    # Handlers de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("no", check_no))
    application.add_handler(CommandHandler("check", check_no))

    # Opcional: maneja cualquier texto (por si quieres extenderlo)
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot iniciado. Escuchando comandos...")
    # Inicia long polling (bloqueante, ideal para correr en background)
    application.run_polling(
        poll_interval=0.5,          # cada 0.5s chequea updates
        timeout=10,                 # espera hasta 10s por update
        drop_pending_updates=True   # ignora mensajes viejos al iniciar
    )

if __name__ == "__main__":
    import requests  # lo importamos aquí para que no falle si no está
    main()
