#!/usr/bin/python3
import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
res = requests.get(url, timeout=10)
print(res.text)
