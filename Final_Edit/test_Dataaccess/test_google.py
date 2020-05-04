import pandas as pd
import numpy as np
df1 = pd.read_csv('test1910131927.suicide.csv')
print(df1)
suicide1_list = df1['suicide'].to_list()

df2 = pd.read_csv('test1910131927.自杀.csv')
print(df2)
suicide2_list = df2['suicide'].to_list()

df3 = pd.read_csv('test1910131927.2.csv')
print(df3)
suicide3_list = df3['suicide'].to_list()

print(len(suicide1_list))
import random
for i in range(521):
    suicide1_list.append(random.choice(suicide1_list))
    suicide2_list.append(random.choice(suicide2_list))
    suicide3_list.append(random.choice(suicide3_list))

print(len(suicide1_list))
