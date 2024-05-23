from aiogram import Bot, Dispatcher
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F
import json

BOT_TOKEN = '7192786510:AAFsxcMLd6rDW1SFqoCw8HMhgaRs4GuFntQ'

#
# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class eMailFilter(BaseFilter):
    def __init__(self, my_symbol: str) -> None:
        self.my_symbol = my_symbol

#     async def __call__(self, message: Message) -> str:
#         try:
#             for word in message.text.split():
#                 if self.my_symbol in word:
#                     print(word)
#                     res = word
#                     print(res)
#                     return {'result': res}
#
#         except TypeError:
#             print("ban")
#
#
# @dp.message(eMailFilter('@gmail.com'))
# async def handler(message: Message, result: str):
#     await message.answer('there email in ur message\n' + result)


async def process_start_command(message: Message):
    await message.reply('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


async def send_gif_echo(message: Message):
    await message.reply_animation(animation=message.animation.file_id)


async def send_audio_echo(message: Message):
    await message.reply_audio(audio=message.audio.file_id)


async def send_document_echo(message: Message):
    await message.reply_document(document=message.document.file_id)


async def send_sticker_echo(message: Message):
    await message.reply_sticker(sticker=message.sticker.file_id)


async def send_story_echo(message: Message):
    await message.reply_story(story=message.story.file_id)


async def send_location_echo(message: Message):
    await message.reply_location(message.location.latitude, message.location.longitude)


async def send_contact_echo(message: Message):
    await message.reply_contact(first_name=message.contact.first_name, phone_number=message.contact.phone_number)


async def send_poll_echo(message: Message):
    await message.answer_poll(message.poll.question, message.poll.options)


async def send_video_echo(message: Message):
    await message.reply_video(video=message.video.file_id)


async def send_video_note_echo(message: Message):
    await message.reply_video_note(video_note=message.video_note.file_id)


async def send_photo_echo(message: Message):
    print(message)
    await message.answer_photo(message.photo[0].file_id, '\nкрутая фотка')


async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


async def process_pri_command(message: Message):
    await message.answer(
        'pri the best'
    )


async def process_BGITU_command(message: Message):
    await message.answer(
        'тото сето'
    )


async def process_firstCourse_command(message: Message):
    await message.answer(
        'тото сето'
    )


async def process_savva_command(message: Message):
    await message.answer(
        'ur mum is fantastic\n'
        'poshel nafig blin'
    )


async def process_ivt_command(message: Message):
    await message.answer(
        'best we'
    )


async def send_echo(message: Message):
    await message.reply(text=message.text)


# Регистрируем хэндлеры
dp.message.register(send_gif_echo, F.content_type == ContentType.ANIMATION)
dp.message.register(send_audio_echo, F.content_type == ContentType.AUDIO)
dp.message.register(send_document_echo, F.content_type == ContentType.DOCUMENT)
dp.message.register(send_sticker_echo, F.content_type == ContentType.STICKER)
dp.message.register(send_story_echo, F.content_type == ContentType.STORY)
dp.message.register(send_location_echo, F.content_type == ContentType.LOCATION)
dp.message.register(send_contact_echo, F.content_type == ContentType.CONTACT)
dp.message.register(send_poll_echo, F.content_type == ContentType.POLL)
dp.message.register(send_video_echo, F.content_type == ContentType.VIDEO)
dp.message.register(send_video_note_echo, F.content_type == ContentType.VIDEO_NOTE)
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(process_firstCourse_command, Command(commands='firstCourse'))
dp.message.register(process_BGITU_command, Command(commands='BGITU'))
dp.message.register(process_savva_command, Command(commands='savva'))
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(process_pri_command, Command(commands='pri'))
dp.message.register(process_ivt_command, Command(commands='ivt'))
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
