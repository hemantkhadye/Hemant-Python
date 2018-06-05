import requests
from lxml import html

proxy_support = {'https': 'https://11115:7My2Ng@world.nohodo.com:6811'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
url = "https://www.mscdirect.co.uk/CGI/INSRCH?N=2014234"
res = requests.get(url, proxies=proxy_support, headers = headers)
print(res.text)
html = html.fromstring(res.text)
ProdURL = html.xpath('//a[@class="linkitempromo"]/@href')
print(ProdURL)
