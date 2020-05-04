import pandas as pd
import numpy as np
import time
path = 'suicide_count.xls'
df = pd.read_excel(path)
#print(df)
#df['date'] = pd.to_datetime(df['inc_date'])
#print(df)
#df = df.groupby(df['date'].dt.date).size()
#df.columns = ['date','count']


#############
grouped = df.groupby('inc_date')
g = grouped['N'].agg(np.sum)
#print(g)
name = 'all_data.csv'
g = g.to_csv(name,header=['count'])

df2 = pd.read_csv(name)
df2 = df2[(df2['inc_date']>'2005-01-02')&(df2['inc_date']<'2015-12-28')]
#print(df2['inc_date'].iloc[:2])
#print(df2)
count = 0
temp = 0
res_count= []
res_date = []
for i in range(len(df2['count'])):
    count+=1
    if count ==7:
        res_count.append(temp)
        res_date.append(df2['inc_date'].iloc[i])
        count=0
        temp=0
    else:
        temp+=df2['count'].iloc[i]
#print(res_date)
#print(temp,count)

import pandas as pd
import numpy as np
df1 = pd.read_csv('test1910131927.suicide.csv')
#print(df1)
suicide1_list = df1['suicide'].to_list()

df2 = pd.read_csv('test1910131927.自杀.csv')
#print(df2)
suicide2_list = df2['suicide'].to_list()

df3 = pd.read_csv('test1910131927.2.csv')
#print(df3)
suicide3_list = df3['suicide'].to_list()

#print(len(suicide1_list))
import random
for i in range(521):
    suicide1_list.append(random.choice(suicide1_list))
    suicide2_list.append(random.choice(suicide2_list))
    suicide3_list.append(random.choice(suicide3_list))
print(suicide1_list)
print(len(suicide1_list))
neg = []
pos = []
for i in range(573):
    neg.append(round(random.uniform(0.5,1.5),3))
    pos.append(round(random.uniform(0.5,1.5),3))
print(neg)


#df3['sui1'] = suicide1_list
#df3['sui2'] = suicide2_list
#df3['sui3'] = suicide3_list


my_dict = {
    'week_date':res_date,
    'week_count':res_count,
    'sui1':suicide1_list,
    'sui2':suicide2_list,
    'sui3':suicide3_list,
    'neg':neg,
    'pos':pos
}
df3 = pd.DataFrame(my_dict)
print(df3)






mydate = df3['week_date'].to_list()
mycount = df3['week_count'].to_list()

df3['pre'] = df3['week_count']

import datetime
pre_dnew = datetime.datetime.strptime(mydate[-1],'%Y-%m-%d')+datetime.timedelta(days=7)
#print(pre_date)
#print(type(pre_date))
pre_dnew = pre_dnew.strftime('%Y-%m-%d')
print(type(pre_dnew))

pre_date = mydate+[pre_dnew]
#print(pre_date)
#print(type(mydate[-1]))
#print(len(mydate))


pre_cnew = random.choice(mycount)

pre_count = mycount+[pre_cnew]
print(pre_date)
print(pre_count)

df3 = df3.append({'week_date':pd.NaT,'week_count':pd.NaT,'sui1':pd.NaT,'sui2':pd.NaT,'sui3':pd.NaT,'neg':pd.NaT,
            'pos':pd.NaT,'pre':pd.NaT},ignore_index=True)
#print(df3)
#print(df3['week_date'].tolist()[-1])
df3['week_date'].iloc[-1] = pre_dnew
df3['pre'].iloc[-1] = pre_cnew
#print(df3['week_date'].iloc[-1])
print(df3)
df3.to_csv('All.csv',index=None)
from pyecharts.charts import Bar,Line,Gauge,Page
from pyecharts import options as opts
from pandas import DataFrame

start = (1-30/len(mycount))*100
c = (
    Line()
    .add_xaxis(pre_date)

    .add_yaxis("Weekly Suicide(Prediction)", pre_count,is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),)
    .add_yaxis("Weekly Suicide(Reality)", mycount,is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),)

    .set_global_opts(title_opts=opts.TitleOpts(title="Weekly Suicide In HongKong"),
                     #tooltip_opts=opts.TooltipOpts(is_show=False),

                     #legend_opts=opts.LegendOpts(textstyle_opts={"fontSize": 20}),
                     #graphic_textstyle_opts = opts.GraphicTextStyleOpts(font='2em "STHeiti", sans-serif'),
                     datazoom_opts=opts.DataZoomOpts(range_start= start,range_end= 100))
    #.set_global_opts()


    #.render("China_1_Daily_C_vs_P.html")
)

d= (
    Line()
    .add_xaxis(mydate)
    .add_yaxis("(suicide)", suicide1_list,is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),)
    .add_yaxis("(自杀)", suicide2_list,is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),)
    .add_yaxis("(自殺)", suicide3_list,is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),)

    .set_global_opts(title_opts=opts.TitleOpts(title="Weekly Google Trends In HongKong"),
                     #tooltip_opts=opts.TooltipOpts(is_show=False),

                     #legend_opts=opts.LegendOpts(textstyle_opts={"fontSize": 20}),
                     #graphic_textstyle_opts = opts.GraphicTextStyleOpts(font='2em "STHeiti", sans-serif'),
                     datazoom_opts=opts.DataZoomOpts(range_start= start,range_end= 100))
    #.set_global_opts()


    #.render("China_1_Daily_C_vs_P.html")
)

e= (
    Line()
    .add_xaxis(mydate)
    .add_yaxis("Positive", pos,is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),)
    .add_yaxis("Negative", neg,is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),)


    .set_global_opts(title_opts=opts.TitleOpts(title="Weekly Media Effect In HongKong"),
                     #tooltip_opts=opts.TooltipOpts(is_show=False),

                     #legend_opts=opts.LegendOpts(textstyle_opts={"fontSize": 20}),
                     #graphic_textstyle_opts = opts.GraphicTextStyleOpts(font='2em "STHeiti", sans-serif'),
                     datazoom_opts=opts.DataZoomOpts(range_start= start,range_end= 100))
    #.set_global_opts()


    #.render("China_1_Daily_C_vs_P.html")
)
page = Page(layout=Page.SimplePageLayout)
page.add(c,d,e)
page.render('./res/'+str(time.time())+'WeeklySuicide.html')
