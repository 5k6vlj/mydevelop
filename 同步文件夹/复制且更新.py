#开发人员  ： 夕枫丶
#开发时间  ： 2019/12/1 0001  18:26
#文件名称  ： 复制且更新.py
#开发工具  ： PyCharm

import os
import hashlib

print('''#开发人员  ： 夕枫丶
#开发时间  ： 2019/11/30 0030  22:01
#开发工具  ： PyCharm
#使用说明  ： source 文件夹为本地文件夹，target 文件夹为目标文件夹
#功能  ： 将source文件夹中与target文件夹不同的文件复制到target文件夹中,并更新target文件夹里的相同文件

''')

path_s=input("Please input the source path : ")
path_t=input("Please input the target path : ")


def copy_update_file(paths,patht):
    for filename in os.listdir(paths):
        filename_s = paths+os.sep+filename
        filename_t = patht+os.sep+filename
        if os.path.isdir(filename_s):
            if not os.path.exists(filename_t):
                os.mkdir(filename_t)
                print('[!] "%s" successful create! ' % filename_t)
            copy_update_file(filename_s,filename_t)
        else:
            if os.path.exists(filename_t):
                with open(filename_s,'rb') as f_s:
                    data=f_s.read()
                    fs_md5=hashlib.md5(data).hexdigest()
                    with open(filename_t,'rb') as f_t:
                        ft_md5=hashlib.md5(f_t.read()).hexdigest()
                    if fs_md5!=ft_md5:
                        with open(filename_t,'wb') as f_t:
                            f_t.write(data)
                            print('[#] "%s" already update! ' % filename_t)
            else:
                print('[*]  Source :',filename_s)
                print('[*]  Target :',filename_t,"\n")
                with open(filename_s,'rb') as f_s:
                    with open(filename_t,'wb') as f_t:
                        f_t.write(f_s.read())
copy_update_file(path_s,path_t)
os.system("pause")