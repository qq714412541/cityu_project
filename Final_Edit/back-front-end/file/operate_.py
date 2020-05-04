import pandas as pd
df = pd.read_csv('All2.csv')
df = df[['week_date','week_count','sui1','sui2','sui3','neg','pos','pre','path']]
print(df)
df.to_csv('All2.csv',index = None)