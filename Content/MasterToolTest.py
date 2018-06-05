# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:08:36 2018

@author: Tech
"""
import requests
import json
import lxml.html
from bs4 import BeautifulSoup
url=[]
proxy_support ={'https': 'https://csimonra:h19VA2xZ@173.228.169.137:29842',
    'https': 'https://csimonra:h19VA2xZ@173.228.169.148:29842'}
# =============================================================================
# res = requests.get("https://www.jumia.com.eg/smart-phones/", proxies=proxy_support)
# soup = BeautifulSoup(res.text, "lxml")
# container = soup.find("section", class_="products")
# urlDiv = container.find_all("a")
# f= open("E:\\URL.text","w+")
# if urlDiv:
#     for ul in urlDiv:
#         i = ul["href"]
#         url.append(i)
#         f.write(i)
#         f.write('|')
# f.close()
# =============================================================================
u="https://www.jumia.com.eg/iphone-x-64gb-space-gray-apple-mpg54232.html"
res1 = requests.get(u, proxies=proxy_support)
pres = BeautifulSoup(res1.text, "lxml")
data = json.loads(str(pres))
print(data)
# =============================================================================
# 
# f= open("E:\\product.html","w+")
# f.write(str(pres.text.encode('utf-8')))
# f.close()
# 
# =============================================================================
#print(pres.text)


    
# =============================================================================
# for t in soup.main.children:
#     if t:
#         print(t)
#         print("==========================")
# 
# =============================================================================
