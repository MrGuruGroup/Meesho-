import requests
import sys
from bs4 import BeautifulSoup
a="https://meesho.com/women-kurtis/pl/dn6ft?page=1"
c=[]
for i in range(1,6):
    b=a+str(i)
    c.append(b)
    # print(b)
for j in c:
    
    r = requests.get(j)
    content = r.content.decode(encoding='UTF-8')
    soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")

    kurta={}
    products=[]
    prices=[]
    brand = soup.find_all('h4', {"class": "plp-card-title-desktop"})
    costs = soup.find_all('div', {"class": "plp-cost-desktop"})
    for i in brand:
        products.append(i.text)
    for j in costs:
        prices.append(j.text)
    import pandas as pd

    df = pd.DataFrame({'Product Name':products,'Prices':prices})

    df.head()
    df.to_csv('Meesho.csv')
