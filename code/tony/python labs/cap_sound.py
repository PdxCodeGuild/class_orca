import requests

from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.keys import Keys
import time

from bs4 import BeautifulSoup

x = 0
trackNtemp = []
TotalTrackN = []
artist = input('drop ur artist here: ')
url = (f'https://soundcloud.com/{artist}/tracks')

driver = webdriver.Chrome()
driver.get(url)

def pagepull(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def saver(soup):
    with open('sound.txt', mode='w', encoding='utf-8') as f:
        f.write(soup.prettify())
        f.close()

def opener(x):
    soundlist = 'li class="soundlist__item"'
    with open('sound.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            if 'itemprop="track"' in line:
                x += 1
            if 'Tracks.' in line:
                trackNtemp = line
                trackNtemp = trackNtemp.split('.')
        for y in list(trackNtemp):
            if y.endswith('Tracks'):
                trackN = y.strip()
        trackN = trackN.split(' ')
    return x

# soup = pagepull(url)
# saver(soup)

# x = opener(x)
elem = driver.find_element_by_tag_name('body')
for z in range(5):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
nupage = driver.page_source
soup1 = BeautifulSoup(nupage, 'html.parser')
saver(soup1)