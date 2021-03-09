""" Взаимодействие с сайтом anilibria.tv """
# 2021 
# https://github.com/CakesTwix/My-Userge-Plugins 
# Telegram - @CakesTwix

from userge import userge, Message
import aiohttp


@userge.on_cmd("random", about={
    'header': "Рандомный тайтл",
    'description': 'Случайное аниме',
    'usage': "{tr}random"})
async def random_(message: Message):
    """ Случайное аниме """
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


@userge.on_cmd("find", about={
    'header': "Найти тайтл по названию(берется только первое аниме из списка)",
    'description': 'Поиск по названию',
    'usage': "{tr}find <название>"})
async def find_(message: Message):
    """ Поиск по названию """
    name = message.filtered_input_str
    async with aiohttp.ClientSession() as session:
            async with session.get("https://api.anilibria.tv/v2/searchTitles?search=" + name) as get:
                answer = await get.json()
                await session.close()
                if 'error' in answer or answer == []:
                    await message.edit("Ничего не найдено", del_in=3)
                    return
    
    await message.delete()                
    caption=answer[0]["names"]["ru"]
    caption+="\n ```Статус:``` " + answer[0]["status"]["string"]
    caption+="\n ```Тип:``` " + answer[0]["type"]["full_string"]
    caption+="\n ```Год:``` " + str(answer[0]["season"]["year"])
    await message.client.send_photo(chat_id=message.chat.id,
                                    photo="https://www.anilibria.tv"+answer[0]["poster"]["url"],
                                    caption=caption,
                                    disable_notification=True)                                