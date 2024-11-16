from pyrogram import filters
from devgagan import app
from devgagan.core import script
from devgagan.core.func import subscribe
from config import OWNER_ID
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------- Start-Buttons ------------------- #

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Join Channel", url="https://t.me/+v4k9PpU_fxtmYmNl")],
        [InlineKeyboardButton("Buy Premium", url="https://t.me/+v4k9PpU_fxtmYmNl")]
    ]
)

@app.on_message(filters.command("start"))
async def start(_, message):
    join = await subscribe(_, message)
    if join == 1:
        return
    await message.reply_photo(photo="https://images.app.goo.gl/KA14FzkZk3aCTaUi8",
                              caption=script.START_TXT.format(message.from_user.mention), 
                              reply_markup=buttons)
