import requests
from bs4 import BeautifulSoup
import selenium

def loginEduTatar(LoginFromMessage, PasswordFromMessage):
    #Вход на сайт Edu Tatar
    UrlLogin_EduTatar = "https://edu.tatar.ru/logon"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    session = requests.Session()
    responce = session.get(UrlLogin_EduTatar, headers={
        'User-Agent' : user_agent
    })
    session.headers.update({'Referer':UrlLogin_EduTatar})
    session.headers.update({'User-Agent':user_agent})

    #Получаем данные для входа от пользователя
    data = {
        'main_login2' : LoginFromMessage,
        'main_password2' : PasswordFromMessage
    }
    #Делаем пост запрос на сайт
    post_requests = session.post(UrlLogin_EduTatar,
                                 data)

    #Сработает исключение при неправильных данных
    try:
        #Получаем информацию(Имя, логин, должность) с сайта после успешной авторизации
        BS_User_Anceta = BeautifulSoup(post_requests.text, "lxml")
        UserInfoFromAnceta = BS_User_Anceta.find_all('td')
        UserNameFromAnceta = UserInfoFromAnceta[1].text
        UserLoginFromAnceta = UserInfoFromAnceta[3].text
        UserJobFromAnceta = UserInfoFromAnceta[5].text
        UserInfoList_FromAnceta = [UserNameFromAnceta, UserLoginFromAnceta, UserJobFromAnceta]
        return ['true', UserInfoList_FromAnceta, session, user_agent]
    except:
        return ['false']
    
