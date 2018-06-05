import requests
import os
from bs4 import BeautifulSoup
# from openpyxl import load_workbook
import xlsxwriter
# import random
import json

UserAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
session = requests.Session()        #code changes By Harsh Dubey
#==============================================================================
session.headers = ({
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7'})
proxy_support = {'http': 'http://11115:7My2Ng@world.nohodo.com:6811'}

#==============================================================================
homeurl = "http://www.chatchaipharmacy.com/"
response = session.get(homeurl, proxies=proxy_support, headers = session.headers)
#Homecookie = response.cookies
soup = BeautifulSoup(response.text, "lxml")
# tokenTag = soup.find("input", {"name": "_token"})
# token = tokenTag["value"]
print(response)

#==============================================================================

loginurl = "http://www.chatchaipharmacy.com/services/api/users/login"
logindata = {"email": "Lazada2@cc.com", "password": "lazada2"}
headers = {'Accept': '*/*', 'Content-Type': 'application/json', 'Referer': 'http://www.chatchaipharmacy.com/', 'Origin': 'http://www.chatchaipharmacy.com', 'Host': 'www.chatchaipharmacy.com', 'User-Agent': UserAgent}
response1 = session.post(loginurl, data=logindata, proxies=proxy_support, headers = session.headers)
print(response1)
json_data = json.loads(response1.text)
token =json_data['token']
print([token])
#===================================================================================
pNo = 1
offset = 0
workbook = xlsxwriter.Workbook("C:\\Users\\Hemant.Khadye\\Desktop\\Python Training\\DataOut.xlsx")
worksheet = workbook.add_worksheet()
row = 0
col = 0
worksheet.write(row, col, "Product URL")
worksheet.write(row, col+1, "Name")
worksheet.write(row, col+2, "Price")
worksheet.write(row, col+3, "Brand")
worksheet.write(row, col+4, "Seller SKU")
worksheet.write(row, col+5, "Description")
worksheet.write(row, col+6, "Image")
row += 1

headers1 = {'Accept': '*/*', 'Content-Type': 'application/json', 'Referer': 'http://www.chatchaipharmacy.com/', 'Origin': 'http://www.chatchaipharmacy.com', 'Host': 'www.chatchaipharmacy.com', 'User-Agent': UserAgent, 'Token': token}
while pNo != 33:
    PageURL = "http://www.chatchaipharmacy.com/services/api/products?offset=" + str(offset) + "&page=" + str(pNo) + "&limit=100"
    print(PageURL)
    PageReq = requests.get(PageURL, headers=headers1, proxies=proxy_support)
    # print(PageReq.text)
    prod_Data = json.loads(PageReq.text)
    Prod_detail = prod_Data['products']
    for pr in Prod_detail:
        col = 0
        # print(Prod_detail.keys())
        Produrl = "http://www.chatchaipharmacy.com/products/" + pr['productCode']
        worksheet.write(row, col, Produrl)
        worksheet.write(row, col + 1, pr['productName'])
        worksheet.write(row, col + 2, pr['price'])
        worksheet.write(row, col + 3, pr['genericName'])
        worksheet.write(row, col + 4, pr['companyCode'])
        worksheet.write(row, col + 5, pr['description'])
        if pr['imagePath'] != []:
            print(pr['imagePath'])
            img = "http://www.chatchaipharmacy.com" + str(pr['imagePath'])
            worksheet.write(row, col + 6, img)
        row += 1
       # print(pr)
    pNo += 1
    offset += 100
workbook.close()

#Setcookies code
# http = httplib2.Http()
# # get cookie_value here
# headers = {'Cookie':cookie_value}
# response, content = http.request("http://www.theURL.com", 'GET', headers=headers)

