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
    LoginEduTatar = State()

StartKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
LoginEduTatar_Button = KeyboardButton('Войти')
StartKeyboard.add(LoginEduTatar_Button)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет! Этот бот - электронный дневник Edu Tatar.\nЧтобы начать работу с ним нажми на кнопку Войти',
                           reply_markup=StartKeyboard)

@dp.message_handler(Text(equals="Войти"))
async def cmd_login(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отправьте свой Логин и пароль в таком формате:\n\n"Логин"\n"Пароль"')
    await ClientStatesGroup.LoginEduTatar.set()

@dp.message_handler(state=ClientStatesGroup.LoginEduTatar)
async def login(message: types.Message, state: FSMContext):
    #Делим сообщение пользователя на строки и заносим их в локальные переменные {login} и {password}
    LoginFromMessage = message.text.split('\n')[0]
    PasswordFromMessage = message.text.split('\n')[1]

    #Переход в директорию для импорта нашего модуля
    sys.path.insert(0, "C:/Users/user/MyProjects/MyPythonProjects/Edu Tatar/script")

    import script_login
    LoginEduTatar = script_login.loginEduTatar(LoginFromMessage, PasswordFromMessage)
    
    #Если получится зайти на сайт с такими данные для входа, то мы сообщим об этом пользователю
    if LoginEduTatar[0] == 'true':
        UserNameFromScript = LoginEduTatar[1][0]
        UserLoginFromScript = LoginEduTatar[1][1]
        await bot.send_message(message.from_user.id, f'Успешная авторизация!\nЛогин: {UserLoginFromScript}\nФИО: {UserNameFromScript}')
        print(LoginEduTatar[4])
        await state.finish()
    elif LoginEduTatar[0] == 'false':
        await bot.send_message(message.from_user.id, 'Не удалось выполнить вход!\nНеправильный Логин или пароль')
        await state.finish()
        
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)