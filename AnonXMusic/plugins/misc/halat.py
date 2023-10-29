import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint


@app.on_message(filters.command(["استوري","حالات","فيديو"],""))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,50)
    url = f"https://t.me/halatwatsa7/{rl}"
    await client.send_audio(message.chat.id,url,caption="🐉 ¦ تـم اختيـار فيلم لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/Mlze1bot")
                ],
            ]
        )
                           )

@app.on_message(filters.command(["اقتباسات", "اقتباس"],""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/akttbas6/{rl}"
    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار اقتباس لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
