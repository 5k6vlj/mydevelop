import pandas as pd
import os
import shutil
print('''
# 作者：夕枫
# 功能：拆分Excel工作表或txt、csv文本文件
'''
)

def SplitTable_excel(Path,SheetName,SplitColumn,Code):
    data = pd.read_excel(Path,sheet_name=SheetName)
    SplitColumnData = data[[SplitColumn]].drop_duplicates()
    if Code == '1' :
        with pd.ExcelWriter('Split_Result.xlsx') as writer:
            for i in range(len(SplitColumnData)):
                ItemName = SplitColumnData.iloc[i,0]
                dataset = data[data[SplitColumn]==ItemName]
                dataset.to_excel(writer,sheet_name=str(ItemName),index=False)
        print('拆分成功')
    elif Code == '2':
        if os.path.exists('Split_Result'):
            shutil.rmtree('Split_Result')
            os.mkdir('Split_Result')
        else:
            os.mkdir('Split_Result')
        for i in range(len(SplitColumnData)):
            ItemName = SplitColumnData.iloc[i,0]
            dataset = data[data[SplitColumn]==ItemName]
            dataset.to_excel('Split_Result/'+str(ItemName)+'.xlsx',sheet_name=str(ItemName),index=False) 
        print('拆分成功')
    else:
        print('请输入正确的拆分模式！')

def SplitTable_csv(Path,Sep,EnCoding,SplitColumn,Code):
    data = pd.read_csv(Path,sep=Sep,encoding=EnCoding,engine='python')
    SplitColumnData = data[[SplitColumn]].drop_duplicates()
    if Code == '1' :
        with pd.ExcelWriter('Split_Result.xlsx') as writer:
            for i in range(len(SplitColumnData)):
                ItemName = SplitColumnData.iloc[i,0]
                dataset = data[data[SplitColumn]==ItemName]
                dataset.to_excel(writer,sheet_name=str(ItemName),index=False)
        print('拆分成功')
    elif Code == '2':
        if os.path.exists('Split_Result'):
            shutil.rmtree('Split_Result')
            os.mkdir('Split_Result')
        else:
            os.mkdir('Split_Result')
        for i in range(len(SplitColumnData)):
            ItemName = SplitColumnData.iloc[i,0]
            dataset = data[data[SplitColumn]==ItemName]
            dataset.to_excel('Split_Result/'+str(ItemName)+'.xlsx',sheet_name=str(ItemName),index=False) 
        print('拆分成功')
    else:
        print('请输入正确的拆分模式！')
try:
    label = input('请输入拆分类型：1、拆分Excel工作簿，2、拆分文本文件 : ')
    if int(label) == 1 :
        print('''
            # 请依次输入以下信息：
            # Path：Excel工作簿的路径
            # SheetName：要拆分的工作表的表名
            # SplitColumn：拆分依据字段
            # Code：拆分模式，1：拆分为多个Excel工作表，2：拆分为多个Excel工作簿
            ''')
        Path = input('Path：')
        SheetName = input('SheetName：')
        SplitColumn = input('SplitColumn：')
        Code = input('Code：')
        SplitTable_excel(Path,SheetName,SplitColumn,Code) 
    elif int(label) ==2 :
        print('''
            # 请依次输入以下信息：
            # Path：文本文件的路径
            # Sep：文本数据的分隔符
            # EnCoding：文本文件的编码，若不清楚则可尝试输入：utf8
            # SplitColumn：拆分依据字段
            # Code：拆分模式，1：拆分为多个Excel工作表，2：拆分为多个Excel工作簿
            ''')
        Path = input('Path：')
        Sep = input('Sep：')
        EnCoding = input('EnCoding：')
        SplitColumn = input('SplitColumn：')
        Code = input('Code：')
        SplitTable_csv(Path,Sep,EnCoding,SplitColumn,Code)
except:
    print('请检查输入的参数是否存在错误！')
        
os.system('pause')
