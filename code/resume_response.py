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

link = "https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true&experience=noExperience&text=Data+Analyst&page=0"

def pull_phone_specs(link):
    driver = webdriver.Chrome()
    driver.get('{}'.format(link))

    stuff = driver.find_elements(by=By.CLASS_NAME, value="vacancy-serp_vacancy_response_xs")
    stuff.click()

    time.sleep(0.5)
    while:
        try:
            stuff = driver.find_element(by=By.CLASS_NAME, value="vacancy-serp_vacancy_response_xs")
            stuff.click()
        except:
            print("bruh")
        driver.navigate().back();
    time.sleep(1)
    elementHTML = driver.page_source  # gives exact HTML content of the element

    soup = BeautifulSoup(elementHTML, 'lxml')
    chars = soup.find('div', attrs={"class": "block___dmkMj"})

    #Нужно будет брать полученные характеристики, а потом пропускать через мясорубку все значения
    # и при наличии нулов - к хуям обрубать колонку.
    try:
        name = soup.find('h1',attrs={"class":"root___e0mAF"} ).text
    except:
        name =""
    try:
        price = soup.find('div',attrs={"class":"price___Y4B7f"}).find_all('span')[-2].get_text()
    except:
        price =""
    try:
        sales = soup.find_all('div', attrs={'style': 'color: var(--color-primary60, #8e90a7);'})[0].find('div').get_text()
    except:
        sales=""
    try:
        stars = soup.find('div',attrs={'class':'label___vyzo3'}).get_text()
    except:
        stars =""
    try:
        perc_of_recs = soup.find_all('div', attrs={'style': 'color: var(--color-primary60, #8e90a7);'})[1].find('div').get_text()
    except:
        perc_of_recs = ""
    try:
        review_num = soup.find('h3', attrs={"class":"header___Awua3"}).find('span', attrs={'class':'count___hYdlC'}).get_text()
    except:
        review_num =""

    #По сути - можно взять все элементы и проверять на их совпадение с именем и потом уже брать то
    # что нужно, после перебора. Звучит как план.

    try:

        os = chars.find('span', string='Операционная система').parent.parent.find('div', attrs={
            'class': "value___omEBd"}).find('span').get_text()
    except:
        os = ""
    try:
        RAM = chars.find('span', string='Оперативная память').parent.parent.find('div', attrs={
            'class': "value___omEBd"}).find('span').get_text()
    except:
        RAM =""
    try:
        ROM = chars.find('span', string='Встроенная память').parent.parent.find('div', attrs={
            'class': "value___omEBd"}).find('span').get_text()
    except:
        ROM =""
    try:
        diagonal = chars.find('span', string='Диагональ').parent.parent.find('div', attrs={
            'class': "value___omEBd"}).find('span').get_text()
    except:
        diagonal =""
    try:
        battery = chars.find('span', string='Ёмкость аккумулятора').parent.parent.find('div', attrs={
            'class': "value___omEBd"}).find('span').get_text()
    except:
        battery =""
    try:
        camera = chars.find('span', string='Основная широкоугольная камера').parent.parent.find('div', attrs={
            'class': "value___omEBd"}).find('span').get_text()
    except:
        camera =""



    product_main = {
        "link":link,
        "name":name,
        "price":price,
        "sales": sales,
        "stars": stars,
        "rec_proc": perc_of_recs,
        "review_num": review_num,
    }
    product_chars = {
        "OS" : os,
        "RAM": RAM,
        "ROM": ROM,
        "diag": diagonal,
        "bat": battery,
        "cam": camera
    }
    return product_main, product_chars

