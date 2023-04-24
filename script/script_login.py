import requests
from bs4 import BeautifulSoup
import selenium

def login(login, password):
    #Вход на сайт Edu Tatar
    url_login = "https://edu.tatar.ru/logon"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    session = requests.Session()
    r = session.get(url_login, headers={
        'User-Agent' : user_agent
    })
    session.headers.update({'Referer':url_login})
    session.headers.update({'User-Agent':user_agent})

    #Получаем данные для входа от пользователя
    data = {
        'main_login2' : login,
        'main_password2' : password
    }
    #Делаем пост запрос на сайт
    post_requests = session.post(url_login,
                                 data)

    #Сработает исключение при неправильных данных
    try:
        #Получаем информацию(Имя, логин, должность) с сайта после успешной авторизации
        bs_responce = BeautifulSoup(post_requests.text, "lxml")
        info_table = bs_responce.find_all('td')
        user_name = info_table[1].text
        user_login = info_table[3].text
        user_job = info_table[5].text
        user_info = [user_name, user_login, user_job]
        return ['true', user_info, session, user_agent]
    except:
        return ['false']
    
