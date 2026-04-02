#!/usr/bin/python3
import requests

TOKEN = "8542117358:AAHAa-EYaPM5IiGVPInJ4zV6zEELVEECrIE"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
res = requests.get(url, timeout=10)
print(res.text)
