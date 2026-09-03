from pyrogram import filters
from pyrogram.types import Message
from spr import spr

@spr.on_message(filters.command(["ايدي", "الآيدي"], prefixes=["", "/", "#", "."]))
async def id_arabic(client, message: Message):
    usr = message.from_user
    chat = message.chat
    await message.reply_text(
        f"**معلوماتك الشخصية:**\n"
        f"• الاسم: {usr.first_name}\n"
        f"• الآيدي: `{usr.id}`\n\n"
        f"**معلومات المحادثة:**\n"
        f"• الآيدي: `{chat.id}`"
    )
