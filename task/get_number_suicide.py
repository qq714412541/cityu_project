import pandas as pd

excel_path = 'suicide_daily_count.xls'
d = pd.read_excel(excel_path)
print(d.head())
print(d.index)
d1 = d.iloc[:,2:4]
print(d1)
d2 = d1[d1['inc_date'] == '2005-01-01']
print(d2)
num  = d2['N'].sum()
print(num)
a=d2.iloc[1,0]
#print(a)
b=0
sum = 0

n_list = []
date_list = []

for index, row in d1.iterrows():
    #print(index, row['inc_date'], row['N'])
    b = row['N']
    if a == row['inc_date']:
        sum = sum + b

    else:
        n_list = n_list+[sum]
        date_list = date_list + [a]
        a = row['inc_date']
        sum = b

print(n_list)
print(date_list)
print(len(n_list),len(date_list))

c={"date": date_list,"number": n_list}
df = pd.DataFrame(c,columns=['date', 'number'])  #指定列名为name和id，顺序name先，id后
print(df)
print(df.iloc[2,0])

count = -1
sum = 0
sum_list = []
count_list = []
for index,row in df.iterrows():


    b = row['number']
    if index % 7 == 0:
        count +=1
        count_list = count_list + [count]
        sum_list = sum_list + [sum]
        sum =  b

    else:
        sum = sum + b

print(count_list)
print(sum_list)


###
c={"period": count_list,"number": sum_list}
df_new = pd.DataFrame(c,columns=['period', 'number'])  #指定列名为name和id，顺序name先，id后
print(df_new)

result_test = df_new.iloc[1:54,1]
print(result_test)
result_test.to_csv('./numberofdeath.csv',index=True)







