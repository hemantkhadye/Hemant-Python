# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import time
import calendar
import os
from bs4 import BeautifulSoup
#     return proxy_support
Inv1=[]
# =============================================================================
proxy_support = {'https':'https://11115:7My2Ng@world.nohodo.com:6811'} #world.nohodo.com,6811,11115,7My2Ng

#==============================================================================

#==================code to calculate epoch time===============
def CacheCode():
    epoch = calendar.timegm(time.gmtime()) #calendar.timegm(time.strptime('Jul 9, 2009 @ 20:02:58 UTC', '%b %d, %Y @ %H:%M:%S UTC'))
    return epoch
##================================================================================

url = "https://www.qoo10.sg/item/APPLE-IPHONE-X-8-8-PLUS-7-7-PLUS-CASE-IPHONE-6-6S-6-PLUS-6S-PLUS-PHONE/436539985"
res = requests.get(url,proxies = proxy_support)
cookie = res.cookies
#print(res.text)
soup = BeautifulSoup(res.text,"lxml")
#print(soup.prettify)
file = open('prd.html','w+')
file.write(str(res.text.encode('utf-8')))
file.close()
# =============================================================================
Var_Total_Count = len(soup.find_all('div', {"id": lambda x: x and x.startswith('inventory_outer_')}))
gd_no = str(soup.find("input", {"id": "GD_NO"})["value"])
inventory_no =  soup.find("input", {"id": "inventory_no"})["value"]
global_order_type = soup.find("input", {"id": "global_order_type"})["value"]
inventory_yn = soup.find("input", {"id": "inventory_yn"})["value"]
lang_cd = soup.find("input", {"id": "lang_cd"})["value"]
link_type = soup.find("input", {"id": "link_type"})["value"]



optDiv = soup.find_all('li', {"id": lambda x: x and x.startswith('li_inventory_')})

#print(optDiv)
#liTags =optDiv.find_all("li")
for f in optDiv:
    Inv1.append(f.text)
print(len(Inv1))
# =============================================================================
cnt=2
token = CacheCode()
posturl = "https://www.qoo10.sg/gmkt.inc/swe_GoodsAjaxService.asmx/GetGoodsInventoryEachLevelNameByKeyword"
#postData= "'inventory_no':' " + str(inventory_no) + "','sel_value1':' " + str(Inv1[0]) + "','sel_value2':'','sel_value3':'','sel_value4':'','level':" + str(cnt) + ",'sel_count':" + str(Var_Total_Count) + ",'keyword':'','lang_cd':'" + str(lang_cd) + "','global_order_type':'" + str(global_order_type) + "','gd_no':'" + str(gd_no) + "','inventory_yn':'" + str(inventory_yn) + "','link_type':'" + str(link_type) + "','___cache_expire___':'" + str(token) +"'"
postData= "'inventory_no':'" + str(inventory_no) + "','sel_value1':'" + str(Inv1[0]) + "','sel_value2':'','sel_value3':'','sel_value4':'','level':" + str(cnt) + ",'sel_count':" + str(Var_Total_Count) + ",'keyword':'','lang_cd':'" + str(lang_cd) + "','global_order_type':'" + str(global_order_type) + "','gd_no':'" + str(gd_no) + "','inventory_yn':'" + str(inventory_yn) + "','link_type':'" + str(link_type) + "','___cache_expire___':'" + str(token) +"'"
print(postData)
headers = {'Accept':'*/*','Content-Type':'application/json; charset=utf-8', 'Host':'www.qoo10.sg','Origin':'https://www.qoo10.sg','Referer':'' + url + '','User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
response1 = requests.post(posturl,data = postData,headers = headers, cookies =cookie ,proxies =proxy_support)
print(response1.text)
