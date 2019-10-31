#from pandas.io.json.json_normalize import nested_to_record
#!-*- coding: utf8 -*-
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
'''pytrends = TrendReq()
pytrends.build_payload(['suicide','自杀'],cat=0,timeframe='2016-12-14 2017-01-25',geo='',gprop='')
print(pytrends.interest_over_time())'''


pytrends = TrendReq()

#kw_list = ["suicide","自杀","自殺"]
#kw_list = ["自杀","自殺"]
kw_list = ["suicide","自杀","自殺"]


class google_trends:

    def collect(self,period,timestr):
        result = [0,0,0]

        for i,word in enumerate(kw_list):
            pytrends.build_payload([word],cat=0,timeframe=period,geo='HK',gprop='')

            df= pytrends.interest_over_time()
            result[i] = df

            df.to_csv('./test%s.%s.csv'%(timestr,word),index=True)
            data = pd.read_csv('./test%s.%s.csv'%(timestr,word))
            x = data.iloc[:, 0]
            #print(z)
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
        return result


if __name__ == "__main__":
    timestr = '1910131927'
    period = '2014-12-14 2017-01-25'
    test = google_trends()
    a = test.collect(period,timestr)
    print('#######',a)