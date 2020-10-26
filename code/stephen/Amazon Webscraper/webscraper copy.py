'''
Amazon Webscraper!
The purpose of this program is to scrape relevant data from amazon product urls in a csv.
Inside the csv is also a buy below threshold, which will print an alert as well as send an
email notifying the recipient that the price is now below the threshold.
There is a scheduled task in Windows that runs the script twice daily.'''



import requests
from bs4 import BeautifulSoup
from time import sleep
import smtplib
import pandas as pd
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

def amazon_scraper(loops_count=1):
    tracker = pd.read_csv('PRODUCT_TRACKER.csv')
    tracker_urls = tracker.url
    loops = 0
    while loops < loops_count:
        
        for x, url in enumerate(tracker_urls):
            page = requests.get(url, headers = headers)
            soup = BeautifulSoup(page.content, features='lxml')

            title = soup.find(id='productTitle').get_text().strip()
            try:
                price = float(soup.find(id='priceblock_ourprice').get_text().replace('$', '').replace(',', '').strip())
            except:
                price = ''
            above = price - tracker.buy_below[x]
            print(f'{title} -- Price: ${price:.2f} \nThis is ${above:.2f} above the buy below threshold.\n')
            loops += 1

            if price <= tracker.buy_below[x]:
                print(f'\n{tracker.code[x]} is below purchase threshold of ${tracker.buy_below[x]}\n')
                send_email(tracker.code[x], tracker.buy_below[x], tracker.url[x])
                
            # sleep(5)

def send_email(item, threshold, url):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "awstest82@gmail.com"
    receiver_email = "mossy82nd@gmail.com"
    password = 'GateRust82'
    message = f"""
Subject: DEAL ALERT

{item} is below purchase threshold of ${threshold}!
You can purchase it at: {url})"""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



amazon_scraper()