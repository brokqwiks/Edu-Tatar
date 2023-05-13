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

#Создаем клавиатуры
StartKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
LoginEduTatar_Button = KeyboardButton('Войти')
StartKeyboard.add(LoginEduTatar_Button)

LoginKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
DiaryEduTatar_Button = KeyboardButton('Дневник')
CancelEduTatar_Button = KeyboardButton('Выйти')
LoginKeyboard.add(DiaryEduTatar_Button).insert(CancelEduTatar_Button)

#Команда start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет! Этот бот - электронный дневник EduTatar.\nЧтобы посмотреть, что умеет этот бот войди в свой аккаунт',
                           reply_markup=StartKeyboard)

#Команада Войти
@dp.message_handler(Text(equals='Войти'))
async def cmd_sing_in(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отправь свой Логин и пароль в таком формате:\n\n"Логин"\n"Пароль"')
    await ClientStatesGroup.LoginEduTatar.set()

@dp.message_handler(state= ClientStatesGroup.LoginEduTatar)
async def login_edutatar(message: types.Message, state: FSMContext):
    user_info = message.text.split("\n")
    #Проверка сообщения на наличии две строки
    if len(user_info) == 2:
        
        #Получаем Логин и Пароль для входа на сайт от пользователя
        loginFromMessage = message.text.split("\n")[0]
        passwordFromMessage = message.text.split("\n")[1]

        #Импорт функции парсера
        sys.path.insert(0, "C:/Users/user/MyProjects/MyPythonProjects/Edu Tatar/script")
        import script_login

        #Получаем ответ от парсера
        responce = script_login.loginEduTatar(loginFromMessage, passwordFromMessage)

        #Проверка ответа на true и false
        if responce[0] == 'true':

            #Вывод сообщения об успешной авторизации и данными аккаунта
            await bot.send_message(message.from_user.id, f"Успешная авторизация!\nЛогин: {responce[1][0]}\nФИО: {responce[1][0]}")

            #Массив с оценками от парсера
            subjects = responce[4]

            #Удаляем ненужными массивы в массиве
            subjects.pop(len(subjects) - 1)
            subjects.pop(len(subjects) - 1)

            #Выводим оценки пользователя таким образом: <Имя предмета>: <Оценки>, <Средний балл>
            for items in subjects:
                grades = ' '.join(items[1:-1])
                await bot.send_message(message.from_user.id, f'{items[0]}: {grades}, {items[-1]}')
            await bot.send_message(message.from_user.id, "Все оценки были выведены\nВыполнен автоматический выход с аккаунта!")
            await state.finish()
            
        elif responce[0] == 'false':
            await bot.send_message(message.from_user.id, "Упс! Не удалось выполнить вход по указанным данным.\nПроверьте правильность написания Логина и Пароля")
            await state.finish()

    elif len(user_info) != 2:
        await bot.send_message(message.from_user.id, "Упс! Не удалось выполнить вход по указанным данным.\nПроверьте правильность написания Логина и Пароля")
        await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)