import asyncio

from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)

from AnonXMusic import app
from config import BANNED_USERS


@app.on_message(
  filters.command(
      [
         "انمي", 
         "انميات",    
       ],""
  )
    & filters.group
    & ~BANNED_USERS
)
async def aflamAR(client: Client, message: Message):
    await message.reply_text(f"""✧<b> اهلين فيك في قسم أنـــمي  دينا</b>\n\n ✧ <a href=https://t.me/Mlze1bot> 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂 </a>   لتصفح الانميات اضغط على زر انميات  """,
        reply_markup=InlineKeyboardMarkup(
              [

        [InlineKeyboardButton("أنـــميــات", callback_data="anmie2 " + str(message.from_user.id))],
        
        [InlineKeyboardButton("✧ [𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂] ", url=f"https://t.me/Mlze1bot")],

       ]
    ), 
     disable_web_page_preview=True
) 


@app.on_message(filters.command(["أغاني", "اغنيه ", "اغاني","غنيلي"],""))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/MusicIsaac/{rl}"
    await client.send_voice(message.chat.id,url,caption="✧ <a href=https://t.me/Mlze1bot> 𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂 </a> ",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆 𝒅𝒊𝒏𝒂", url=f"t.me/Mlze1bot")
                ],
            ]
        )
    )
