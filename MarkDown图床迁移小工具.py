import os,re

replaceNum = 0

def replace_img_domain(srcdir,tardir,srcdomain,tardomain,mode):
    global replaceNum
    if mode=='1' :
        for fileItem in os.listdir(srcdir):
            srcFilePath = srcdir+os.sep+fileItem
            tarFilePath = tardir+os.sep+fileItem
            if os.path.isdir(srcFilePath):
                if not os.path.exists(tarFilePath):
                    os.mkdir(tarFilePath)
                replace_img_domain(srcFilePath,tarFilePath,srcdomain,tardomain,mode)
            elif os.path.splitext(srcFilePath)[1]!=".md":
                with open(tarFilePath,'w',encoding='utf8') as fileWriter:
                    with open(srcFilePath,'r',encoding='utf8') as fileReader:
                        fileWriter.write(fileReader.read())
                print('【{0}】 不是MarkDown文件,只复制不替换\n'.format(srcFilePath))
            else:
                print('【{0}】 为MarkDown文件,正在进行处理：\n'.format(srcFilePath))
                with open(tarFilePath,'w',encoding='utf8') as fileWriter:
                    with open(srcFilePath,'r',encoding='utf8') as fileReader:
                        content = fileReader.read()
                        rePattern = r'!\[.*?\]\((.*?)\)|<img.*?src=[\'\"](.*?)[\'\"].*?>'
                        imglinks = [''.join(i) for i in re.findall(rePattern,content)]
                        sublinks = [i.replace(srcdomain,tardomain) for i in imglinks]
                        if imglinks==sublinks:
                            print('\t该文件的所有图片中不存在指定的域名，只复制不替换，请检查域名是否有误！\n')
                        else:
                            for srclink,tarlink in zip(imglinks,sublinks):
                                if srclink!=tarlink:
                                    content = content.replace(srclink, tarlink)
                                    print('\t'+srclink+' -> '+tarlink)
                            print('\n')
                            replaceNum += 1
                        fileWriter.write(content)
    elif mode=='2':
        if os.path.splitext(srcdir)[1]!=".md" or os.path.splitext(tardir)[1]!=".md":
            print('原始文件路径或目标文件路径不是MarkDown文件,请检查路径是否有误！\n')
        else:
            print('正在进行处理：\n')
            with open(tardir,'w',encoding='utf8') as fileWriter:
                with open(srcdir,'r',encoding='utf8') as fileReader:
                    content = fileReader.read()
                    rePattern = r'!\[.*?\]\((.*?)\)|<img.*?src=[\'\"](.*?)[\'\"].*?>'
                    imglinks = [''.join(i) for i in re.findall(rePattern,content)]
                    sublinks = [i.replace(srcdomain,tardomain) for i in imglinks]
                    if imglinks==sublinks:
                        print('\t该文件的所有图片中不存在指定的域名，只复制不替换，请检查域名是否有误！\n')
                    else:
                        for srclink,tarlink in zip(imglinks,sublinks):
                            if srclink!=tarlink:
                                content = content.replace(srclink, tarlink)
                                print('\t'+srclink+' -> '+tarlink)
                        print('\n')
                        replaceNum += 1
                    fileWriter.write(content)


# https://cdn.jsdelivr.net/gh/xifenghhh/Image/img/gzhyjlq.png

print('''# 开发人员  ： 夕枫
# 开发时间  ： 2022/4/14
# 文件名称  ： MarkDown图床迁移小工具
# 开发工具  ： PyCharm
# 工具作用  ： 替换MarkDown文件中所有图片链接的域名为指定域名，仅替换图片，非图片链接即使匹配亦忽略
# 使用说明  ： 
    1、支持单个MarkDown文件替换，以及文件夹递归替换
    2、文件夹模式下非MarkDown文件只复制文件，而不替换链接
    3、最终得到的文件或文件夹的结构与原始内容一致，但MarkDown文件的图片链接将被替换成指定域名，非图片链接即使匹配亦不替换
''')

try:
    mode = input('请输入替换模式，[1]:文件夹，[2]:单个MarkDown文件 ：')
    if mode=="1":
        srcdir = input('请输入需要进行图床迁移的文件夹路径 ：')
        tardir = input('请输入结果存放路径，若路径不存在将自动创建 ：')+os.sep+'result'
        srcdomain = input('请输入原始域名 ：')
        tardomain = input('请输入迁移域名 ：')
        if not os.path.exists(tardir):
            os.makedirs(tardir)
        replace_img_domain(srcdir, tardir, srcdomain, tardomain, mode)

    elif mode=="2":
        srcdir = input('请输入需要进行图床迁移的MarkDown文件路径 ：')
        tardir = input('请输入结果存放路径，若路径不存在将自动创建 ：')
        srcdomain = input('请输入原始域名 ：')
        tardomain = input('请输入迁移域名 ：')
        if not os.path.exists(tardir):
            os.makedirs(tardir)
        tardir = tardir +os.sep + 'new_' + os.path.split(srcdir)[1]
        replace_img_domain(srcdir,tardir,srcdomain,tardomain,mode)

    print('共替换%s个MarkDown文件'%replaceNum)
except :
    print('请检查输入的参数是否存在错误！')

os.system('pause')