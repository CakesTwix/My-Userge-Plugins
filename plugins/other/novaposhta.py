from userge import userge, Message
import aiohttp


@userge.on_cmd("novaposhta", about={
    'header': "Трекинг посылки",
    'description': 'Получение информации про посылку по номеру',
    'usage': "{tr}novaposhta <Номер>"})
async def novaposhta_(message: Message):
    DocumentNumber = message.filtered_input_str
    
    Data={
        "apiKey": "abe3a74549c55e4b703ed042c5169406",
        "modelName": "TrackingDocument",
        "calledMethod": "getStatusDocuments",
        "methodProperties": {
            "Documents": [
            {
                "DocumentNumber": DocumentNumber,
                "Phone":""
            }
        ]
    }
    
    }

    async with aiohttp.ClientSession() as session:
            async with session.get("https://api.novaposhta.ua/v2.0/json/", json=Data) as get:
                answer = await get.json()
                await session.close()
    item = answer['data'][0]

    caption = f"**Экспресс-накладная: **{item['Number']}"
    caption += f"\n**Статус: **{item['Status']}"
    if 'DateCreated' in item:
        caption += f"\n**Было создано: **{item['DateCreated']}"
        caption += f"\n**Ожид. дата доставки: **{item['ScheduledDeliveryDate']}"
        caption += f"\n```{item['CitySender']} -> {item['CityRecipient']}```"

    if item.get('DocumentCost') != None:
        caption += f"\n**Цена доставки: **{item['DocumentCost']} грн."

    await message.edit(caption)

