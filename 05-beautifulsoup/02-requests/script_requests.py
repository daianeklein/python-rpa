import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.gabrielcasemiro.com.br")

if page.status_code == 200:
    print(page.text)
else:
    print('Http error: ', page.status_code)

soup = BeautifulSoup(page.text)

