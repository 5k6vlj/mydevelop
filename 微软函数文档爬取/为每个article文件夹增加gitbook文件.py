import os
import re
import shutil

path = r'C:\Users\18719\Desktop\docs\_book'
srcpath = r'C:\Users\18719\Desktop\_book\gitbook'

targetPath = []
for root,dirs,files in os.walk(path):
    for dir in dirs:
        dirpath = os.path.join(root,dir)+os.sep+'gitbook'
        if 'article' in dirpath:
            targetPath.append(dirpath)

targetPath = tuple(targetPath)
for i in targetPath:
    shutil.copytree(srcpath,i)

