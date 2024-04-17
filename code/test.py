import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.joom.ru/ru/search/s.origPrice.desc/q.%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B')
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button___Fogz2 rounded-rect___bviwL large___rb5cP primary___Go6Zn large___rb5cP")

print(submit_button)