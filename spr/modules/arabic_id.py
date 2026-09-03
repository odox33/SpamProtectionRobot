from pyrogram import filters
from pyrogram.types import Message
from spr import spr


@spr.on_message(filters.command(["ايدي", "الآيدي", "أيدي"], prefixes=["", "/", "#", "."]) & filters.group)
async def arabic_id_command(_, message: Message):
    user = message.from_user
    chat = message.chat
    
    text = (
        f"**معلوماتك الشخصية:**\n"
        f"• الاسم: {user.mention}\n"
        f"• الآيدي: `{user.id}`\n\n"
        f"**معلومات المجموعه:**\n"
        f"• اسم المجموعة: {chat.title}\n"
        f"• آيدي المجموعة: `{chat.id}`"
    )
    
    await message.reply_text(text)

__MODULE__ = "Arabic ID"
__HELP__ = "اكتب 'ايدي' في المجموعة ليقوم البوت بإرسال معلوماتك وآيدي المجموعة."
