from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from spr import spr

@spr.on_message(filters.command(["start"]) & filters.private)
async def odox_start_handler(_, message: Message):
    text = (
        f"**مرحباً بك عزيزي {message.from_user.mention} في سورس حماية تي بي (TB) 🛡️**\n\n"
        "• يمكنك حماية مجموعتك من السبام والسبامرز بكفاءة عالية.\n"
        "• يمكنك أيضاً إنشاء بوت حماية الخاص بك مجاناً أو الاشتراك بالنسخة المدفوعة.\n\n"
        "اختر ما تناسبك من الأزرار في الأسفل 👇"
    )
    
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🤖 صنع بوت مجاني", url="https://t.me/odox_2bot"),
                InlineKeyboardButton("💎 صنع بوت مدفوع", url="https://t.me/odox3")
            ],
            [
                InlineKeyboardButton("📢 قناة السورس", url="https://t.me/odox_6"),
                InlineKeyboardButton("👨‍💻 حساب المطور", url="https://t.me/odox3")
            ]
        ]
    )
    
    await message.reply_text(text=text, reply_markup=keyboard, disable_web_page_preview=True)
