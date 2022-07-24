import os,re
import json
import requests
import random as rd
from bs4 import BeautifulSoup


headers = [
{'user-agent':'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1'},
{'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1'},
{'user-agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
{'user-agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}
]
ip = ['115.75.5.17:38351','14.215.212.37:9168','103.37.141.69:80','120.220.220.95:8085','106.54.128.253:999']


link = 'https://support.microsoft.com/zh-cn/office/betadist-%E5%87%BD%E6%95%B0-49f1b9a9-a5da-470f-8077-5f1730b5fd47'
web = requests.get(link, headers=rd.choice(headers),proxies={'http':rd.choice(ip)},timeout=(5,15))
web.encoding = web.apparent_encoding
Soup = BeautifulSoup(web.text,'lxml')
textContent = str(Soup.select('div#supArticleContent')[0])
content = textContent.replace('\t', '').replace('\r', '').replace('\n', '')
result = re.sub(r'<div class="ocArticleFooterSection".*(</div>)$',r'\1',content)
result = re.sub(r'({)|(})',r'\1 \2',result)




