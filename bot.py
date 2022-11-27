import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5811115081:AAE8snl_kvuiRi5uBWNNfNcKSpTZqWs9RsE")

API_ID = int(os.environ.get("API_ID", "1445748"))

API_HASH = os.environ.get("API_HASH", "b40c645a5a39a93c269c4f3ab8e4b02e")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
