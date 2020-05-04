import pandas as pd
import numpy as np
import time
from Algorithm import Algorithm
#path = 'new_data.xlsx'


class NewData:
    def read_new(self,path):
        try:
            df = pd.read_excel(path,sheet_name='count')
            #df2 = pd.read_excel(path,sheet_name='frequency')
            #data_China_ycc = pd.read_excel(s+'_cdP{0}.xlsx'.format(date),sheet_name=s+'_cd0')
            #print(df2)
            new_date = df['week_date'].to_list()[0]

            new_count = df['week_count'].to_list()[0]
            new_sui1 = df['sui1'].to_list()[0]
            new_sui2 = df['sui2'].to_list()[0]
            new_sui3 = df['sui3'].to_list()[0]
            new_pos = df['pos'].to_list()[0]
            new_neg = df['neg'].to_list()[0]
            print(new_count)
            print(new_neg)



            df3 = pd.read_csv('../file/All2.csv')
            mydate = df3['week_date'].to_list()
            mycount = df3['week_count'].tolist()
            #print(df3)

            new_date=new_date.strftime('%Y-%m-%d')

            print(new_date)
            print(type(new_date),type(df3['week_date'].iloc[-1]))
            print(df3['week_date'].iloc[-1])


            if new_date == df3['week_date'].iloc[-1]:

                df3['week_count'].iloc[-1] = new_count
                df3['sui1'].iloc[-1] = new_sui1
                df3['sui2'].iloc[-1] = new_sui2
                df3['sui3'].iloc[-1] = new_sui3
                df3['neg'].iloc[-1] = new_neg
                df3['pos'].iloc[-1] = new_pos

                import datetime
                import random
                pre_dnew = datetime.datetime.strptime(mydate[-1],'%Y-%m-%d')+datetime.timedelta(days=7)
                #print(pre_date)
                #print(type(pre_date))
                pre_dnew = pre_dnew.strftime('%Y-%m-%d')
                myal = Algorithm()
                print(new_count)
                pre_cnew = myal.predict(mycount,new_sui1,new_sui2,new_sui3,new_neg,new_pos)
                #pre_cnew = random.choice(mycount)

                df3 = df3.append({'week_date':pd.NaT,'week_count':pd.NaT,'sui1':pd.NaT,'sui2':pd.NaT,'sui3':pd.NaT,'neg':pd.NaT,
                            'pos':pd.NaT,'pre':pd.NaT,'path':pd.NaT},ignore_index=True)
                #print(df3)
                #print(df3['week_date'].tolist()[-1])
                df3['week_date'].iloc[-1] = pre_dnew
                df3['pre'].iloc[-1] = pre_cnew
                print(df3)

                df3.to_csv('../file/All2.csv',index = None)
                return 0
            else:
                return 11
        except:
            return 12


'''su = NewData()
path = '../file/new_data.xlsx'
su.read_new(path)'''

