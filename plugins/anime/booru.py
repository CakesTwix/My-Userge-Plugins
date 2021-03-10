""" Anime Arts (Booru) """


from userge import userge, Message
import aiohttp


@userge.on_cmd("loli", about={
    'header': "Loli Arts! From lolibooru.moe",
    'description': 'Sending art with little illegal girls',
    'usage': "{tr}loli"})
async def loli_(message: Message):
    """ Loli! """
    await message.delete()
    async with aiohttp.ClientSession() as session:
            async with session.get("https://lolibooru.moe/post/index.json?limit=1&tags=order:random  rating:s") as get:
                answer = await get.json()
                await session.close()
    tag = ''
    for tags in answer[0]["tags"].split():
                tag += '#' + tags + ' '
    await message.client.send_photo(chat_id=message.chat.id,
                                    photo=answer[0]["sample_url"].replace (" ","%20"),
                                    caption=tag,
                                    disable_notification=True)


@userge.on_cmd("danbooru", about={
    'header': "Anime Arts! From danbooru.donmai.us",
    'description': 'Sending art from danbooru',
    'usage': "{tr}danbooru"})
async def loli_(message: Message):
    """ Anime Arts """
    await message.delete()
    async with aiohttp.ClientSession() as session:
            async with session.get("https://danbooru.donmai.us/posts.json?limit=1&tags=order:random rating:s") as get:
                answer = await get.json()
                await session.close()
    tag = ''
    for tags in answer[0]["tag_string"].split():
                tag += '#' + tags + ' '
    await message.client.send_photo(chat_id=message.chat.id,
                                    photo=answer[0]["large_file_url"].replace (" ","%20"),
                                    caption=tag,
                                    disable_notification=True)