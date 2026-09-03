from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@spr.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("صنع بوتات 🤖", url="https://t.me/odox_2bot")]
        ]
    )
    await message.reply_text(
        "أهلاً بك في سورس حماية تي بي 🛡️\nاختر أحد الخيارات أدناه:",
        reply_markup=keyboard
    )
