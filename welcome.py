from pyrogram import filters
from JaniMusic import app

@app.on_message(filters.new_chat_members)
async def welcome(client, message):
    for user in message.new_chat_members:
        await message.reply_text(
            f"👋 Welcome {user.mention}\n"
            f"🎶 Music sunne ke liye /play use kare"
        )
