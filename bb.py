from bs4 import BeautifulSoup as bs
from sys import argv
from datetime import datetime
from time import sleep
import requests, os

uri = argv[1]
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
headers = { 'User-Agent' : user_agent }

def check_button():
    r = requests.get(uri, headers=headers)
    soup = bs(r.content, 'html.parser')
    cart = soup.find('div', class_='fulfillment-add-to-cart-button')
    cart_button = cart.find('button')
    return cart_button.get_text()

try:
    while True:
        print("[{}] Checking... ".format(datetime.now().time()), end="")
        status = check_button()
        if status != "Sold Out":
            print("Available!!")
            while True:
                print('\a')
                sleep(1)
        print(status)
        sleep(10)
except KeyboardInterrupt:
    os.system("echo {} | clip".format(uri))
