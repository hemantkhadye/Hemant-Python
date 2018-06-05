# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:49:36 2018

@author: Tech
"""

import requests
import os
from bs4 import BeautifulSoup
import xlsxwriter
Cat_1_URL = []
Cat_1_Count = []
Cat_2_URL = []
Cat_2_Count = []
Cat_3_URL = []
Cat_3_Count = []

Cpath = "E:\\Hemant Python\\Qoo10\\"
filename = Cpath + "11StreetCountPython.xlsx"
workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet()
row = 1
col = 0


# proxy_support ={'https': 'https://11115:7My2Ng@world.nohodo.com:6811'}
# Mainurl = "http://www.11street.my/"
# response = requests.get(Mainurl, proxies = proxy_support)
# soup = BeautifulSoup(response.text, "lxml")
# ul = soup.find_all("ul", class_="meta-categories-list wrapper")
#========================================================================
# Extracting first level cat
# for l in ul:
#     li = l.find_all("li")
#     for i in li:
#         a = i.find("a")
#         URL = a['href']
#         name = a.text
#         Cat_1_URL.append(URL)
#         worksheet.write(row, 0, URL)
#         worksheet.write(row, 1, name)
#         print(name)
#         row += 1
#========================================================================

filename = Cpath + "SubCat_count11street.xlsx"
subURLBook = xlsxwriter.Workbook(filename)
subCatSheet = subURLBook.add_worksheet()
r1 = 1
c1 = 0
subCatSheet.write(r1, 0, 'URL')
#subCatSheet.write(r1, 1, 'Cat Name')
subCatSheet.write(r1, 2, 'Count')
subCatSheet.write(r1, 3, 'CCC')

#========================================================================

# for url in Cat_1_URL:
#     res = requests.get(url, proxies = proxy_support)
#     psoup = BeautifulSoup(res.text, "lxml")
#     # Extracting subcat
#     ul = psoup.find("div", {"class": "r_cont"})
#     li = ul.find_all("li")
#     filler = '&gdsc_cd='
#     for lidiv in li:
#         a = lidiv.find('a')
#         atext = a.text
#         ahref = a['data-code']
#         cnt = lidiv.find('span').text
#         cnt = cnt.replace(',', '')
#         cnt = cnt.replace('.', '')
#         print(atext, " --- ", ahref)
#         link = url + filler + ahref
#         Cat_2_URL.append(link)
#         Cat_2_Count.append(cnt)
#         subCatSheet.write(r1, 0, link)
#         subCatSheet.write(r1, 1, atext)
#         subCatSheet.write(r1, 2, cnt)
#         subCatSheet.write(r1, 3, url)
#         r1 += 1

# =============================================================================

subCatSplitSheet = subURLBook.add_worksheet(name='Split URL')
Cr = 1
subCatSplitSheet.write(Cr, 0, 'URL')
subCatSplitSheet.write(Cr, 1, 'Count')
subCatSplitSheet.write(Cr, 2, 'Pages')
subCatSplitSheet.write(Cr, 3, 'Split URL Part')
subCatSplitSheet.write(Cr, 4, 'Split URL')
Cr += 1
part1 = "SG|No:"
part2 = "|asg|asg|Fashion|NA|NR|Seller"
for i in range(0, len(Cat_2_URL)):
    link = Cat_2_URL[i]
    cnt = int(Cat_2_Count[i])
    pno = 1
    pages = int(cnt/120)
    if cnt % 120 > 0:
        pages += 1
    PgSplitCnt = int(pages / 50)
    if pages % 50 > 0:
        PgSplitCnt += 1
    for j in range(0,PgSplitCnt):
        SplitURL = part1 + str(pno) + link + part2
        print(SplitURL)
        subCatSplitSheet.write(Cr, 0, link)
        subCatSplitSheet.write(Cr, 1, cnt)
        subCatSplitSheet.write(Cr, 2, pages)
        subCatSplitSheet.write(Cr, 3, PgSplitCnt)
        subCatSplitSheet.write(Cr, 4, SplitURL)
        pno += 50
        Cr += 1
# =============================================================================
subURLBook.close()

