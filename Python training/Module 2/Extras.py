
# To get random numbers. Can be use for choosing proxies randomly
import numpy as np
import csv
import requests
from lxml import html
# np.random.seed(1)
print(np.random.randint(0, 100))


proxies = ['one', 'two']
proxiesDictionary = {'one':0, 'two':0}

for i in range(20):
        proxiesDictionary[proxies[np.random.randint(0, 2)]] += 1
print(proxiesDictionary)


#######################################################################
# Excercise
#######################################################################

# Try to build a dictionary using author names from yesterday. See how many times an author is present on the page
proxy = {"http": "http://sachin:sachin@123@seattle.wonderproxy.com:80",
         "https": "https://sachin:sachin@123@seattle.wonderproxy.com:80"}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
Author_Dict = {}
url = 'http://quotes.toscrape.com/'
r = requests.get(url, proxies=proxy, headers=headers).text
# print(r)

html = html.fromstring(r)


# Try to get the author names. You have the html variable with you.
author = html.xpath('//small[@class ="author"]/text()')
for auth in author:
        if auth in Author_Dict.keys():
                Author_Dict[auth] += 1
        else:
                Author_Dict[auth] = 1

print(Author_Dict)