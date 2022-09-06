import os
from bs4 import BeautifulSoup
import re
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
executable_path = os.path.join(os.getcwd(), 'chromedriver', 'chromedriver.exe')
browser = webdriver.Chrome(options=options, service=Service(executable_path=executable_path))
url = 'https://spb.hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=python+junior&no_magic=true&L_save_area=true&items_on_page=50'


def get_vacancy():
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    blocks = soup.find_all('div', class_=re.compile('vacancy-serp-item__layout'))
    block = blocks[0].find_all('a', class_=re.compile('bloko-link'))
    for href in block:
        href.get('href')
        return href