from lxml import html
import requests
import csv


proxy = {"http": "http://sachin:sachin@123@seattle.wonderproxy.com:80",
         "https": "https://sachin:sachin@123@seattle.wonderproxy.com:80"}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

#url = 'http://quotes.toscrape.com/'
url = "https://www.mscdirect.co.uk/CGI/INSRCH?N=2014234"

r = requests.get(url, proxies = proxy, headers= headers).text
print(r)

html = html.fromstring(r)
quotes = html.xpath('//span[@class = "text"]/text()')

# Print first 5 quotes
print(quotes[0:5])

# Try to get the author names. You have the html variable with you.
author = html.xpath('//small[@class ="author"]/text()')

with open("Training.csv", 'a', newline="") as outfile:
    writer = csv.writer(outfile)


for i in range(0, len(quotes)):
    writer.write(quotes[i], author[i])
    print(quotes[i])
    print(author[i])
