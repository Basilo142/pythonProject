from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='***')
dp = Dispatcher(bot)


@dp.message_handler()
async def get_mes(message: types.Message):

    chat_id = message.chat.id
    send = await bot.send_message(chat_id=chat_id, text='asdasd')
    print(send.to_python())

executor.start_polling(dp)
