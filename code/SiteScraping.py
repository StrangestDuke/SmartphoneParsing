import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By


"""
Функционал:

Получение максимального и минимального элемента на момент работы скрипты(если максов нет - развернуть 
скрипт)+
Нажатие на кнопку(получить больше)((Вероятно - придется делать при помощи selenium))
В максимум вниз окно уебунькивать, чтобы данные подгружались и давать ожидание одну секунду, если 
по истечению этого времени Флекс не дополнится элементами - начинаем парсить элементы
Взять ссылки на все эти приколы и сохранить отдельно.

Парсинг самоличных страниц:
....
"""

def get_links(text):
    ua = fake_useragent.UserAgent()

    data = requests.get(
        url="https://www.joom.ru/ru/search/q.%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B",
        headers={"user-agent": ua.ff}
    )

    #Нахождения диапазона цен в момент работы скрипта, для перебора между всех штук между значениями
    # которые имеются на данный момент в датабазе сайта.
    #https://www.joom.ru/ru/search/s.origPrice.desc/q.%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B С БОЛЬШОГО К МАЛЕНЬКОМУ
    #https://www.joom.ru/ru/search/s.origPrice.asc/q.%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B С МАЛЕНЬКОГО К БОЛЬШОМУ

    data_lowest = requests.get(
        url="https://www.joom.ru/ru/search/s.origPrice.asc/q.%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B",
        headers={"user-agent": ua.ff}
    )
    data_highest = requests.get(
        url="https://www.joom.ru/ru/search/s.origPrice.desc/q.%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B",
        headers={"user-agent": ua.ff}
    )

    soup = BeautifulSoup(data.content, 'lxml')
    soup_max = BeautifulSoup(data_highest.content,'lxml')
    soup_low = BeautifulSoup(data_lowest.content,'lxml')

    try:
        max_price = int(soup.find("div", attrs={"class":"price___Vlu0y"}).find_all("span", recursive=False)[-2].find("a").text)
        smallest_price = int(soup.find("div", attrs={"class":"price___Vlu0y"}).find_all("span", recursive=False)[-2].find("a").text)
    except:
        max_price = 0
        smallest_price = 0


    #Сюда хуячим селен

    driver = webdriver.Chrome()
    driver.get('https://www.joom.ru/ru/search/s.origPrice.desc/q.%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B')
    submit = driver.find_element("input#kc-login")
    submit.click()
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button___Fogz2.rounded-rect___bviwL.large___rb5cP.primary___Go6Zn")

    #!!! Как костя мне сказал - на сайте весь прикол состоит в ложной ссылке, которая JS-у отправляет
    # сигнал, который уже и запрашивает дополнительные данные и там уже и идет подключение и другая
    # штука.



    driver.implicitly_wait(0.5)
    time.sleep(3)
    activate_btn = driver.find_element_by_xpath(activate_xpath)

    driver.quit()

for page in range():
        try:
            data = requests.get(
                url="https://krasnoyarsk.hh.ru/search/vacancy?L_save_area=true&text={text}&excluded_text=&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&page={page}",
                headers={"user-agent": ua.random}
            )
            if data.status_code == 200:
                soup = BeautifulSoup(data.content, "lxml")
                for i in soup.find("div", attrs={"data-qa":"vacancy-serp__results"}).find_all("div", attrs={"class":"serp-item"}):
                    #Находятся все ссылки в блоке, после чего они все приписываются в лист. Из него
                    #берётся первая ссылка, что ссылат на работу, а не на компанию
                    yield f'{i.find_all("a", "bloko-link")[0].attrs["href"].split("?")[0]}'
        except Exception as e:
            print(f"{e}")
        time.sleep(0.1)
    print(page_count)


def get_resume(link):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=link,
        headers={"user-agent": ua.random}
    )
    if data.status_code != 200:
        return
    soup = BeautifulSoup(data.content, "lxml")

    #Название вакансии+, описание вакансии+, зп+, регион+, работодатель+
    #Требования, опыт работы+, график работы ,

    try:
        name = soup.find(attrs={"data-qa":"vacancy-title"} ).text
    except:
        name =""
    try:
        about = soup.find(attrs={"class":"g-user-content"}).p.text
    except:
        about = ""
    try:
        salary = soup.find(attrs={"data-qa":"vacancy-salary-compensation-type-net"}).text.replace("\u2009","").replace("\xa0", " ")
    except:
        salary =""
    try:
        region = soup.find(attrs={"data-qa":"vacancy-view-location"}).text
    except:
        region = ""
    try:
        company = soup.find(attrs={"data-qa":"vacancy-company-name"}).find("span").text
    except:
        company = ""
    try:
        exp = soup.find(attrs={"data-qa":"vacancy-experience"}).text.replace("\u2009","").replace("\xa0", " ")
    except:
        exp = ""
    try:
        emp_mode = soup.find(attrs={"data-qa":"vacancy-view-employment-mode"}).text
    except:
        emp_mode = ""
    resume = {
        "link":link,
        "name":name,
        "salary":salary,
        "about": about,
        "region": region,
        "company": company,
        "exp": exp,
        "emp_mode":emp_mode,
    }
    return resume

links = get_links("BI-analytic")
data = []
def put_resume_to_work(link):
    data.append(get_resume(link))

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(put_resume_to_work, links)


with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

