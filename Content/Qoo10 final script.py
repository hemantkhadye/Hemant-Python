# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:43:48 2017

@author: Tech
"""
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time
import calendar
import os

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
proxy_support ={'https': 'https://csimonra:h19VA2xZ@173.246.181.89:29842',
                'https': 'https://csimonra:h19VA2xZ@208.110.59.137:29842',
                'https': 'https://csimonra:h19VA2xZ@208.110.59.208:29842',
                'https': 'https://csimonra:h19VA2xZ@217.182.223.112:29842',
                'https': 'https://csimonra:h19VA2xZ@217.182.223.118:29842',
                'https': 'https://csimonra:h19VA2xZ@217.182.223.126:29842',
                'https': 'https://csimonra:h19VA2xZ@173.228.169.148:29842'}

url = "https://www.qoo10.sg/gmkt.inc/Category/Default.aspx?gdlc_cd=100000001&gdmc_cd=200000001&gdsc_cd=300000001"
response = requests.get(url, proxies = proxy_support)
soup = BeautifulSoup(response.text, "lxml")
#==================Code to get total no of Page================
Prodtext = soup.find_all("ul", {"id": "category_result_list"})
for pd in Prodtext:
    span = pd.find_all("span")
    for sp in span:
        ProCount = sp.text
        ProCount = ProCount.replace("(", "")
        ProCount = ProCount.replace(")", "")
        ProCount = ProCount.replace(",", "")
PageNo = int(int(ProCount)/120)
if((int(ProCount) % 120) > 0):
    PageNo += 1
#=================Code to hit list pages========================
for PgNo in range(2,5):
    if (PgNo == 1):
        response = requests.get(url)
        path = 'E:/test'
        strname = os.path.join(path, 'page' + str(PgNo) + '.html')
        f = open(strname, 'w+')
        f.write(str(response.text.encode("utf-8")))
        f.close()
        soup = BeautifulSoup(response.text, "lxml")
    else:
        epoch = CacheCode()
        strepoch = str(epoch)
        pos = url.index("?", 0, len(url))
        data = url[pos:]
        data = data.replace("?","{'")
        data = data.replace("=","':'")
        data = data.replace("&",",'")
        data = data + "'keywordArrLength' : '1','is_img_search_yn':'N','sortType': 'SORT_RANK_POINT','dispType' : 'UIG5','filterDelivery' : 'NNNNNANNNN','is_research_yn' : 'Y','coupon_filter_no' : 0,'partial' : 'on','curPage' : '" + str(PgNo) + "','pageSize' : '120','ajax_search_type' : 'C','___cache_expire___' : '" + strepoch + "'}"
        headers = {'Accept':'*/*','Content-Type':'text/html; charset=utf-8', 'Host':'www.qoo10.sg','Origin':'https://www.qoo10.sg','Referer':'https://www.qoo10.sg/gmkt.inc/Category/Default.aspx?gdlc_cd=100000001&gdmc_cd=200000001&gdsc_cd=300000001&keywordArrLength=1&brand_keyword=&keyword_hist=&keyword=&within_keyword_auto_change=&image_search_rdo=U&attachFile=&search_image_url=&search_image_nm=&search_keyword=&is_img_search_yn=N&sortType=SORT_RANK_POINT&dispType=UIG5&flt_pri_idx=&filterDelivery=NNNNNANNNN&search_global_yn=&basis=&shipFromNation=&shipto=&brandnm=&SearchNationCode=&is_research_yn=Y&hid_keyword=&quick_delivery_yn=&video_goods_yn=&coupon_filter_no=&gd_type=&drugs_type=&priceMin=&priceMax=&category_specific_kw_nos=&curPage=1&pageSize=120&partial=on&brandno=','User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        r= requests.post('https://www.qoo10.sg/gmkt.inc/Search/SearchResultAjaxTemplate.aspx', data = data, headers = headers, proxies = proxy_support)
        path = 'E:/test'
        strname = os.path.join(path, 'page' + str(PgNo) + '.html')
        f = open(strname, 'w+')
        f.write(str(r.text.encode('utf-8')))
        f.close()
        