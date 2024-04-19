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

#НУЖНО НАПИСАТЬ. ЭТО ПРОСТО КОД СПИЗЖЕННЫЙ С ДРУГОЙ ЧАСТИ ПО.

"""
Цена, скидка, рейтинг, количество покупок и отзывов,
ОЗУ, ПЗУ, ДИАГОНАЛЬ, ОС, ПРОЦ, БАТАРЕЯ, КАМЕРА
"""

def get_stuff_automated(link):
    driver = webdriver.Chrome()
    driver.get('{}'.format(link))

    driver.implicitly_wait(3)

    submit_button = driver.find_element(by=By.CLASS_NAME, value="expandButton___HYAx0")
    submit_button.click()

    needed_stuff = driver.find_element(by=By.CLASS_NAME, value="block___dmkMj")
    elementHTML = driver.page_source#gives exact HTML content of the element

    soup = BeautifulSoup(elementHTML,'lxml')

    #Нужно будет брать полученные характеристики, а потом пропускать через мясорубку все значения
    # и при наличии нулов - к хуям обрубать колонку.
    try:
        name = soup.find(attrs={"h1":"root___e0mAF"} ).text
    except:
        name =""
    try:
        price = soup.find(attrs={"div":"price___Y4B7f"}).find_all(attrs={'span'})[-2].text
    except:
        price =""
    try:
        sales = soup.find(attrs={"span":"msrPriceContent___B4IAF"}).find_all('span')[-2].text
    except:
        sales=""
    try:
        stars = soup.find(attrs={"div":"rating___xgC0f"}).find(attrs={'div':'label___vyzo3'}).get_text()
    except:
        stars =""
    try:
        review_num = soup.find(attrs={"h3":"header___Awua3"}).find(attrs={'span':'count___hYdlC'}).get_text()
    except:
        review_num =""

    chars = soup.find(attrs={"div":"block___dmkMj"})

    #По сути - можно взять все элементы и проверять на их совпадение с именем и потом уже брать то
    # что нужно, после перебора. Звучит как план.

    try:
        os = chars.find(attrs={"h3":"header___Awua3"}).find(attrs={'span':'count___hYdlC'}).get_text()
    except:
        os =""
    try:
        RAM = soup.find(attrs={"h3":"header___Awua3"}).find(attrs={'span':'count___hYdlC'}).get_text()
    except:
        RAM =""
    try:
        ROM = soup.find(attrs={"h3":"header___Awua3"}).find(attrs={'span':'count___hYdlC'}).get_text()
    except:
        ROM =""
    try:
        diagonal = soup.find(attrs={"h3":"header___Awua3"}).find(attrs={'span':'count___hYdlC'}).get_text()
    except:
        diagonal =""
    try:
        processor = soup.find(attrs={"h3":"header___Awua3"}).find(attrs={'span':'count___hYdlC'}).get_text()
    except:
        processor =""
    try:
        battery = soup.find(attrs={"h3":"header___Awua3"}).find(attrs={'span':'count___hYdlC'}).get_text()
    except:
        battery =""
    try:
        camera = soup.find(attrs={"h3":"header___Awua3"}).find(attrs={'span':'count___hYdlC'}).get_text()
    except:
        camera =""



    product_main = {
        "link":link,
        "name":name,
        "price":price,
        "sales": sales,
        "stars": stars,
        "review_num": review_num,
    }
    product_chars = {
        "OS" : os,
        "RAM": RAM,
        "ROM": ROM,
        "diag": diagonal,
        "proc": processor,
        "bat": battery,
        "cam": camera
    }
    return product_main, product_chars

data = get_stuff_automated("https://www.joom.ru/ru/products/63dd574ea5e8de010840476f")
with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

