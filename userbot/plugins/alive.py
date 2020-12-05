import time

import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://media.giphy.com/media/3oEjI0naHAj6j8Bn2M/giphy.gif"
pm_caption = "⚠️ ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot is On 🔥 FIRE �⚠️ \n\n"
pm_caption += "🔸**SYSTEM STATUs**\n"
pm_caption += "🔹TELETHON VERSION : **6.0.9**\n ⭕️ Python: **3.7.4**\n"
pm_caption += "🔸DATABASE STATUS  : **Functional**\n"
pm_caption += f"🔸 **Uptime** : `{uptime}` \n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += "🔸**ᔕᗴᑎᔕᗴᎥᗰᗩ᙭ OS** :   1.15`\n"
pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [MIT License](https://github.com/SenseiMAX/SenseiMAX-Kingbot/blob/master/LICENSE)\n"
pm_caption += "🔸**Made By 😎** : [This Peros](https://t.me/senseimaxxx)\n\n"
pm_caption += "➥ **Check Stats By Doing** `.stat`. \n\n"
pm_caption += "🔻Deploy ᔕᗴᑎᔕᗴᎥᗰᗩ᙭-Kingbot : [ℝ𝕖𝕡𝕠](https://github.com/SenseiMAX/SenseiMAX-Kingbot)\n"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
