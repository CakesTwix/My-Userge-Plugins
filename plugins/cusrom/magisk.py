from bs4 import BeautifulSoup
from requests import get
from userge import Message, userge




@userge.on_cmd("magisk$", about={"header": "Get Latest Magisk Zip and Manager"})
async def magisk_(message: Message):
    """Get Latest MAGISK"""
    magisk_repo = "https://raw.githubusercontent.com/topjohnwu/magisk-files/"
    magisk_dict = {
        "⦁ 𝗦𝘁𝗮𝗯𝗹𝗲": magisk_repo + "master/stable.json",
        "⦁ 𝗕𝗲𝘁𝗮": magisk_repo + "master/beta.json",
        "⦁ 𝗖𝗮𝗻𝗮𝗿𝘆": magisk_repo + "master/canary.json",
    }
    releases = "<code><i>𝗟𝗮𝘁𝗲𝘀𝘁 𝗠𝗮𝗴𝗶𝘀𝗸 𝗥𝗲𝗹𝗲𝗮𝘀𝗲:</i></code>\n\n"
    for name, release_url in magisk_dict.items():
        data = get(release_url).json()

        releases += (
            f'{name}: [APK v{data["magisk"]["version"]}]({data["magisk"]["link"]}) \n'
        )

    await message.edit(releases, disable_web_page_preview=True)