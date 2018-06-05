import requests
from bs4 import BeautifulSoup

proxy_support = {'http': 'http://11115:7My2Ng@world.nohodo.com:6811'}

SplChar = {'!': '%21', '#': '%23', '$': '%24', '&': '%26', "'": '%27', '(': '%28', ')': '%29', '*': '%2A', '+': '%2B', ',': '%2C', '/': '%2F', ':' : '%3A', ';': '%3B', '=': '%3D',  '?': '%3F',  '@': '%40',  '[': '%5B',  ']': '%5D',  '"': '%22',  '%': '%25',  '<': '%3C',  '>': '%3E'}
dataList = []

url = "http://www.asashi.com.my/webshaper/store/searchProd.asp"
searchText="DELL+AX210+USB2.0+PORTABLE+SPEAKER"

res = requests.post(url, data= searchText, proxies= proxy_support)
soup = BeautifulSoup(res.text, "lxml")
print(soup.prettify())
SearchDiv = soup.find("table", Class_ = "searchResultsGrid")
print(SearchDiv.text)
