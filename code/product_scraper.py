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

def get_stuff_automated(link):
    driver = webdriver.Chrome()
    driver.get('{}'.format(link))

    driver.implicitly_wait(3)

    submit_button = driver.find_element(by=By.CLASS_NAME, value="loadingContent___KuI7U")
    submit_button.click()

    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    needed_stuff = driver.find_element(by=By.CLASS_NAME, value="inner___X6KPD")
    elementHTML = needed_stuff.get_attribute('outerHTML') #gives exact HTML content of the element

    elementSoup = BeautifulSoup(elementHTML,'html.parser')
    return elementSoup