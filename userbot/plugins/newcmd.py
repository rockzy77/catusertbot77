import asyncio

from telethon import events, functions

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql

from . import ALIVE_NAME, PM_START, PMMESSAGE_CACHE, set_key

PM = "heeeee"


@bot.on(events.NewMessage(pattern="lol (.*)"))
async def _(event):
    if event.fwd_from:
        return
    chat_id = event.sender_id
    chat = await event.get_chat()    
    test1 = await event.client.send_message(chat, PM)    