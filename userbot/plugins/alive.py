import asyncio
from telethon import events
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME, hellversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Sensei"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/d1dfcc8bafcdf7c8ad49e.mp4"
pm_caption = "__**🔥🔥ɦɛʟʟɮօt ɨs օռʟɨռɛ🔥🔥**__\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"😈Hêllẞø†😈       : __**{hellversion}**__\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/HellBot_Official)\n"

pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/@pi_ka_pi)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/hellboy-op/hellbot) 🔹 [📜License📜](https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)"

@bot.on(admin_cmd(outgoing=True, pattern="zinda$"))
@bot.on(sudo_cmd(pattern="zinda$", allow_sudo=True))
async def amireallyzinda(zinda):
    chat = await zinda.get_chat()
    await zinda.delete()
    """ For .zinda command, check if the bot is running.  """
    await borg.send_file(zinda.chat_id, PM_IMG,caption=pm_caption)
    await zinda.delete() 
