#开发人员  ： 夕枫丶
#开发时间  ： 2019/11/30 0030  22:01
#文件名称  ： 同步文件夹内容.py
#开发工具  ： PyCharm
import os



path_s=input("Please input the source path : ")
path_t=input("Please input the target path : ")

def copy_file(paths,patht):
    for filename in os.listdir(paths):
        filename_s = paths+os.sep+filename
        filename_t = patht+os.sep+filename
        if os.path.isdir(filename_s):
            if not os.path.exists(filename_t):
                os.mkdir(filename_t)
                print('[*] "%s" successful create! ' % filename_t)
            copy_file(filename_s,filename_t)
        else:
            if os.path.exists(filename_t):
                print('[*] "%s" already exists! ' % filename_t)
            else:
                print('[*]  Source :',filename_s)
                print('[*]  Target :',filename_t,"\n")
                with open(filename_s,'rb') as f_s:
                    with open(filename_t,'wb') as f_t:
                        f_t.write(f_s.read())

copy_file(path_s,path_t)
os.system("pause")