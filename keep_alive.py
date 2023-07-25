# This is only to keep the bot 'alive'.
# Flask will keep sending a message every 5m to poke the bot to stay awake

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "I YET LIVE"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()