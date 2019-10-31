#from pandas.io.json.json_normalize import nested_to_record
#!-*- coding: utf8 -*-
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
'''pytrends = TrendReq()
pytrends.build_payload(['suicide','自杀'],cat=0,timeframe='2003-01-01 2015-12-30',geo='',gprop='')
print(pytrends.interest_over_time())'''
pytrends = TrendReq()
kw_list = ["suicide","自杀","自殺"]
class google_trends:
    def collect(self,period,timestr):
        result = [0,0,0]
        for i,word in enumerate(kw_list):
            pytrends.build_payload([word],cat=0,timeframe=period,geo='HK',gprop='')
            df= pytrends.interest_over_time()
            print(df)
            result[i] = df[word].values.reshape(-1,1).tolist()
            print(result[i])
            df.to_csv('./test%s.%s.csv'%(timestr,word),index=True)
            data = pd.read_csv('./test%s.%s.csv'%(timestr,word))
            x = data.iloc[:, 0]
            y = df.iloc[:,0]/100
            y = y.values.reshape(-1, 1)
            x.values.reshape(-1,1)
            xs = [datetime.strptime(d, '%Y-%m-%d').date() for d in x]
            #print(xs,type(xs))
            plt.scatter(xs, y, color='blue')
            plt.title('google trends for %s'%word)
            plt.xlabel('time')
            plt.ylabel('relative value')
            plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
            plt.rcParams['axes.unicode_minus'] = False
            plt.savefig('./test%s_%s.jpg'%(timestr,word))
            plt.show()
            #print(df[word])
            a = df.to_json(orient='split')
            print('test',a)
            print('#test#',a[4])
        return result
if __name__ == "__main__":
    timestr = '1910131927'
    period = '2005-01-01 2015-12-30'
    test = google_trends()
    a = test.collect(period,timestr)
    print('#######',a)