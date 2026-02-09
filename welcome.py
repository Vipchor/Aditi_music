from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from JaniMusic import app

# 👉 Yahan apni welcome image ka link daalo
WELCOME_IMAGE = "https://files.catbox.moe/f7i8t9.jpg"

@app.on_message(filters.new_chat_members)
async def welcome(client, message):
    for user in message.new_chat_members:
        caption = (
            f"✨ **Welcome {user.mention}** ✨\n\n"
            f"🎶 Music Lovers Group me aapka swagat hai\n"
            f"🔥 High Quality Songs | ⚡ Fast Play\n\n"
            f"▶️ Song chalane ke liye **/play song name** likhe\n"
            f"💖 Enjoy & Stay Active"
        )

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🎧 Play Music", callback_data="help_menu"),
                    InlineKeyboardButton("💬 Support", url="https://t.me/Esprosupport"),
                ],
                [
                    InlineKeyboardButton("📢 Updates Channel", url="https://t.me/shree_update"),
                ],
            ]
        )

        await message.reply_photo(
            photo=WELCOME_IMAGE,
            caption=caption,
            reply_markup=buttons,
        )
