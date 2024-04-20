
import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json
import concurrent.futures
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def get_stuff_automated(link):
    driver = webdriver.Chrome()
    driver.get('{}'.format(link))


    driver.execute_script("window.scrollTo(0, (document.body.scrollHeight/10));")
    time.sleep(1)
    stuff = driver.find_element(by=By.CLASS_NAME, value="expandButton___HYAx0")
    stuff.click()

    time.sleep(1)
    elementHTML = driver.page_source#gives exact HTML content of the element

    soup = BeautifulSoup(elementHTML,'lxml')


    chars = soup.find('div', attrs={"class":"block___dmkMj"})

    print(chars)

    #По сути - можно взять все элементы и проверять на их совпадение с именем и потом уже брать то
    # что нужно, после перебора. Звучит как план.
    try:

        os = chars.find('span', string='Операционная система').parent.parent.find('div',attrs={'class':"value___omEBd"}).find('span').get_text()
    except:
        os =""
        print("Everything is fucked")

    return os



data = get_stuff_automated("https://www.joom.ru/ru/products/63dd574ea5e8de010840476f")
print(data)
