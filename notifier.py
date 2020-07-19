import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/gp/product/B07NDF3ZGQ/ref=ox_sc_saved_title_4?smid=A9OB8DNMN7HBF&psc=1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}


def check_availability():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    avail_content = soup.find(id="availability").get_text()
    in_stock = avail_content.strip()

    comp_string = 'In Stock'

    # If the product is 'In Stock', send an email
    if in_stock.find(comp_string) != -1:
        print("Found!")
        send_email()

    else:
        print("Not Found!")


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hazedrops1206@gmail.com', 'MY_PASSWORD')

    subject = 'The product is back in stock again!'
    body = 'Check the amazon link https://www.amazon.com/gp/product/B07NDF3ZGQ/ref=ox_sc_saved_title_4?smid=A9OB8DNMN7HBF&psc=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'hazedrops1206@gmail.com',
        'hazedrops@hotmail.com',
        msg
    )

    print('Hey Email Has Been Sent!')

    server.quit()


while(True):
    check_availability()
    time.sleep(60 * 60 * 24 * 3)  # Check the availability in every 3 days
