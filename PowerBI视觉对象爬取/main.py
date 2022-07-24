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

def get_info_perpage(n):
    url = 'https://appsource.microsoft.com/en-us/marketplace/apps?page='+str(n)+'&product=power-bi-visuals'
    web = requests.get(url,headers=rd.choice(headers),proxies={'http':rd.choice(ip)},timeout=(5,10))
    web.encoding=web.apparent_encoding
    jsonData = json.loads(re.search(r'__INITIAL_STATE__=(.*?)};',web.text).group(1)+'}')['apps']['dataList']
    return jsonData


allData = []
def get_page(pageNumList,n=3):
    errorList = []
    if n==3:
        print('\n正在获取视觉对象信息，请稍候\n')

    for i in pageNumList:
        try:
            content = get_info_perpage(i)
            allData.extend(content)
        except:
            errorList.append(i)
    if len(errorList) and n>0:
        get_page(errorList,n-1)
    if len(errorList) and n==0:
        print('本次爬取中，第'+'、'.join(errorList)+'页的视觉对象信息获取失败，将爬取其它页面的视觉对象')

def download(data,path,n=3):
    if n==3:
        print('开始下载视觉对象，请稍候\n')

    dir = path+os.sep+'PowerBI Visuals Result'
    if not os.path.exists(dir):
        os.mkdir(dir)
    count = 0
    totalCount = len(data)
    errorList = []
    for i in data:
        try:
            name = i['title'].replace('/','_').replace('\\','_')
            pbix = dir+os.sep+name+'.pbix'
            pbiviz = dir+os.sep+name+'.pbiviz'
            pbixUrl = i['downloadSampleLink']
            pbivizUrl = i['downloadLink']

            with open(pbix,'wb') as file:
                content = requests.get(pbixUrl,headers=rd.choice(headers),proxies={'http':rd.choice(ip)},timeout=(5,10))
                content.encoding=content.apparent_encoding
                file.write(content.content)
            with open(pbiviz,'wb') as file:
                content = requests.get(pbivizUrl,headers=rd.choice(headers),proxies={'http':rd.choice(ip)},timeout=(5,10))
                content.encoding=content.apparent_encoding
                file.write(content.content)

            count+=1
            print('共有%d个视觉对象，已处理%d个，完成度：%.2f%%'%(totalCount,count,count/totalCount*100))
        except:
            errorList.append(i)
            count+=1
            print('爬取第%d个视觉对象时出现一点错误，已跳过' % count)

    if len(errorList) and n>0:
        print('\n本次共有%d个视觉对象爬取失败，正在尝试重新爬取\n'%len(errorList))
        download(errorList,path,n-1)
    if len(errorList) and n==0:
        print('多次爬取失败，相关的视觉对象信息已保存为错误日志，请查看errorlog.txt文件')
        with open(path+os.sep+'errorlog.txt','a',encoding='utf8') as f:
            for i in errorList:
                f.write(str(i)+'\n')

if __name__ == '__main__':

    print('''# 开发人员  ： 夕枫
# 开发时间  ： 2022/4/25
# 工具作用  ： 爬取PowerBI视觉对象
# 使用说明  ： 
        1、只需输入页数N，即可自动爬取前N页的视觉对象与演示文件
        2、结果存放在本工具所在路径下的PowerBI Visuals Result文件夹中
        3、如不确定页数，建议输入10
        4、官网地址：https://appsource.microsoft.com/en-us/marketplace/apps?page=1&product=power-bi-visuals
''')
    try:
        pageNum = input('请输入要爬取的页数：')
        pageNumList = list(range(1,int(pageNum)+1))

        get_page(pageNumList)

        download(allData,os.getcwd())

        print('\n----------爬取结束----------')
        os.system('pause')
    except:
        print('请检查参数是否输入有误。若无误，则本工具已失效！')