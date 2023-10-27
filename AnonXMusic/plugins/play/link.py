import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app

@app.on_message(filters.command(["الرابط","/link"],""))
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("قم برفعي مسؤول في المجموعة أولا ؟")
    await message.reply_text(f"تم إنشاء رابط الدعوة بنجاح :\n {invitelink}")
    
