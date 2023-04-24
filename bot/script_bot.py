from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

import config
import sys

bot = Bot(config.bot_token)
dp = Dispatcher(bot, 
                storage=MemoryStorage())

class ClientStatesGroup(StatesGroup):
    login = State()

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
login_button = KeyboardButton("Войти")
start_keyboard.add(login_button)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет! Этот бот - электронный дневник Edu Tatar.\nЧтобы начать работу с ним нажми на кнопку Войти',
                           reply_markup=start_keyboard)

@dp.message_handler(Text(equals="Войти"))
async def cmd_login(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отправьте свой Логин и пароль в таком формате:\n\n"Логин"\n"Пароль"')
    await ClientStatesGroup.login.set()

@dp.message_handler(state=ClientStatesGroup.login)
async def login(message: types.Message, state: FSMContext):
    login = message.text.split('\n')[0]
    password = message.text.split('\n')[1]

    sys.path.insert(0, "C:/Users/user/MyProjects/MyPythonProjects/Edu Tatar/script")

    import script_login
    res = script_login.login(login, password)
    
    if res[0] == 'true':
        user_name = res[1][0]
        user_login = res[1][1]
        await bot.send_message(message.from_user.id, f'Успешная автонризация!\nЛогин: {user_login}\nФИО: {user_name}')
        await state.finish()
    elif res[0] == 'false':
        await bot.send_message(message.from_user.id, 'Не удалось выполнить вход!\nНеправильный Логин или пароль')
        await state.finish()
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)