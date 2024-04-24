from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import datetime
import pandas as pd



def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('nikagobeja2@gmail.com', 'xxxxxx')
    subject = "The Shirt you want is below rating 4.4! Now is your chance to buy!"
    body ="This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess"
    msg =f"Subject: {subject}\n\n{body}"
    server.sendmail(
    'nikagobeja2@gmail.com',
    msg
    )

def check_url():
    url ='https://www.amazon.com/Scuderia-Ferrari-Charles-Leclerc-T-Shirt/dp/B09R7XX8SH/ref=sr_1_51?sr=8-51'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
           "Accept-Encoding": "gzip, deflate", 
           "Accept": "text/html,application/xhtml+xml,application/xml;q=.0.9,*/*;q=0.8", 
           "DNT":"1","Connection":"close", 
           "Upgrade-Insecure-Requests": "1"} 
    

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')


    title = soup2.find(id='productTitle').get_text().strip()
    rating = soup2.find(class_="a-size-base a-color-base").get_text().strip()

    

    today = datetime.date.today()

    header = ['Title', 'Rating', 'Date']
    data = [title, rating, today]

# Create CSV file 
    with open('AmazonwebScraper.csv', mode='+a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    if(rating  > '4.2'):
        send_mail()

check_url()        

df = pd.read_csv(r'C:\Users\Greench Pc\Desktop\linkedIN\AmazonwebScraper.csv')
print(df)




