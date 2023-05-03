import requests
from bs4 import BeautifulSoup

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
    
        #Получаем информацию(Имя, логин, должность) с сайта после успешной авторизации
    BS_User_Anceta = BeautifulSoup(post_requests.text, "lxml")
    UserInfoFromAnceta = BS_User_Anceta.find_all('td')
    UserNameFromAnceta = UserInfoFromAnceta[1].text
    UserLoginFromAnceta = UserInfoFromAnceta[3].text
    UserJobFromAnceta = UserInfoFromAnceta[5].text
    UserInfoList_FromAnceta = [UserNameFromAnceta, UserLoginFromAnceta, UserJobFromAnceta]



        
    return ['true', UserInfoList_FromAnceta, session, user_agent,  LoginFromMessage, PasswordFromMessage]

def diary(LoginFromMessage, PasswordFromMessage):
    LoginEduTatar = loginEduTatar(LoginFromMessage, PasswordFromMessage)
    session = LoginEduTatar[2]
    Url_UserDiaryTerm = "https://edu.tatar.ru/user/diary/term"
    responce_diaryTerm = session.get(url=Url_UserDiaryTerm)

    BS_User_Diary_Term = BeautifulSoup(responce_diaryTerm.text, 'lxml')

    #обрабатываю html страницу    
    contrainer = BS_User_Diary_Term.find_all("tr")
    strOut = ""
    data_list = []
    for elem in contrainer:
        key = elem.text
        data_list.append(key)

    #не обработанные оценки и предметы в списке
    DataSubjectsList = data_list
    DataSubjectsList.pop(0)
    SubjectsAndRatings_List = []
    SubjectsAndRatings_Dict = {}
    Ratings = []
    test1 = []
    items = []
    
    #обработка
    for subject in DataSubjectsList:
        a = subject.split('\n')
        if subject != '':
            items.append(a)
    
    #Добавляем название предмета и оценки [[name, ''] [name, '']]
    for subject in items:
        SubjectsAndRatings_List.append([subject[1]])
        nameSubject = subject[1]
        for rating in subject:
            if len(rating) == 1 or len(rating) == 4:
                for i in SubjectsAndRatings_List:
                    for name in i:
                        if nameSubject == name:
                            i.append(rating)

    generalAllSubjectList = len(SubjectsAndRatings_List) - 1
    generalAllSubject = items[generalAllSubjectList][0].split('ИТОГО')[1]
    SubjectsAndRatings_List.append([generalAllSubject])

    r = requests.post(url=Url_UserDiaryTerm, headers={'Connection':'close'})

    return [SubjectsAndRatings_List]

