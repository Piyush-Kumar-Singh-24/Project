import requests
from bs4 import BeautifulSoup as BS
from smtplib import SMTP
import time

URL = "https://www.amazon.in/Acer-HA270-Awmi-27-inch-Monitor/dp/B07JD7GKJP/?_encoding=UTF8&pd_rd_w=dJEUA&content-id=amzn1.sym.1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_p=1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_r=JYCJMJE383P8BCBN84ZJ&pd_rd_wg=vg6VE&pd_rd_r=22424d1e-a8a4-486e-91e0-7bd9a9f58ab8&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

def extract_price():
    page = requests.get(URL, headers=headers)
    Soup = BS(page.content, "html.parser")
    price = float(Soup.find('span',attrs ={"class":"a-price-whole"}).text.split()[0].replace(",",""))
    return price

SMTP_SERVER = "smtp.gmail.com"
port = 587
EMAIL_ID = "bls.piyush01@gmail.com"
password = "kpkiwiochzfeetnq"

def notify():
    server = SMTP(SMTP_SERVER, port)
    server.starttls()
    server.login(EMAIL_ID, password)

    subject = "Buy Now"
    body = "Price has fallen. Go buy it now!"+URL

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(EMAIL_ID, EMAIL_ID, msg)
    server.quit()

Aprice = 11000

while(True):
    time.sleep(60)
    if extract_price() <= Aprice:
        notify()

