import os,re
import json
import requests
import random as rd

headers = [
{'user-agent':'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1'},
{'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1'},
{'user-agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
{'user-agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}
]
ip = ['115.75.5.17:38351','14.215.212.37:9168','103.37.141.69:80','120.220.220.95:8085','106.54.128.253:999']

pbixUrl = 'https://visuals.azureedge.net/app-store/chicletSlicer.ChicletSlicer1448559807354.1.6.3.0.pbix'

with open('test.pbix', 'wb') as file:
    content = requests.get(pbixUrl, headers=rd.choice(headers), proxies={'http': rd.choice(ip)}, timeout=(5, 10))
    content.encoding = content.apparent_encoding
    file.write(content.content)