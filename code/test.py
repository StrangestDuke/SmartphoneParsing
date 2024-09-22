import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json
import random
import concurrent.futures
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
"""
ua = fake_useragent.UserAgent()

    # Сюда хуячим селен
soup = get_stuff_automated("https://www.joom.ru/ru/search/s.origPrice.desc/q.%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B")

    # !!! Как костя мне сказал - на сайте весь прикол состоит в ложной ссылке, которая JS-у отправляет
    # сигнал, который уже и запрашивает дополнительные данные и там уже и идет подключение и другая
    # штука.

# a class="content___N4xbX"
try:
# Находятся все ссылки в блоке, после чего они все приписываются в лист. Из него
# берётся первая ссылка, что ссылат на работу, а не на компанию
    links = soup.find_all("a", href=True, attrs={"class": "content___N4xbX"})#['href']
    stuff = [x['href'] for x in links]
except Exception as e:
    print(f"{e}")
    links = []

print(stuff)
"""
"""
linky='https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true&experience=noExperience&text=Data+Analyst&page=0'
def pull_phone_specs(link, number_of_pages):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('{}'.format(link))

    enter = driver.find_elements(by=By.CLASS_NAME, value='supernova-button')
    enter[-1].click()
    time.sleep(4)
    currentElement = driver.switch_to.active_element
    currentElement.send_keys("89049930982")
    currentElement.send_keys(Keys.ENTER)
    time.sleep(30)

    driver.get('{}'.format(link))
    link = driver.current_url
    list_of_all_stuff = driver.find_elements(by=By.CLASS_NAME, value="controls-container--W4GQ8YruzOneqECRzwox")

    for i in list_of_all_stuff:
        i.find_element(by=By.TAG_NAME, value='a').click()
        if driver.current_url != link:
            print("it`s different shit")
            new_link = driver.current_url
            original_window = driver.current_window_handle
            driver.switch_to.new_window('tab')
            driver.get('{}'.format(new_link))
            driver.switch_to.window(original_window)
            driver.back()
        try:
            popout = driver.find_element(by=By.CLASS_NAME, value='bloko-modal-container_visible')
            popout = popout.find_element(by=By.TAG_NAME, value='bloko-modal')
            popout = popout.find_element(by=By.TAG_NAME, value='bloko-modal-footer')
            popout = popout.find_element(by=By.TAG_NAME, value='bloko-button_kind-success')
            popout.click()
        except:
            pass
        time.sleep(random.uniform(0.3, 0.6))

def get_number_of_pages(link):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=link,
        headers={"user-agent": ua.random}
    )
    if data.status_code != 200:
        print('Fuck')
        return
    soup = BeautifulSoup(data.content, "lxml")

    try:
        name = soup.find(attrs={"class":"bloko-gap"} ).find('div').find_all('span')[-3].text
    except:
        name =""
    return name

balls = pull_phone_specs(linky,get_number_of_pages(linky))

print(balls)

"""
"""
try:
    with open("links.json", encoding="utf-8") as f:
        links = json.load(f)
except:
    links = get_links("https://www.joom.ru/ru/search/s.origPrice.desc/q.%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B")
    with open("links.json", "w", encoding="utf-8") as f:
        json.dump(links, f, indent=4, ensure_ascii=False)


data = []
def put_products_to_work(link):
    data.append(pull_phone_specs(link))

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(pull_phone_specs, links)

with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

"""
"""

(() => {
    let delay = 0;
    const jobs = document.querySelectorAll(".vacancy-search-item__card a.vacancy-serp__vacancy_response");
    jobs.forEach(job =>{
            setTimeout(() => {
                job.click();
            }, delay)
            delay += 2000
    })

})();

"""

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)