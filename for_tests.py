import re
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, BaseFilter
from aiogram.types import Message, PhotoSize
import logging


TOKEN = ""
with open('secret.txt', 'r') as q:
    text = q.read()
    TOKEN = re.match(r'token:([:\w-]*$)', text).group(1)

bot = Bot(token=TOKEN)
dp = Dispatcher()
admin_ids = [1393291388]
logger = logging.getLogger('QQ')



@dp.message(F.photo[-1].as_('photo_max'))
async def pereslat_photo(message: Message, photo_max: PhotoSize):
    await message.reply_photo(photo_max.file_id)

class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

@dp.message(IsAdmin(admin_ids))
async def q(message: Message):
    await message.answer("Вы админ")





@dp.message()
async def qq(message: Message):
    await message.answer('ты пидор')

if __name__ == '__main__':
    print(logger)
    logger.warning('Предупреждение!')
    logger.error('Отладочная информация')
    dp.run_polling(bot)
