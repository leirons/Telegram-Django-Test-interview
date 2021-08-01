from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# MainMenu
bitcoin = KeyboardButton("Bitcoin")
etherium = KeyboardButton("Etherium")
dogecoin = KeyboardButton('DogeCoin')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(bitcoin, etherium, dogecoin)
