import os
import requests
from bs4 import BeautifulSoup

url = input("enter url of website to scrap: ")


r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.title.text)
images = soup.find_all('img')
i = 0
for image in images:
    link = image['src']
    print(str(i), link)

    with open(str(i)+'.jpg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content)

    i = i + 1
