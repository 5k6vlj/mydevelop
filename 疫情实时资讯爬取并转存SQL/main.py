import akshare as ak
import pandas as pd
import pymysql

connect = pymysql.connect(host='localhost',user='xifeng',password='nhjdwm',database='mytest')
cursor = connect.cursor()

create_table = '''
create table if not exists covid19ReportNews(
    id int primary key not null auto_increment,
    title varchar(255),
    detail varchar(255),
    time varchar(255),
    link varchar(2000)
);
'''
delete_table = 'truncate table covid19ReportNews;'
update_table = 'insert into covid19ReportNews(title,detail,time,link) values (%s,%s,%s,%s);'

covid_19_163_df = ak.covid_19_163(indicator="实时资讯新闻播报")
if len(covid_19_163_df):
    cursor.execute(create_table)
    cursor.execute(delete_table)
    cursor.executemany(update_table,[tuple(i) for i in covid_19_163_df.values])
else:
    cursor.execute(create_table)

connect.commit()
cursor.close()
connect.close()
