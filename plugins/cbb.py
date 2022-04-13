#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Jasa Bot : <a href='tg://user?id={OWNER_ID}'> @TempatBikinBot</a>\n○ CHANNEL 1 : @BlingBlingID</code>\n○ CHANNEL 2 : <a href='https://t.me/ViralBelatungid'>Channel Kita</a>\n○ CHANNEL 3 : <a href='t.me/vipdino'>Click here</a>\n○ CHANNEL 4 : @TemanKasur\n○ GROUP CHAT  : @Havingsexid</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass