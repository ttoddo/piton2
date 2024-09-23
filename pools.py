from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, URLInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder
eat_count = 0
mush_count = 0
# Токен бота
BOT_TOKEN = '7192786510:AAFTRZflUgo-J1T_IwMsC1ZxAYd6VieFo_M'  # Замените на ваш токен

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

eat_first_builder = ReplyKeyboardBuilder()
eat_second_builder = ReplyKeyboardBuilder()
eat_third_builder = ReplyKeyboardBuilder()

mush_first_builder = ReplyKeyboardBuilder()
mush_second_builder = ReplyKeyboardBuilder()
mush_third_builder = ReplyKeyboardBuilder()

# Создаем кнопки
survey_btn = KeyboardButton(text='Анкета')
pool1_btn = KeyboardButton(text='Съедобное/несъедобное')
pool2_btn = KeyboardButton(text='Грибовик')
x = 3
a = 'Да'
b = 'Нет'
c = 'Не знаю'
eat_first: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(x)
]
i = 0
for k in range(1):
    eat_first[i] = KeyboardButton(text=f'{a}')
    i += 1
    eat_first[i] = KeyboardButton(text=f'{b}')
    i += 1
    eat_first[i] = KeyboardButton(text=f'{c}')


eat_second: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(x)
]
i = 0
while i != x:
    eat_second[i] = KeyboardButton(text=f'{a}')
    i += 1
    eat_second[i] = KeyboardButton(text=f'{b}')
    i += 1
    eat_second[i] = KeyboardButton(text=f'{c}')
    i += 1

eat_third: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(x)
]
i = 0
while i != x:
    eat_third[i] = KeyboardButton(text=f'{a}')
    i += 1
    eat_third[i] = KeyboardButton(text=f'{b}')
    i += 1
    eat_third[i] = KeyboardButton(text=f'{c}')
    i += 1


mush_first: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(x)
]
i = 0
while i != x:
    mush_first[i] = KeyboardButton(text='Поганка')
    i += 1
    mush_first[i] = KeyboardButton(text='Дымовик')
    i += 1
    mush_first[i] = KeyboardButton(text='Трутовик')
    i += 1
mush_second: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(x)
]
i = 0
while i != x:
    mush_second[i] = KeyboardButton(text='Лисичка')
    i += 1
    mush_second[i] = KeyboardButton(text='Свинух')
    i += 1
    mush_second[i] = KeyboardButton(text='Подосиновик')
    i += 1
mush_third: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i + 1}') for i in range(x)
]
i = 0
while i != x:
    mush_third[i] = KeyboardButton(text='Плесень')
    i += 1
    mush_third[i] = KeyboardButton(text='Мухомор')
    i += 1
    mush_third[i] = KeyboardButton(text='Белый')
    i += 1
# Добавляем кнопки в билдер
kb_builder.row(survey_btn, pool1_btn, pool2_btn, width=2)

eat_first_builder.row(*eat_first, width=2)
eat_second_builder.row(*eat_second, width=2)
eat_third_builder.row(*eat_third, width=2)

mush_first_builder.row(*mush_first, width=2)
mush_second_builder.row(*mush_second, width=2)
mush_third_builder.row(*mush_third, width=2)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)
eat_keyboards = [eat_first_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
),
    eat_second_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    ),
    eat_third_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )]

mush_keyboards = [mush_first_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
),
    mush_second_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    ),
    mush_third_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True
    )]

# Опросные вопросы
survey_questions = [
    "Имя",
    "Фамилия",
    "Грибной стаж"
]
# Вопросы викторин
quiz_questions = {
    'eat_photo': ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcVjWlIsGP97s8QyOrjIc2hWsUGmzsXxav4A&s",
                "https://upload.wikimedia.org/wikipedia/commons/1/12/2005-09_Amanita_phalloides_crop.jpg",
                  "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Amanita_muscaria_3_vliegenzwammen_op_rij.jpg/275px-Amanita_muscaria_3_vliegenzwammen_op_rij.jpg"],
    'eat': ["Съедобен ли этот гриб",
                  "А этот?",
                  "А что cкажете про этот?"],
    'mush': ["Что это за гриб",
                  "А этот",
                  "И последний"],
    'mush_photo': ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWEoIPrbQ-LzpIc9r8gu5QuFpn-YxBXefNZg&s",
                    "https://avatars.dzeninfra.ru/get-zen_doc/1648379/pub_61a97df4924136357006fa4a_61a97e1336045133bef75eaa/scale_1200",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhwXKsfEP7V9ni6vp9baHyMoaU97wZL5XZ2Q&s"]
}

# Переменные для хранения состояния пользователя
user_data = {}


# Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo('https://3fc4ed44-3fbc-419a-97a1-a29742511391.selcdn.net/coub_storage/media_block'
                               '/cw_image/d9c8950c727/93191f1cc0d0e95737c48/1587108573_3c74wg_1587108518_s7ulc7_att'
                               '-url-download.jpg',"Аааа, это мой гриб! Выбери команду", reply_markup=keyboard)


# Обработчик кнопки "Пройти опрос"
@dp.message(lambda message: message.text == 'Анкета')
async def start_survey(message: Message):
    user_data[message.from_user.id] = {"survey_step": 0, "survey_answers": []}
    await ask_survey_question(message)


async def ask_survey_question(message: Message):
    user_id = message.from_user.id
    step = user_data[user_id]["survey_step"]
    question = survey_questions[step]
    await message.answer(question, reply_markup=types.ReplyKeyboardRemove(
    ))  # Убираем клавиатуру для ввода текста



@dp.message(lambda message: message.text == 'Съедобное/несъедобное')
async def start_survey(message: Message):
    user_data[message.from_user.id] = {"eat_step": 0, "eat": []}
    await ask_eat_question(message)


async def ask_eat_question(message: Message):
    user_id = message.from_user.id
    step = user_data[user_id]["eat_step"]
    p = quiz_questions['eat_photo'][step]
    question = quiz_questions['eat'][step]
    await message.answer_photo(URLInputFile(p), f'{question}', reply_markup=eat_keyboards[step])




@dp.message(lambda message: message.text == 'Грибовик')
async def start_survey(message: Message):
    user_data[message.from_user.id] = {"mush_step": 0, "mush": []}
    await ask_mush_question(message)


async def ask_mush_question(message: Message):
    user_id = message.from_user.id
    step = user_data[user_id]["mush_step"]
    p = quiz_questions['mush_photo'][step]
    question = quiz_questions['mush'][step]
    await message.answer_photo(URLInputFile(p), f'{question}', reply_markup=mush_keyboards[step])


@dp.message(lambda message: message.from_user.id in user_data and "survey_step" in user_data[message.from_user.id])
async def handle_survey_answer(message: Message):
    user_id = message.from_user.id
    step = user_data[user_id]["survey_step"]
    user_data[user_id]["survey_answers"].append(message.text)

    # Если есть еще вопросы
    if step + 1 < len(survey_questions):
        user_data[user_id]["survey_step"] += 1
        await ask_survey_question(message)
    else:
        # Выводим результаты опроса
        results = "\n".join(f"{q}: {a}" for q, a in zip(survey_questions, user_data[user_id]["survey_answers"]))
        await message.answer(f"{results}", reply_markup=keyboard)
        del user_data[user_id]  # Очищаем данные пользователя после завершения опроса


@dp.message(lambda message: message.from_user.id in user_data and "eat_step" in user_data[message.from_user.id])
async def handle_eat_answer(message: Message):
    user_id = message.from_user.id
    step = user_data[user_id]["eat_step"]
    user_data[user_id]["eat"].append(message.text)

    # Если есть еще вопросы
    if step + 1 < len(quiz_questions["eat"]):
        user_data[user_id]["eat_step"] += 1
        await ask_eat_question(message)
    else:
        # Выводим результаты опроса
        results = "\n".join(
            f"{q}: {s}" for q, s in zip(quiz_questions["eat"], user_data[user_id]["eat"]))
        await message.answer(f"Результат:\n{results}\n", reply_markup=keyboard)
        del user_data[user_id]  # Очищаем данные пользователя после завершения опроса
@dp.message(lambda message: message.from_user.id in user_data and "mush_step" in user_data[message.from_user.id])
async def handle_mush_answer(message: Message):
    user_id = message.from_user.id
    step = user_data[user_id]["mush_step"]
    user_data[user_id]["mush"].append(message.text)

    # Если есть еще вопросы
    if step + 1 < len(quiz_questions["mush"]):
        user_data[user_id]["mush_step"] += 1
        await ask_mush_question(message)
    else:
        # Выводим результаты опроса
        results = "\n".join(
            f"{q}: {s}" for q, s in zip(quiz_questions["mush"], user_data[user_id]["mush"]))
        await message.answer(f"Результат:\n{results}\n", reply_markup=keyboard)
        del user_data[user_id]
# Запуск бота
if __name__ == '__main__':
    dp.run_polling(bot)
