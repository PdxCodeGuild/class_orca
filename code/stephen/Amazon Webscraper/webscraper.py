'''
Amazon Webscraper!
The purpose of this program is to scrape relevant data from Amazon product urls in a csv.
Inside the csv is also a buy below threshold, which will print an alert as well as send an
email notifying the recipient that the price is now below the threshold.
There is a scheduled task in Windows that runs the script twice daily.
'''



import requests
from bs4 import BeautifulSoup
from time import sleep
import smtplib
import pandas as pd
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# defining user agent for getting access with requests module
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

# set to run once and quit, could be modified with multiple loops or on a time interval
def amazon_scraper(loops_count=1):
    # using pandas module to read csv file
    tracker = pd.read_csv('PRODUCT_TRACKER1.csv')
    tracker_urls = tracker.url
    
    loops = 0
    
    while loops < loops_count:
        # pulling urls from csv and parsing web page code to find specific tags and return them
        for x, url in enumerate(tracker_urls):
            page = requests.get(url, headers = headers)
            soup = BeautifulSoup(page.content, features='lxml')

            title = soup.find(id='productTitle').get_text().strip()
            # set up try/except to catch when a price isn't displayed so it doesn't crash
            try:
                price = float(soup.find(id='priceblock_ourprice').get_text().replace('$', '').replace(',', '').strip())
            except:
                price = ''
            # determining how much more the product currently is than what I said I'd be willing to pay
            above = price - tracker.buy_below[x]
            
            print(f'{title} -- Price: ${price:.2f} \nThis is ${above:.2f} above the buy below threshold.\n')
            loops += 1

            # prints aleret if price is below set threshold, runs the send email function
            if price <= tracker.buy_below[x]:
                print(f'\n{tracker.code[x]} is below purchase threshold of ${tracker.buy_below[x]}\n')
                send_email(tracker.code[x], tracker.buy_below[x], tracker.url[x])
                
            sleep(3)

# function to send a notification email from a throwaway gmail acct
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

    # creates secure connection through starttls and ssl
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



amazon_scraper()