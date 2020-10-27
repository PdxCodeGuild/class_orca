import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

trackNtemp = []
tracks = 0
actual_track = 0
artist = input('drop ur artist here: ')
url = (f'https://soundcloud.com/{artist}/tracks')

# op = Options()
# op.add_argument('--headless')
driver = webdriver.Chrome()
driver.get(url)

def saver():
    with open(f'{artist}.txt', mode='w', encoding='utf-8') as f:
        f.write(BeautifulSoup(driver.page_source, 'html.parser').prettify())
        f.close()

def opener(trackNtemp):
    with open(f'{artist}.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            if 'infoStats__statLink sc-link-light' in line:
                trackNtemp = line.strip()
                trackNtemp = trackNtemp.split('"')
                trackNtemp.pop()
        trackN_ = trackNtemp[-1]
        Totaltrack = trackN_.split(' ')[0]
        f.close()
    return Totaltrack

def trackCheck():
    with open(f'{artist}.txt', mode='r', encoding='utf-8') as f:
        soundlist = '<li class="soundList__item">'
        x = 0
        for line in f:
            if '<li class="soundList__item">' in line:
                x += 1
    return x
def SCROLLER():
    elem.send_keys(Keys.PAGE_DOWN)

elem = driver.find_element_by_tag_name('body')
time.sleep(1)
SCROLLER()
time.sleep(1)
saver()

tracks = opener(trackNtemp)
tracks = int(tracks)
actual_track = trackCheck()
print(f'{artist} has {tracks} tracks. may take a bit.')

time_start = time.time()

while actual_track != tracks:
    SCROLLER()
    saver()
    if tracks < 99 and (time.time()-time_start) > 33:
        print("uh, takin longer than it should. stoppin' it")
        break
    actual_track = trackCheck()
    
if actual_track != tracks:
    print('some issues with matching track numbers. probably some hidden/deleted stuff.')
else:
    # print(f'bout {round(time.time()-time_start)} seconds to finish')
    print('done here')

time.sleep(1)

print(f"savin' track names to {artist}_tracks.txt")

with open(f'{artist}_tracks.txt', mode='w', encoding='utf-8') as f:
    with open(f'{artist}.txt', mode='r', encoding='utf-8') as g:
        for line in g:
            if '<span class="">' in line:
                x = next(g).strip()
                f.write(f'{x}\n')
        g.close()
    f.close()