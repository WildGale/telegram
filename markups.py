from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


#Main Menu
btnSub = KeyboardButton('❤️ ПОДПИСАТЬСЯ')
btnSettings = KeyboardButton('Настройки')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnSub)
mainMenu.add(btnSettings)

#Inline btns
sub_inline_markup = InlineKeyboardMarkup(row_width=1)

btnSubMonth = InlineKeyboardButton('Месяц 100$', callback_data='submonth')

sub_inline_markup.insert(btnSubMonth)