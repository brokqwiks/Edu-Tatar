import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

def loginEduTatar():
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
        'main_login2' : '50199002086',
        'main_password2' : 'heLCifpE'
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

    Url_UserDiaryTerm = "https://edu.tatar.ru/user/diary/term"
    responce_diaryTerm = session.get(url=Url_UserDiaryTerm)

    BS_User_Diary_Term = BeautifulSoup(responce_diaryTerm.text, 'lxml')
    test = BS_User_Diary_Term.find_all('tr')
        
    contrainer = BS_User_Diary_Term.find_all("tr")
    strOut = ""
    data_list = []
    for elem in contrainer:
        key = elem.text
        data_list.append(key)

    DataSubjectsList = data_list
    DataSubjectsList.pop(0)
    SubjectsAndRatings = []
    test1 = []
    items = []
    
    for subject in DataSubjectsList:
        a = subject.split('\n')
        if subject != '':
            items.append(a)
    
    algebra = []
    biology = []
    geografy = []
    geometry = []
    izo = []
    english = []
    informatica = []
    history = []
    litera = []
    music = []
    obs = []
    rodlitera = []
    rod = []
    rus = []
    tehnology = []
    fizika = []
    PE = []
    himiya = []

    for subject_or_rating_algebra in items[0]:  #Алгебра
        if subject_or_rating_algebra == 'Алгебра':
            algebra.append(subject_or_rating_algebra)
        elif subject_or_rating_algebra == '5' or subject_or_rating_algebra == '4' or subject_or_rating_algebra == '3' or subject_or_rating_algebra == '2' or subject_or_rating_algebra == '1':
            algebra.append(subject_or_rating_algebra)
        elif len(subject_or_rating_algebra) == 4:
            algebra.append(subject_or_rating_algebra)
                
    for subject_or_rating_geometry in items[3]:
        if subject_or_rating_geometry == 'Геометрия':
            geometry.append(subject_or_rating_geometry)
        elif subject_or_rating_geometry == '5' or subject_or_rating_geometry == '4' or subject_or_rating_geometry == '3' or subject_or_rating_geometry == '2' or subject_or_rating_geometry == '1':
            geometry.append(subject_or_rating_geometry)
        elif len(subject_or_rating_geometry) == 4:
            geometry.append(subject_or_rating_geometry)

    for subject_or_rating_biology in items[1]:
        if subject_or_rating_biology == 'Биология':
            biology.append(subject_or_rating_biology)
        elif subject_or_rating_biology == '5' or subject_or_rating_biology == '4' or subject_or_rating_biology == '3' or subject_or_rating_biology == '2' or subject_or_rating_biology == '1':
            biology.append(subject_or_rating_biology)
        elif len(subject_or_rating_biology) == 4:
            biology.append(subject_or_rating_biology)

    for subject_or_rating_geografy in items[2]:
        if subject_or_rating_geografy == 'География':
            geografy.append(subject_or_rating_geografy)
        elif subject_or_rating_geografy == '5' or subject_or_rating_geografy == '4' or subject_or_rating_geografy == '3' or subject_or_rating_geografy == '2' or subject_or_rating_geografy == '1':
            geografy.append(subject_or_rating_geografy)
        elif len(subject_or_rating_geografy) == 4:
            geografy.append(subject_or_rating_geografy)

    for subject_or_rating_izo in items[4]:
        if subject_or_rating_izo == 'Изобразительное искусство':
            izo.append(subject_or_rating_izo)
        elif subject_or_rating_izo == '5' or subject_or_rating_izo == '4' or subject_or_rating_izo == '3' or subject_or_rating_izo == '2' or subject_or_rating_izo == '1':
            izo.append(subject_or_rating_izo)
        elif len(subject_or_rating_izo) == 4:
            izo.append(subject_or_rating_izo)
    
    for subject_or_rating_english in items[5]:
        if subject_or_rating_english == 'Иностранный язык (английский)':
            english.append(subject_or_rating_english)
        elif subject_or_rating_english == '5' or subject_or_rating_english == '4' or subject_or_rating_english == '3' or subject_or_rating_english == '2' or subject_or_rating_english == '1':
            english.append(subject_or_rating_english)
        elif len(subject_or_rating_english) == 4:
            english.append(subject_or_rating_english)

    for subject_or_rating_informatica in items[6]:
        if subject_or_rating_informatica == 'Информатика':
            informatica.append(subject_or_rating_informatica)
        elif subject_or_rating_informatica == '5' or subject_or_rating_informatica == '4' or subject_or_rating_informatica == '3' or subject_or_rating_informatica == '2' or subject_or_rating_informatica == '1':
            informatica.append(subject_or_rating_informatica)
        elif len(subject_or_rating_informatica) == 4:
            informatica.append(subject_or_rating_informatica)

    for subject_or_rating_history in items[7]:
        if subject_or_rating_history == 'История':
            history.append(subject_or_rating_history)
        elif subject_or_rating_history == '5' or subject_or_rating_history == '4' or subject_or_rating_history == '3' or subject_or_rating_history == '2' or subject_or_rating_history == '1':
            history.append(subject_or_rating_history)
        elif len(subject_or_rating_history) == 4:
            history.append(subject_or_rating_history)

    for subject_or_rating_litera in items[8]:
        if subject_or_rating_litera == 'Литература':
            litera.append(subject_or_rating_litera)
        elif subject_or_rating_litera == '5' or subject_or_rating_litera == '4' or subject_or_rating_litera == '3' or subject_or_rating_litera == '2' or subject_or_rating_litera == '1':
            litera.append(subject_or_rating_litera)
        elif len(subject_or_rating_litera) == 4:
            litera.append(subject_or_rating_litera)

    for subject_or_rating_music in items[9]:
        if subject_or_rating_music == 'Музыка':
            music.append(subject_or_rating_music)
        elif subject_or_rating_music == '5' or subject_or_rating_music == '4' or subject_or_rating_music == '3' or subject_or_rating_music == '2' or subject_or_rating_music == '1':
            music.append(subject_or_rating_music)
        elif len(subject_or_rating_music) == 4:
            music.append(subject_or_rating_music)
            
    for subject_or_rating_obs in items[10]:
        if subject_or_rating_obs == 'Обществознание':
            obs.append(subject_or_rating_obs)
        elif subject_or_rating_obs == '5' or subject_or_rating_obs == '4' or subject_or_rating_obs == '3' or subject_or_rating_obs ==  '2' or subject_or_rating_obs == '1':
            obs.append(subject_or_rating_obs)    
        elif len(subject_or_rating_obs) == 4:
            obs.append(subject_or_rating_obs)

    for subject_or_rating_rodlitera in items[11]:
        if subject_or_rating_rodlitera == 'Родная литература':
            rodlitera.append(subject_or_rating_rodlitera)
        elif subject_or_rating_rodlitera == '5' or subject_or_rating_rodlitera == '4' or subject_or_rating_rodlitera == '3' or subject_or_rating_rodlitera == '2' or subject_or_rating_rodlitera == '1':
            rodlitera.append(subject_or_rating_rodlitera)
        elif len(subject_or_rating_rodlitera) == 4:
            rodlitera.append(subject_or_rating_rodlitera)

    for subject_or_rating_rod in items[12]:
        if subject_or_rating_rod == 'Родной язык':
            rod.append(subject_or_rating_rod)
        elif subject_or_rating_rod == '5' or subject_or_rating_rod == '4' or subject_or_rating_rod == '3' or subject_or_rating_rod == '2' or subject_or_rating_rod == '1':
            rod.append(subject_or_rating_rod)
        elif len(subject_or_rating_rod) == 4:
            rod.append(subject_or_rating_rod)

    for subject_or_rating_rus in items[13]:
        if subject_or_rating_rus == 'Русский язык':
            rus.append(subject_or_rating_rus)
        elif subject_or_rating_rus == '5' or subject_or_rating_rus == '4' or subject_or_rating_rus == '3' or subject_or_rating_rus == '2' or subject_or_rating_rus == '1':
            rus.append(subject_or_rating_rus)
        elif len(subject_or_rating_rus) == 4:
            rus.append(subject_or_rating_rus)

    for subject_or_rating_tehnology in items[14]:
        if subject_or_rating_tehnology == 'Технология':
            tehnology.append(subject_or_rating_tehnology)
        elif subject_or_rating_tehnology == '5' or subject_or_rating_tehnology == '4' or subject_or_rating_tehnology == '3' or subject_or_rating_tehnology == '2' or subject_or_rating_tehnology == '1':
            tehnology.append(subject_or_rating_tehnology)
        elif len(subject_or_rating_tehnology) == 4:
            tehnology.append(subject_or_rating_tehnology)

    for subject_or_rating_fizika in items[15]:
        if subject_or_rating_fizika == 'Физика':
            fizika.append(subject_or_rating_fizika)
        elif subject_or_rating_fizika == '5' or subject_or_rating_fizika == '4' or subject_or_rating_fizika == '3' or subject_or_rating_fizika == '2' or subject_or_rating_fizika == '1':
            fizika.append(subject_or_rating_fizika)
        elif len(subject_or_rating_fizika) == 4:
            fizika.append(subject_or_rating_fizika)

    for subject_or_rating_PE in items[16]:
        if subject_or_rating_PE == 'Физическая культура':
            PE.append(subject_or_rating_PE)
        elif subject_or_rating_PE == '5' or subject_or_rating_PE == '4' or subject_or_rating_PE == '3' or subject_or_rating_PE == '2' or subject_or_rating_PE == '1':
            PE.append(subject_or_rating_PE)
        elif len(subject_or_rating_PE) == 4:
            PE.append(subject_or_rating_PE)

    for subject_or_rating_himiya in items[17]:
        if subject_or_rating_himiya == 'Химия':
            himiya.append(subject_or_rating_himiya)
        elif subject_or_rating_himiya == '5' or subject_or_rating_himiya == '4' or subject_or_rating_himiya == '3' or subject_or_rating_himiya == '2' or subject_or_rating_himiya == '1':
            himiya.append(subject_or_rating_himiya)
        elif len(subject_or_rating_himiya) == 4:
            himiya.append(subject_or_rating_himiya)

    AllSubjects = [algebra, biology, geografy, geometry, izo, english, informatica, history, litera, music, obs, rodlitera, rod, rus, tehnology, fizika, PE, himiya]
    print(AllSubjects)

    return ['true', UserInfoList_FromAnceta, session, user_agent, items, AllSubjects]


    
    

loginEduTatar()
