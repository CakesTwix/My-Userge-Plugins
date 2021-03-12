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
    url = "https://lolibooru.moe/post/index.json?limit=1&tags=order:random  rating:s"
    async with aiohttp.ClientSession() as session:
            async with session.get(url) as get:
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
    'usage': "{tr}danbooru",
    'options': {'-nsfw': '18+ Art~~'},
    'examples': ['{tr}danbooru -nsfw']}
    )
async def danbooru_(message: Message):
    """ Anime Arts """
    await message.delete()
    url = "https://danbooru.donmai.us/posts.json?limit=1&tags=order:random rating:s"
    if '-nsfw' in message.flags:
        url = "https://danbooru.donmai.us/posts.json?limit=1&tags=order:random rating:e"
    async with aiohttp.ClientSession() as session:
            async with session.get(url) as get:
                answer = await get.json()
                await session.close()

    if answer[0]['tag_string_character'] != "":
        tag = '**Character:** '
        for tags in answer[0]["tag_string_character"].split():
                tag += '#' + tags + ' '
    if answer[0]['tag_string_copyright'] != "":          
        tag += '\n**Copyright:** '
        for tags in answer[0]["tag_string_copyright"].split():
                tag += '#' + tags + ' '
    
    if answer[0]['tag_string_artist'] != "":
        tag += '\n**Artist:** '
        for tags in answer[0]["tag_string_artist"].split():
            tag += '#' + tags + ' '
    
    if answer[0]['source'] != "":
        tag += f'\n**Source:** [Link]({answer[0]["source"]})'


    await message.client.send_photo(chat_id=message.chat.id,
                                    photo=answer[0]["large_file_url"].replace (" ","%20"),
                                    caption=tag,
                                    disable_notification=True)