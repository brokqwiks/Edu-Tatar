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
    DiaryEduTatar = State()

StartKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
LoginEduTatar_Button = KeyboardButton('Войти')
StartKeyboard.add(LoginEduTatar_Button)

LoginKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
DiaryEduTatar_Button = KeyboardButton('Дневник')
CancelEduTatar_Button = KeyboardButton('Выйти')
LoginKeyboard.add(DiaryEduTatar_Button).insert(CancelEduTatar_Button)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет! Этот бот - электронный дневник EduTatar.\nЧтобы посмотреть, что умеет этот бот войди в свой аккаунт',
                           reply_markup=StartKeyboard)

@dp.message_handler(Text(equals='Войти'))
async def cmd_sing_in(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отправь свой Логин и пароль в таком формате:\n\n"Логин"\n"Пароль"')
    await ClientStatesGroup.LoginEduTatar.set()

@dp.message_handler(state=ClientStatesGroup.LoginEduTatar)
async def LoginEduTatar(message: types.Message, state: FSMContext):
    LoginFromMessage = message.text.split('\n')[0]
    PasswordFromMessge = message.text.split('\n')[1]
    
    sys.path.insert(0, 'C:/Users/user/MyProjects/MyPythonProjects/Edu Tatar/script')
    import script_login

    LoginEduTatar = script_login.loginEduTatar(LoginFromMessage, PasswordFromMessge)
    
    if LoginEduTatar[0] == 'true':
        await bot.send_message(message.from_user.id, f'Успешная авторизация!\nЛогин: {LoginEduTatar[1][1]}\nФИО: {LoginEduTatar[1][0]}',
                               reply_markup=LoginEduTatar)
        await state.finish()
        await ClientStatesGroup.DiaryEduTatar.set()

        @dp.message_handler(state=ClientStatesGroup.DiaryEduTatar)
        async def cmd_diary(message: types.Message, state: FSMContext):
            if message.text == 'Дневник':
                DiaryEduTatar = script_login.diary(LoginFromMessage, PasswordFromMessge)
                print(DiaryEduTatar[0])
                await state.finish()
            elif message.text == 'Выйти':
                await bot.send_message(message.from_user.id, 'Вы успешно вышли с аккаунта',
                                       reply_markup=StartKeyboard)
                await state.finish()
        
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)