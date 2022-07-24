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

def get_content(link):
    web = requests.get(link, headers=rd.choice(headers),timeout=(5,15),proxies={'http':rd.choice(ip)})
    web.encoding = web.apparent_encoding
    textContent = re.search(r'<!-- end mobile-contents button  -->([\d\D]*?)<!-- </content> -->', web.text).group(1)
    content = textContent.replace('\t', '').replace('\r', '').replace('\n', '')
    result_one = re.sub(r'(</h1>).*?<!-- <content> -->', r'\1', content)
    result = re.sub(r'({)|(})',r'\1 \2',result_one)
    return result

def download(data,path,n=3):
    count = 0
    totalCount = len(data)
    errorList = []
    for i in data:
        try:
            dir = path+os.sep+i['category'].replace('/','_').replace('\\','_')
            filepath = dir+os.sep+i['toc_title'].replace('/','_').replace('\\','_').replace('#','_')+'.md'
            content = get_content(i['link'])
            if not os.path.exists(dir):
                os.makedirs(dir)
            with open(filepath,'w',encoding='utf8') as file:
                file.write(content)
            count+=1
            print('共有%d个函数，已处理%d个函数，完成度：%.2f%%'%(totalCount,count,count/totalCount*100))
        except:
            errorList.append(i)
            count+=1
            print('爬取第%d个函数时出现一点错误，已忽略该函数' % count)

    if len(errorList) and n>0:
        print('\n本次共有%d个函数爬取失败，正在尝试重新爬取\n'%len(errorList))
        download(errorList,path,n-1)
    if len(errorList) and n==0:
        print('多次爬取失败，相关函数信息已保存为错误日志，请查看errorlog.txt文件')
        with open(path+os.sep+'errorlog.txt','a',encoding='utf8') as f:
            for i in errorList:
                f.write(str(i)+'\n')


if __name__ == '__main__':
    url = 'https://docs.microsoft.com/zh-cn/dax/toc.json'
    web = requests.get(url,headers=rd.choice(headers))
    web.encoding = web.apparent_encoding
    jsonData = json.loads(web.text)['items'][0]['children'][1]['children'][2:]
    data = []
    for i in jsonData:
        for j in i['children']:
            j['category']=i['toc_title']
            j['link']='https://docs.microsoft.com/zh-cn/dax/'+j['href']
            data.append(j)

    path = 'c:/users/18719/desktop/article'
    download(data,path)
    print('\n----------爬取结束----------')

    # 创建SUMMARY.md文件
    print('\n----------正在创建SUMMARY.md文件----------')

    dirName = re.sub(r'.*[\\/]','',path)
    contentList = ['# Summary']
    for i in jsonData:
        ShowName = i['toc_title']
        RealName = ShowName.replace('/','_').replace('\\','_')
        fileName = i['children'][0]['toc_title']
        Link = dirName+os.sep+RealName+os.sep+fileName.replace('/','_').replace('\\','_').replace('#','_')+'.md'
        contentList.append('- ['+ShowName+']('+Link+')')
        for j in i['children']:
            ShowName = j['toc_title']
            RealName = j['category'].replace('/', '_').replace('\\', '_')
            fileName = ShowName
            Link = dirName+os.sep+RealName+os.sep+fileName.replace('/','_').replace('\\','_').replace('#','_')+'.md'
            contentList.append('  - [' + ShowName + '](' + Link + ')')

    with open(path+os.sep+'SUMMARY.md', 'w', encoding='utf8') as f:
        f.write('\n'.join(contentList))

    print('\n----------创建成功----------')