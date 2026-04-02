#!/usr/bin/python3
import requests
import os
import json

TOKEN = os.getenv("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
res = requests.get(url, timeout=10)
resp = json.loads(res.text)
mes = resp["result"]
chat = mes[0]
chat1 = chat["message"]
chat_id = chat1["chat"]
print (chat_id["id"])