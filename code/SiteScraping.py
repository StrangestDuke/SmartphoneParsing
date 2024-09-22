import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from site_automation import get_stuff_automated
from product_scraper import pull_phone_specs
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

def get_links(link):
    ua = fake_useragent.UserAgent()

    #Сюда тыкаем селен
    soup = get_stuff_automated(link)
    ammount_of_products = len(soup.find_all('a'))

    #!!! Как костя мне сказал - на сайте весь прикол состоит в ложной ссылке, которая JS-у отправляет
    # сигнал, который уже и запрашивает дополнительные данные и там уже и идет подключение и другая
    # штука.

    #a class="content___N4xbX"
    try:
        #Находятся все ссылки в блоке, после чего они все приписываются в лист. Из него
        #берётся первая ссылка, что ссылат на работу, а не на компанию
        links = soup.find_all("a", href=True, attrs={"class": "content___N4xbX"})
        stuff = ["https://www.joom.ru{}".format(x["href"]) for x in links]
    except Exception as e:
        print(f"{e}")
        stuff = []
    return stuff

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

for i in links:
    put_products_to_work(i)
    print(data)

with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=4,ensure_ascii=False)
