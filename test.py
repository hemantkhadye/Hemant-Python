# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 15:37:32 2017

@author: Tech
"""
import urllib.request
import requests
import urllib.parse
import os
import time
from bs4 import BeautifulSoup
import xlsxwriter

#--------code to calculate epoch time------------------------
def CacheCode():
    date_time = '30.11.2017 11:05:02'
    pattern = '%d.%m.%Y %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))
    return epoch

#------------code for file writer---------------------------------
def FileWrite(prodURLs):
    workbook = xlsxwriter.Workbook('ProductURL.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1','URL','bold')
    row = 1
    col = 0
    for prod in prodURLs:
        worksheet.write(row,col,prod)
        row+=1
    workbook.close()
#-------------------Category page for pagination-------------------
proxy_support = urllib.request.ProxyHandler({
        'http': 'https://csimonra:h19VA2xZ@173.228.169.137:29842',
        'https': 'https://csimonra:h19VA2xZ@173.228.169.148:29842'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
url = "https://www.qoo10.sg/gmkt.inc/Category/Default.aspx?gdlc_cd=100000001&gdmc_cd=200000001&gdsc_cd=300000001"
response = urllib.request.urlopen(url).read().decode('utf-8')
# print(response)
# scrapIt(response)


# def scrapIt(resopnse):
soup = BeautifulSoup(response, "lxml")
# variables

#------------Code to get total no of Page---------------------------
PageNo = 0
PgNo = 1
# code to extract total Product no
Prodtext = soup.find_all("ul", {"id": "category_result_list"})
for pd in Prodtext:
    span = pd.find_all("span")
    for sp in span:
        ProCount = sp.text
        ProCount = ProCount.replace("(", "")
        ProCount = ProCount.replace(")", "")
        ProCount = ProCount.replace(",", "")

# Code to get page no
PageNo = int(int(ProCount)/120)
# print(PageNo)
if((int(ProCount) % 120) > 0):
    PageNo += 1
# print(PageNo)
# print(ProCount)

#-------------------code to hit List Pages--------------------------
prodURLs = []
for PgNo in range(2,5):
    
    # code to hitlist pages and get product data
    
#    print(soup.prettify())           
#    print(PgNo)
    if (PgNo == 1):
        proxy_support = urllib.request.ProxyHandler({
        'http': 'https://csimonra:h19VA2xZ@173.228.169.137:29842',
        'https': 'https://csimonra:h19VA2xZ@173.228.169.148:29842'})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        response = urllib.request.urlopen(url).read().decode('utf-8')
        path = 'E:/test'
        strname = os.path.join(path, 'page' + str(PgNo) + '.html')
        f = open(strname, 'w+')
        f.write(str(response.encode("utf-8")))
        # def scrapIt(resopnse):
        soup = BeautifulSoup(response, "lxml")
    else:
        epoch = CacheCode()
        strepoch = str(epoch)
        pos = url.index("?", 0, len(url))
        data = url[pos:]
        data = data.replace("?","{'")
        data = data.replace("=","':'")
        data = data.replace("&",",'")
        data = data + "',"
#        print(data)
        posturl="https://www.qoo10.sg/gmkt.inc/Category/Default.aspx"
        data = data + "'keywordArrLength' : '1','is_img_search_yn':'N','sortType': 'SORT_RANK_POINT','dispType' : 'UIG5','filterDelivery' : 'NNNNNANNNN','is_research_yn' : 'Y','coupon_filter_no' : 0,'partial' : 'on','curPage' : '" + str(PgNo) + "','pageSize' : '120','ajax_search_type' : 'C','cache_expire' : '" + strepoch + "'}"
        print(data)
        postdata = urllib.parse.urlencode(data)
        req = urllib.request.Request(url, data)
        proxy_support = urllib.reques.ProxyHandler({
        'http': 'https://csimonra:h19VA2xZ@173.228.169.137:29842',
        'https': 'https://csimonra:h19VA2xZ@173.228.169.148:29842'})
        opener = urllib.reques.build_opener(proxy_support)
        urllib.reques.install_opener(opener)
        response =  urllib.request.urlopen(req)
        # response = urllib.request.urlopen(posturl).read().decode('utf-8')
        path = 'E:/test'
        strname = os.path.join(path, 'page' + str(PgNo) + '.html')
        f = open(strname, 'w+')
        f.write(str(response.encode("utf-8")))
        # def scrapIt(resopnse):
        soup = BeautifulSoup(response, "lxml")
        
    if(PgNo == 1):
        ProdDiv = soup.find_all("div", class_= "item_wrap")
        for div in ProdDiv:
            alink = div.find_all("a", class_= "thmb")
            for a in alink:
                prodURLs.append(a["href"])
#                print(a["href"])
    else:
#        print("Page" + str(PgNo) + "URLs")
        ProdDiv = soup.find_all("div", class_= "sbj")
        for div in ProdDiv:
            alink = div.find_all("a")
            for a in alink:
                prodURLs.append(a["href"])
#                print(a["href"])
     
print(prodURLs.count)
#FileWrite(prodURLs)           
#---------------------Hit Product Page------------------------

# strname=os.path.join(path,'home.html')
# f=open(strname,'w+')
# f.write(str(response))
#URLcount = prodURLs.count
#print(URLcount)
#j=1
#for j in range(1,URLcount):
#    print(j)

