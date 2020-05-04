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
name = str(time.time())+'.csv'
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
my_dict = {
    'week_date':res_date,
    'week_count':res_count
}
df3 = pd.DataFrame(my_dict)






print(df3)

mydate = df3['week_date'].to_list()
mycount = df3['week_count'].to_list()
print(mydate)
print(len(mydate))

from pyecharts.charts import Bar,Line,Gauge,Page
from pyecharts import options as opts
from pandas import DataFrame

start = (1-30/len(mycount))*100
c = (
    Line()
    .add_xaxis(mydate)
    .add_yaxis("Weekly Suicide", mycount,is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),)

    .set_global_opts(title_opts=opts.TitleOpts(title="Weekly Suicide Count In HongKong"),
                     #tooltip_opts=opts.TooltipOpts(is_show=False),

                     #legend_opts=opts.LegendOpts(textstyle_opts={"fontSize": 20}),
                     #graphic_textstyle_opts = opts.GraphicTextStyleOpts(font='2em "STHeiti", sans-serif'),
                     datazoom_opts=opts.DataZoomOpts(range_start= start,range_end= 100))
    #.set_global_opts()


    #.render("China_1_Daily_C_vs_P.html")
)
page = Page(layout=Page.SimplePageLayout)
page.add(c)
page.render('../res/'+str(time.time())+'WeeklySuicide.html')
