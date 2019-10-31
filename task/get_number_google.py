import pandas as pd
###len = 52
excel_path = 'test1910131927.suicide.csv'
d = pd.read_csv(excel_path)
#d = pd.read_excel(excel_path)
print(d.head())
print(d.index)
d_n = d.iloc[:,1]
print(d_n)


excel_path = 'test1910131927.自杀.csv'
d2 = pd.read_csv(excel_path)
#d = pd.read_excel(excel_path)
print(d2.head())
print(d2.index)
d2_n = d2.iloc[:,1]
print(d2_n)

excel_path = 'test1910131927.自殺.csv'
d3 = pd.read_csv(excel_path)
#d = pd.read_excel(excel_path)
print(d3.head())
print(d3.index)
d3_n = d3.iloc[:,1]
print(d3_n)

excel_path = 'numberofdeath.csv'
d4 = pd.read_csv(excel_path)
#d = pd.read_excel(excel_path)
print(d4.head())
print(d4.index)
d4_n = d4.iloc[:,1]
print(d4_n)

new = pd.concat([d4_n,d_n,d2_n,d3_n],axis=1,ignore_index=True)
#print('####',new)
new.to_csv('./alltest.csv',index=True)
print('#################################')
print(new.iloc[:,0])
print(new.iloc[:,1:4])

####model
import statsmodels.api as sm
import numpy as np
import statsmodels.formula.api as smf
#X = np.column_stack((x, x**2))
#X = sm.add_constant(X)
est2 = sm.OLS(new.iloc[:,0],new.iloc[:,1:4]).fit() #方法二
#y_pred = est.predict(X)
print(est2.summary())


'''b0 = est2.params['const']
b1 = est2.params[1]
b2 = est2.params[2]
print('slope1:',est2.params[1],'slope2',est2.params[2])
print('function:y=%f + x1* %f + x2* %f'%(est2.params['const'],est2.params[2],est2.params[1]))'''



####train and test
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(new.iloc[:,1:4],new.iloc[:,0], test_size = 0.2)


print('Shape of Training Set:',X_train.shape,'Shape of Testing Set:',X_test.shape)


from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

Y_test_pred = est2.predict(X_test)
Y_train_pred = est2.predict(X_train)

rmse_train = (np.sqrt(mean_squared_error(Y_train, Y_train_pred)))
r2_train = r2_score(Y_train, Y_train_pred)
rmse_test = (np.sqrt(mean_squared_error(Y_test, Y_test_pred)))
r2_test = r2_score(Y_test, Y_test_pred)

#est2.fit(X_train,Y_train)
print("The model performance for training set--------------------------------------")
print('RMSE is {}'.format(rmse_train))
print('R2 score is {}'.format(r2_train))
print("\n")


print("The model performance for testing set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse_test))
print('R2 score is {}'.format(r2_test))

####plot
import matplotlib.pyplot as plt
plt.scatter(Y_train,Y_train_pred,marker = 'o')
plt.xlabel('Y_train')
plt.ylabel('Y_train_pred')
plt.show()


plt.scatter(Y_test,Y_test_pred,marker = 'o')
plt.xlabel('Y_test')
plt.ylabel('Y_test_pred')
plt.show()
print(type(X_train))
a = Y_test_pred.tolist()
print(a,type(a),len(a))
print(new.iloc[:,0].tolist())

