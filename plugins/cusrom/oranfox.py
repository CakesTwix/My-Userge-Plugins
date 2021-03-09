# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# Copyright (C) 2021 BY - GitHub.com/CakesTwix [TG - @CakesTwix]
# All rights reserved.

import requests
from userge import Message, userge
from datetime import datetime


@userge.on_cmd(
    "ofox",
    about={
        "header": "get orangefox recovery by device codename do"
        ".ofox codename"
    },
)
async def ofox_(message: Message):
    if not message.input_str:
        await message.err("Provide a device codename to search recovery", del_in=2)
        return
    photo = "https://i.imgur.com/582uaSk.png"
    API_HOST = "https://api.orangefox.download/v3/devices/get?codename="
    codename = message.input_str
    cn = requests.get(f"{API_HOST}{codename}")
    r = cn.json()
    try:
        s = requests.get(f"https://api.orangefox.download/v3/releases/?codename={codename}").json()

        info = f"📱 **Device**: {r['full_name']}\n"
        info += f"👤 **Maintainer**: {r['maintainer']['name']}\n\n"

        recovery = f"🦊 <code>OrangeFox Project Recovery {s['data'][0]['version']} | {s['data'][0]['type']}</code>\n"

        msg = info
        msg += recovery
        msg += f"🧾 <code>{s['data'][0]['md5']}</code>\n"
        msg += f"📅 <code>{datetime.utcfromtimestamp(s['data'][0]['date']+10800).strftime('%Y-%m-%d %H:%M:%S')}</code>\n"
        msg += f"⬇️ <a href={r['url']}>DOWNLOAD</a> | {round(s['data'][0]['size']/1e+6,1)}MB"
        await userge.send_photo(message.chat.id, photo=photo, caption=msg) 
    except:
        await message.err(f"OrangeFox not found for {codename}!", del_in=3)
