import random, re
import asyncio
from userbot.utils import admin_cmd
from telethon import events

@borg.on(admin_cmd(pattern="spmsg (.*)"))
async def _(event):
    name = event.pattern_match.group(1)
    if event.fwd_from:
        return
    await event.edit(f"{name} {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name}{name}\n{name} {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name} {name}\n{name} {name}{name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name}{name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name}{name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name}{name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name}{name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}")






