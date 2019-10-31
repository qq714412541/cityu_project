import pandas as pd

class readfile:
    def excel(self,path,date_num,num_col):
        excel_path = path
        d = pd.read_excel(excel_path)
        print(d.head())
        print(d.index)
        d1 = d.iloc[:, 2:4]
        print(d1)
        d2 = d1[d1['inc_date'] == '2003-01-01']
        print(d2)
        num = d2['N'].sum()
        print(num)
        a = d2.iloc[1, 0]
        # print(a)
        b = 0
        sum = 0
        count = 0
        n_list = []
        date_list = []
        for index, row in d1.iterrows():
            # print(index, row['inc_date'], row['N'])
            b = row['N']
            if a == row['inc_date']:
                sum = sum + b

            else:
                n_list = n_list + [sum]
                date_list = date_list + [a]
                a = row['inc_date']
                sum = b
