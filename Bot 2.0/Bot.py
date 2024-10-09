import logging
import os
import pandas as pd
import numpy as np


from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

#load_dotenv = ('config.env')

TOKEN = os.getenv('TOKEN')
bot=Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO, filename = "mylog.log")
logger = logging.getLogger(__name__)


@dp.message(Command(commands=['start']))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!\nВведите ФИО правильно, в одну строку с пробелами между фамилией, именем и отчеством'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    dict_list = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G','Д': 'D','Е': 'E','Ё': 'E','Ж': 'ZH','З': 'Z',
    'И': 'I','Й': 'I','К': 'K','Л': 'L','М': 'M','Н': 'N','О': 'O','П': 'P','Р': 'R','С': 'S','Т': 'T',
    'У': 'U','Ф': 'F','Х': 'KH','Ц': 'TS','Ч': 'CH','Ш': 'SH','Щ': 'SHCH','Ы': 'Y','Ъ': 'IE','Э': 'E','Ю': 'IU','Я': 'IA',' ': ' '}
    text=[]
    for i in message.text:
        if i in dict_list.keys():
            name = dict_list[i]
        else:
            name=dict_list.get(i.upper(),"?").lower()
            logging.warning("Введен неизвестный символ ь - {}".format(i))
        text.append(name)
    text="".join(text)
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=text)

if __name__ == '__main__':
    dp.run_polling(bot)