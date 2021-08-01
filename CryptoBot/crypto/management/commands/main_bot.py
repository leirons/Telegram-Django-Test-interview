from django.core.management.base import BaseCommand, CommandError
from aiogram import Bot, Dispatcher, executor, types

from . import markups
from . import coin_parser
from . import work_with_db as db

from django.conf import settings


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        bot = Bot(settings.TOKEN)
        dp = Dispatcher(bot)

        @dp.message_handler(commands=['start', 'menu'])
        async def menu(message: types.Message):
            await bot.send_message(message.from_user.id, f'Вы перешли в главное меню', reply_markup=markups.mainMenu)

        @dp.message_handler()
        async def sub_menu(message: types.Message):
            await db.create_user_profile(request=message.from_user.id, name=message.from_user.first_name,
                                         surname=message.from_user.last_name)
            if message.text == 'Bitcoin':
                coin = coin_parser.get_coins('Bitcoin')
                crypto_name = coin['crypto_name']
                crypto_value = coin['crypto_value']
                await bot.send_message(message.from_user.id, f'{crypto_name},Цена: {crypto_value}')
            elif message.text == 'Etherium':
                coin = coin_parser.get_coins('Ethreium')
                crypto_name = coin['crypto_name']
                crypto_value = coin['crypto_value']
                await bot.send_message(message.from_user.id, f'{crypto_name},Цена: {crypto_value}')
            elif message.text == 'Dogecoin':
                coin = coin_parser.get_coins('Ethreium')
                crypto_name = coin['crypto_name']
                crypto_value = coin['crypto_value']
                await bot.send_message(message.from_user.id, f'{crypto_name},Цена: {crypto_value}')
            else:
                await bot.send_message(message.from_user.id, 'К сожалению мы не можем обработать ваш запрос.')

        executor.start_polling(dispatcher=dp, skip_updates=True)
