from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
BOT_TOKEN = '7192786510:AAFTRZflUgo-J1T_IwMsC1ZxAYd6VieFo_M'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()





kb_builder = ReplyKeyboardBuilder()

x = int(input())

# Создаем первый список с кнопками
buttons_1: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(x)
]
for i in range(x):
    a = str(input())
    buttons_1[i] = KeyboardButton(text=f'{a}')
# Распаковываем список с кнопками методом add
kb_builder.add(*buttons_1)


# Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах,
# а также говорим методу повторять такое размещение для остальных рядов
kb_builder.adjust(2, 1, 3, 5, 10, 5, 3, 2, 1, repeat=True)




# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Вот такая получается клавиатура',
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )
if __name__ == '__main__':
    dp.run_polling(bot)
