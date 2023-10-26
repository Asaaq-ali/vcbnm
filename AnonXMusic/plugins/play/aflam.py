import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from AnonXMusic import app
from config import BANNED_USERS

#########################################################################################
###############msrahia##########################################################################
#################drama########         # Aflam Arabic #             ##########################
#########################################################################################
#########################################################################################
@app.on_message(
    filters.command(["افلام"],"")
    & filters.group
)
async def aflamAR(c: Client, m: Message):
    global mid
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("افلام 📼", callback_data="film " + str(m.from_user.id))],
        [InlineKeyboardButton("افلام 📼", callback_data="film " + str(m.from_user.id))],
  
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],

    ])
    
# Replay Edit
@app.on_callback_query(filters.regex("^aflamAR2 (\\d+)$"))
async def aflamAR2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("افلام 📼", callback_data="film " + str(m.from_user.id))],
        [InlineKeyboardButton("افلام 📼", callback_data="film " + str(m.from_user.id))],
  
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الافلام والمسلسلات \n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^film (\\d+)$"))
async def film(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("كوري 🇰🇷", callback_data="comedy " + str(m.from_user.id))],
        [InlineKeyboardButton("صيني 🇨🇳", callback_data="action " + str(m.from_user.id))],
   
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="aflamAR2 " + str(m.from_user.id))],
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],
        
    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الافلام \n√", reply_markup=keyboard)


#########################################################################################
#########################################################################################
#########################         # Aflam Comedy #             ##########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^comedy (\\d+)$"))
async def comedy(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ النبيل", callback_data="Xco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ المرشحة الصادقة ", callback_data="Xco2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المحتالون ", callback_data="Xco3 " + str(m.from_user.id))] +
     
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="film " + str(m.from_user.id))],
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("◍ اهلا بك في قائمة الافلام الكوريه \n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco1 (\\d+)$"))
async def Xco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم  :  النبيل
    🌎 الدولة : كوريا
    🗄 تصنيف : اكشن
    📜 قصة الفيلم:
يسافر ملاكم نصف كوري-فلبيني إلى كوريا على أمل إيجاد والده،
ليجد نفسه مطارداً من قبل مجموعات مختلفة من الأشخاص
يسعون جميعهم خلفه دون أن يعرف سبب استهدافهم له.
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco2 (\\d+)$"))
async def Xco2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : المرشحة الصادقة 
        📖 انتاج سنة  : 2020
        🌎 الدولة : كوريا
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
تدور الأحداث عن عضوة مجلس وطني يجري الكذب في عروقها مجرى الدم لكن بعد حادثة غير متوقعة تجد نفسها مجبرة على قول الحقيقة أثناء شروعها في حملة إعادة انتخابها.

        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco3 (\\d+)$"))
async def Xco3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : المحتالون
         انتاج سنة : 2017
        🌎 الدولة : كوريا
        🗄 تصنيف : أكشن، اثاره، تشويق
        📜 قصة الفيلم:
يتحدث فيلم “The Swindlers” “عن جي سونغ” (هيون بن) هو محتال ذكي الذي يشكل خطة و يخدع فقط زملائه المحتالين ليمسك بـ جانغ دو تشيل و يقوم أولا بتجنيد المدعي العام هيو سو (يو جي تاي) ثم بقية المحتالين (باي سونغ وو)، وشون جا (نانا)، والرئيس كيم (أن سي-ها) ليلقون بـالطعم لـ سيونغ-غان (بارك سونغ-وونغ) اليد اليمنى لجانغ دو تشيل
        """, reply_markup=keyboard)



#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^XXco1 (\\d+)$"))
async def XXco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/afalm1/2", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco3 (\\d+)$"))
async def XXco3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/afalm1/6", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco5 (\\d+)$"))
async def XXco5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/afalm1/7", reply_to_message_id=mid)

#####
@app.on_callback_query(filters.regex("^action (\\d+)$"))
async def action(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("النهاية ", callback_data="Xact1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مصاصي الدماء ", callback_data="Xact2 " + str(m.from_user.id))],
   
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="aflamAR2 " + str(m.from_user.id))],
        [InlineKeyboardButton("السورس ✅", url=f"https://t.me/Mlze1bot")],

    ])
    await m.message.edit_text("اهلا بك في قائمة الافلام الاكشن الصينيه", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact1 (\\d+)$"))
async def Xact1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : النهاية 
📖 انتاج سنة : 2019
🌎 الدولة : الصين
🗄 تصنيف : اكشن , اثارة , تشويق
📜 قصة الفيلم:
تدور قصة الجزء الرابع حيث في العام 1964، بعد وفاة زوجته، يسافر إيب مان إلى سان فرانسيسكو لتخفيف التوترات بين أساتذة الكونغ فو المحليين وطالبه النجم، بروس لي، خلال البحث عن مستقبل أفضل لابنه.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact2 (\\d+)$"))
async def Xact2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رجوع ⬅️", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : مصاصي الدماء
📖 انتاج سنة : 2017
🌎 الدولة : الصين
🗄 تصنيف : اكشن , اثارة , رعب
📜 قصة الفيلم:
ينضم تيم تشيونج إلى منظمة إبادة مصاصي الدماء و هي منظمة سرية تهدف للقضاء عليهم و يديرها عمه تشاو، يقوم تيم لاحقاً بالحفاظ على حياة مصاصة الدماء سومار و يحاول حمايتها من قائدها الشرير الذي قام بدفنها و هي حية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^XXact1 (\\d+)$"))
async def XXact1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/afalm1/4", reply_to_message_id=mid)

@app.on_callback_query(filters.regex("^XXact3 (\\d+)$"))
async def XXact3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/afalm1/9", reply_to_message_id=mid)

##########################################قف هنا#####





