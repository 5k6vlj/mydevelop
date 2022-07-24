import os
import re

articlePath = r'C:\Users\18719\Desktop\m\article'
contentList = ['# Summary']

for root,dirs,files in os.walk(articlePath):
    if len(files):
        fileName = list(filter(lambda x:'概' in x,files))[0]
        dirName = re.sub(r'.*\\(.*\\)',r'\1',root)
        categoryName = dirName.split('\\')[1]
        categoryContent = '- ['+categoryName+']('+dirName+os.sep+fileName+')'
        contentList.append(categoryContent)

        for file in files:
            dirName = re.sub(r'.*\\(.*\\)', r'\1', root)
            filePath = dirName+os.sep+file
            name = os.path.splitext(file)[0]
            fileContent = '  - ['+name+']('+filePath+')'
            if '#' not in fileContent:
                contentList.append(fileContent)

with open('SUMMARY.md','w',encoding='utf8') as f:
    f.write('\n'.join(contentList))



