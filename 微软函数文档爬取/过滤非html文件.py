import os

path = r'C:\Users\18719\Desktop\docs\_book\m\article'

for root,dirs,files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1]!='.html':
            os.remove(os.path.join(root,file))