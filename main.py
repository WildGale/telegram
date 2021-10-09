import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.message import ContentType
import markups as nav

TOKEN = "2029480345:AAHwiJkt-cbQJy8_NSaFvu3A75SDoNX3_uA"
YOOTOKEN = "381764678:TEST:29893"

logging.basicConfig(level=logging.INFO)

#Init
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приветсвую!', reply_markup = nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == '❤️ ПОДПИСАТЬСЯ':
            await bot.send_message(message.from_user.id, 'Описание подписки', reply_markup = nav.sub_inline_markup)

@dp.callback_query_handler(text="submonth")
async def submonth(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки", description="Описание подписки", payload="month_sub", provider_token=YOOTOKEN, currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб", "amount": 700000}])

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
     if message.successful_payment.invoice_payload == "moth_sub":
        await bot.send_message(message.from_user.id, "Вы подписались на один месяц!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)              