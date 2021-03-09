from userge import userge, Message
import aiohttp


@userge.on_cmd("random", about={
    'header': "Рандомный тайтл",
    'usage': "{tr}random"})
async def random_(message: Message):
    await message.delete()
    async with aiohttp.ClientSession() as session:
            async with session.get("https://api.anilibria.tv/v2/" + 'getRandomTitle') as get:
                answer = await get.json()
                await session.close()
                if 'error' in answer:
                    raise Exception(f'API Error: {(answer["error"]["code"])} | {(answer["error"]["message"])}')

    caption=answer["names"]["ru"]
    caption+="\n ```Статус:``` " + answer["status"]["string"]
    caption+="\n ```Тип:``` " + answer["type"]["full_string"]
    caption+="\n ```Год:``` " + str(answer["season"]["year"])
    await message.client.send_photo(chat_id=message.chat.id,
                                    photo="https://www.anilibria.tv"+answer["poster"]["url"],
                                    caption=caption,
                                    disable_notification=True)