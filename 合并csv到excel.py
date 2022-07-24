import pandas as pd
import os
import shutil

dirpath = '1'
files = os.listdir(dirpath)
with pd.ExcelWriter('CombineResult.xlsx') as writer:
    for file in files:
        filepath = dirpath+os.sep+file
        filename = file.split('.')[0]
        data = pd.read_csv(filepath)
        data.to_excel(writer,sheet_name=str(filename),index=False)