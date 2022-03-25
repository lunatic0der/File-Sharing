# (©)Codexbotz
# Recode By @mrismanaziz

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL1, CHANNEL2, GROUP1, GROUP2, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"• Owner: @{OWNER}\n• Channel 1: @{CHANNEL1}\n• Channel 2: @{CHANNEL2}\n• Group 1: @{GROUP1}\n• Group 2: @{GROUP2}\nㅤ",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close"),
                    ]
                ]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
