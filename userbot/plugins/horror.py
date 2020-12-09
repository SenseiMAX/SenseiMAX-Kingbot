import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from userbot.utils import admin_cmd

import asyncio

from time import sleep

COLLECTION_STRINGZ = [

  "scary-forest-wallpaper",

  "halloween-screensavers-and-wallpaper",

  "creepy-hd-wallpaper",

  "scary-halloween-wallpapers-and-screensavers",
  
  "slender-man-wallpaper-hd",
  
  "scary-anime-wallpaper",

  "scary-wallpapers-hd-1920x1080"

]

async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGZ) - 1)

    pack = COLLECTION_STRINGZ[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"donottouch.jpg")

@borg.on(admin_cmd(pattern="horrordp ?(.*)"))

async def main(event):

    await event.edit("**Starting horrotr Profile Pic...\n\nDone !!! Check Your DP. Made by @veryhelpful") #Owner @KRAKEN_THE_BADASS,edited by - @veryhelpful

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(600) #Edit this to your required needs
