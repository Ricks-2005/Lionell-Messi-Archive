from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from Messi import pbot
from Messi.utils.errors import capture_err
from Messi.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


MEMEK = "https://te.legra.ph/file/dcb028440757ea5153898.jpg"

@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=MEMEK,
        caption=f"""✨ **Hey I'm SpamGuardian** 

**Owner of repo : [PrimesDivision](https://t.me/SpamGuardianBot)**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`
** My collaborators**
** 1) [Flame](https://t.me/CipherFlame)**
** 1) [Alpha](https://t.me/immortalsxking)**
** 2) [Ds x Hashira](https://t.me/ricks_005)**

**Follow The Given Buttons For Source Code**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source", url="https://github.com/rick40096/lionell-messi-archive"), 
                    InlineKeyboardButton(
                        "Support", url="https://t.me/RengokuSupport")
                ]
            ]
        )
    )
