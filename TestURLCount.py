from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup
import xlsxwriter
catdata=[]
caturl = []
catcount =[]

proxy_support ={'https': 'https://11115:7My2Ng@world.nohodo.com:6811'}
#===========code to iterate through the excel file=============================

workbook = xlsxwriter.Workbook('E:\\Namshi.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1','URL','bold')
worksheet.write('B1','Name','bold')
worksheet.write('C1','Count','bold')
row = 1
col = 0


file = open("E:\\Namshi.text",'w+')
url = "https://en-ae.namshi.com/"
rs= requests.get(url,proxies=proxy_support)
soup = BeautifulSoup(rs.text, "lxml")
catLink = soup.find_all("li",{"data-nm-hover-toggle": "data-nm-hover-toggle"})
for cat in catLink:
    liList = cat.find_all("ul",{"class": "level_02"})
    for li in liList:
        aTag = li.find("a")
        CatName = aTag.text
#        file.write(CatName +"{")
        worksheet.write(row,1,CatName)
        CatUrl = "https://en-ae.namshi.com" + aTag["href"]
#        worksheet.write(row,1,CatUrl)
        caturl.append(CatUrl)
        row += 1
        
for url in caturl:
    worksheet.write(row,0,url)
    file.write(url +"{")
    rss= requests.get(url,proxies=proxy_support)
    soup = BeautifulSoup(rss.text, "lxml")
    count = soup.find("p",{"class": "items"})
    print(url)
    print(count)
    if count != []:
        cnt = count.text
       
        file.write(cnt +"{")
        worksheet.write(row,2,cnt)
        catcount.append(cnt)
        file.write("|")
    
# =============================================================================
# for data , url , cnt from zip(catdata, caturl,catcount):
#     file.write(data, "!+", url, "!+", cnt)
# file.close()
# =============================================================================

file.close()
workbook.close()