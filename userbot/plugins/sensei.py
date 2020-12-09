#by @sensei_nex

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("sensei"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "sensei":
    await event.edit("@Sensei_nex")
    animation_chars = [
            "@Sensei_nex tera baap",
            "@Sensei_nex is bot ka creator",
            "@Sensei_nex bot ko jaan dene wala",
            "@Sensei_nex owner of @SenseiMAXprojects ",
            "tujhe aur kya chaiye vo hai mere sath",
            "tera baap",
            "@Sensei_nex"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
