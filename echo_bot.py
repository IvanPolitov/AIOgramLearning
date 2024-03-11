import re
# import requests
# import time
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType


TOKEN = ""
with open("secret.txt", "r") as q:
    text = q.read()
    TOKEN = re.match(r'token:([:\w-]*$)', text).group(1)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Присылает текст, старт
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Присылает текст, хелп
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# присылает фото в ответ на фото
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


# --- аудио
@dp.message(F.audio)
async def send_audio_echo(message: Message):
    await message.answer_audio(message.audio.file_id)


# --- видео
@dp.message(F.video)
async def send_video_echo(message: Message):
    await message.answer_video(message.video.file_id)


# --- сткер
@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.answer_sticker(message.sticker.file_id)


# --- гифка
@dp.message(F.animation)
async def send_animation_echo(message: Message):
    await message.answer_animation(message.animation.file_id)


# --- документ
@dp.message(F.document)
async def send_document_echo(message: Message):
    await message.answer_document(message.document.file_id)


# --- гс
@dp.message(F.voice)
async def send_voice_echo(message: Message):
    await message.answer_voice(message.voice.file_id)


# пересылает в ответ всё остальное
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается методом send_copy'
        )


if __name__ == '__main__':
    dp.run_polling(bot)
