from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app as Client
from AnonXMusic import app


@Client.on_callback_query(filters.regex("arbic"))
async def arbic(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""<b>- مرحبا عـزيـزي  </b> [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) ! \n
<b>- في قسم تشغيل الأغاني والفيديو في المكالمات</b>\n
<b>- استخدم الازرار لـ تصفـح اوامـر الميـوزك</b> """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضف البوت لـ مجموعتك ",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [                   InlineKeyboardButton("طريقة التشغيل", callback_data="bcmds"),
                    InlineKeyboardButton("طريقة التفعيل", callback_data="bhowtouse"),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("bcmds"))
async def acbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>- عـزيـزي  [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !</b>
<b>- استخـدم الازرار بالاسفل لمعرفة طريقة التشغيل</b>
\n™""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اوامر التشغيل", callback_data="bbasic"),
                    InlineKeyboardButton("اوامر الادمن", callback_data="badmin"),
                ],[
                    InlineKeyboardButton("العودة", callback_data="arbic")
                ],
            ]
        ),
    )
