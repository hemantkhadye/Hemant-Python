from lxml import html
import requests


def request_web(url):
    try:
        proxy = {"http":"http://sachin:sachin@123@seattle.wonderproxy.com:80",
         "https": "https://sachin:sachin@123@seattle.wonderproxy.com:80"}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        r = requests.get(url, proxies = proxy, headers= headers).text
    except:
        r="<a></a>"
    return r


proxy = {"http": "http://sachin:sachin@123@seattle.wonderproxy.com:80",
         "https": "https://sachin:sachin@123@seattle.wonderproxy.com:80"}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

url='http://www.hkexnews.hk/sdw/search/searchsdw.aspx'
res=html.fromstring(request_web(url))

viewstat=res.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
vieganerator=res.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
eventval=res.xpath('//input[@id="__EVENTVALIDATION"]/@value')[0]

payload={'__VIEWSTATE':viewstat,
'__VIEWSTATEGENERATOR':vieganerator,
'__EVENTVALIDATION':eventval,
'today': 20180406,
'sortBy': '',
'selPartID': '',
'alertMsg': '',
'ddlShareholdingDay': '05',
'ddlShareholdingMonth': '04',
'ddlShareholdingYear': '2018',
'txtStockCode': '00001',
'txtStockName':'',
'txtParticipantID':'',
'txtParticipantName':'',
'btnSearch.x': '37',
'btnSearch.y': '20'}


get_res=requests.post(url,headers=headers,proxies=proxy,data=payload)

post_res=html.fromstring(get_res.text)
print(get_res.text)

tr = post_res.xpath['//tr[@class="row1"]/td[@nowrap="nowrap"][1]/text()[2]']

