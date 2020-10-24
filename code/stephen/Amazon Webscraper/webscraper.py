import requests
from bs4 import BeautifulSoup
import smtplib


def price_check(url, buy_below):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'lxml')
    try:
        title = soup.find(id='productTitle').get_text().strip()
    except AttributeError:
        print('not working!')
    try:
        price = soup.find(id="priceblock_ourprice").get_text()[1:].strip().replace(',','')
    except AttributeError:
        print('not working!')
    convprice = float(price)
    if convprice > buy_below:
        print('Buy this!!!')
    print(title, convprice)

price_check('https://www.amazon.com/dp/B0887C9XWF/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B0887C9XWF&pd_rd_w=iMKJA&pf_rd_p=7d37a48b-2b1a-4373-8c1a-bdcc5da66be9&pd_rd_wg=Px8Sm&pf_rd_r=XX6TMS82NKJXAF1FBGRF&pd_rd_r=95485425-5451-47bb-a43d-5ba2a9f05058&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNVBFU1JQSFBUQlMxJmVuY3J5cHRlZElkPUEwNzc2MjkxMVYyNE9MWlIxUkY3UiZlbmNyeXB0ZWRBZElkPUEwNTkzMTU3RkFESkhKN0dBTlUxJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==', 100)