
import os
import re
import random

from platform import python_version as kontol
from telethon import events, Button
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://te.legra.ph/file/dcb028440757ea5153898.jpg"

@register(pattern=("activate"))
async def awake(event):
  TEXT += f"Hi {event.sender.first_name}, I'm **SpamGuardian**.\n\n"
  TEXT += f"❄ SpamGuardian Is Alive **"\n\n
  TEXT += f"❄ My Domain : [Primes](https://t.me/PrimesDivision)**\n\n"
  TEXT += f"❄**Powered By: [Primes Team](https://t.me/PrimesxTech)**\n\n"
   Thanks For Adding Me Here ❤️ re ❤️ **"
  BUTTON = [[Button.url("Help", "https://t.me/spamguardianbot?start=help"), Button.url("My Home", "https://t.me/TeleSupportChat")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

