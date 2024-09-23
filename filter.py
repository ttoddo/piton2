from aiogram import Bot, Dispatcher
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message
import json

with open('config.json') as file:
    config = json.load(file)
BOT_TOKEN: str = config['7192786510:AAFsxcMLd6rDW1SFqoCw8HMhgaRs4GuFntQ']
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
class strToUnicode(BaseFilter):
    def __init__(self):
        self.text: str  