from telethon import events

PM = "heeeee"


@bot.on(events.NewMessage(pattern="lol (.*)"))
async def _(event):
    if event.fwd_from:
        return
    event.sender_id
    chat = await event.get_chat()
    await event.client.send_message(chat, PM)
