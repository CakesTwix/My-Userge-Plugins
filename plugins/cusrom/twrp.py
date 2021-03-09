from bs4 import BeautifulSoup
from requests import get
from userge import Message, userge


@userge.on_cmd(
    "twrp",
    about={"header": "Find twrp for you device", "usage": "{tr}twrp <device codename>"},
    allow_via_bot=True,
)
async def device_recovery(message: Message):
    """ Get Latest TWRP """
    message.reply_to_message
    args = message.filtered_input_str
    if args:
        device = args
    else:
        await message.err("```Provide Device Codename !!```", del_in=3)
        return
    url = get(f"https://dl.twrp.me/{device}/")
    if url.status_code == 404:
        reply = f"`Couldn't find twrp downloads for {device}!`\n"
        return await message.edit(reply, del_in=5)
    page = BeautifulSoup(url.content, "lxml")
    download = page.find("table").find("tr").find("a")
    dl_link = f"https://dl.twrp.me{download['href']}"
    dl_file = download.text
    size = page.find("span", {"class": "filesize"}).text
    date = page.find("em").text.strip()
    reply = (
        f"**Latest TWRP for {device}:**\n"
        f"[{dl_file}]({dl_link}) - __{size}__\n"
        f"**Updated:** __{date}__"
    )
    await message.edit(reply)