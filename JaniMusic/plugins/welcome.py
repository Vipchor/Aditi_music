from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from JaniMusic import app

WELCOME_PHOTO = "https://files.catbox.moe/f7i8t9.jpg"

@app.on_message(filters.new_chat_members & filters.group)
async def welcome(client, message):
    for user in message.new_chat_members:
        text = (
            f"👋 **Welcome {user.mention}**\n\n"
            "🎶 **Official Music Group**\n"
            "🔥 Non-Stop Songs & Masti\n\n"
            "▶️ Song play karne ke liye `/play`\n"
            "❤️ Enjoy & Stay Active"
        )

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎧 Play Music",
                        url="https://t.me/" + app.username
                    )
                ]
            ]
        )

        await message.reply_photo(
            photo=WELCOME_PHOTO,
            caption=text,
            reply_markup=buttons
        )
