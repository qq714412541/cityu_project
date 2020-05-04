import datetime
print(datetime.datetime.now())
print(datetime.timedelta(days = 7))
a = datetime.datetime.now()+datetime.timedelta(days = 7)
#a = '2015-12-27'+datetime.timedelta(days = 7).strftime("%Y-%m-%d")
print((a.strftime('%Y-%m-%d')))