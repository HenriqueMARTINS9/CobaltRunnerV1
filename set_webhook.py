import requests
import os

TOKEN = "7148335420:AAFd00HaGsoVlNijc6Tsd847PG4W6dzzExg"
WEBHOOK_URL = 'https://cobalt-runner-v1.vercel.app/hook'  # Remplacez par l'URL de votre application Vercel

response = requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}')
print(response.json())
