# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:13:07 2017

@author: Tech
"""

import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time
import calendar
import os
import urllib.parse
#==================Variable declaration part==================
prodURLs = []
PageNo = 0
PgNo = 1
errCode = 0
#==================code to calculate epoch time===============
def CacheCode():
    epoch = calendar.timegm(time.gmtime()) #calendar.timegm(time.strptime('Jul 9, 2009 @ 20:02:58 UTC', '%b %d, %Y @ %H:%M:%S UTC'))
    return epoch

#==================code for file writer=======================
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
#==================Category page for pagination================
proxy_support ={'https': 'https://csimonra:h19VA2xZ@173.228.169.137:29842',
    'https': 'https://csimonra:h19VA2xZ@173.228.169.148:29842'}

Mainurl = "https://www.qoo10.sg/shop/stone"
response = requests.get(Mainurl, proxies = proxy_support)
cookie1=response.cookies
print(cookie1)
soup = BeautifulSoup(response.text, "lxml")
#print(response.text)

#==================Code to get total no of Page================
Prodtext = soup.find_all("span", {"class": "num"})
for pd in Prodtext:
    ProCount = pd.text
PageNo = int(int(ProCount)/120)
if((int(ProCount) % 120) > 0):
    PageNo += 1
#=================code to get sell_coupon_cust_no===============
CustNo = soup.find("input" , {"id" :"sell_coupon_cust_no"})['value']
encCustNo = urllib.parse.quote(CustNo)
#print(CustNo)
#=================Code to disptype========================
DispType = soup.find("input" , {"id" :"dispType"})['value']
#print(DispType)
#=================Code to hit list pages========================
for PgNo in range(1,5):
    if (PgNo == 1):
        response = requests.get(Mainurl, cookies = cookie1, proxies = proxy_support)
        c1=response.cookies
        cookie1.update(c1)
        print(cookie1)
        path = 'E:/test'
        strname = os.path.join(path, 'page' + str(PgNo) + '.html')
        f = open(strname, 'w+')
        f.write(str(response.text.encode("utf-8")))
        f.close()
# =============================================================================
#         soup = BeautifulSoup(response.text, "lxml")
#         ProdDiv = soup.find_all("div", class_= "item_wrap")
#         for div in ProdDiv:
#             alink = div.find_all("a", class_= "thmb")
#             for a in alink:
#                 prodURLs.append(a["href"])
# =============================================================================
    else:
        time.sleep(2)
        epoch = CacheCode()
        strepoch = str(epoch)
        #encCustNO= encrypt(CustNo)
        #print(encCustNo)
        url = "https://www.qoo10.sg/gmkt.inc/Search/SearchResultAjaxTemplate.aspx"
        data = "minishop_bar_onoff=N&sell_coupon_cust_no=" + CustNo + "&SellerCooponDisplay=Y&sell_cust_no=" + encCustNo + "&theme_sid=0&global_yn=N&qid=0&fbidx=-1&sortType=SORT_RANK_POINT&dispType=" + DispType + "&filterDelivery=NNNNNANNNNNNNN&search_global_yn=N&shipto=ALL&is_research_yn=Y&coupon_filter_no=0&partial=on&paging_value=" + str(PgNo-1) + "&curPage=" + str(PgNo) + "&pageSize=120&ajax_search_type=M&___cache_expire___=" + str(epoch)
        print(data)
        headers = {'Accept':'*/*','Content-Type':'text/html; charset=utf-8', 'Host':'www.qoo10.sg','Origin':'https://www.qoo10.sg','Referer':Mainurl,'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        r= requests.post('https://www.qoo10.sg/gmkt.inc/Search/SearchResultAjaxTemplate.aspx', data = data, headers = headers, cookies = cookie1, proxies = proxy_support)
        c2=r.cookies
        cookie1.update(c2)
        print(cookie1)
        path = 'E:/test'
        strname = os.path.join(path, 'page' + str(PgNo) + '.html')
        f = open(strname, 'w+')
        f.write(str(r.text.encode('utf-8')))
        f.close()
    #PgNo+=1
    #print(PgNo)
# =============================================================================
#         soup = BeautifulSoup(response.text, "lxml")
#         ProdDiv = soup.find_all("div", class_= "item_wrap")
#         for div in ProdDiv:
#             alink = div.find_all("a", class_= "thmb")
#             for a in alink:
#                 prodURLs.append(a["href"])
# =============================================================================
        
