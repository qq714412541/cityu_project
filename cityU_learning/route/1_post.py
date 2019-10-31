import requests
import json

'''user_info = {'name': 111, 'password': 222}
print(type(user_info))
user_info_json = json.dumps(user_info)
print(type(user_info_json))
#r = requests.post("http://127.0.0.1:5000/register", data=user_info)
r = requests.post("http://127.0.0.1:5000/add", data=user_info)
#data is in form style
print(r.text)'''

json_data = {'a': 1, 'b': 2}

r = requests.post("http://127.0.0.1:5000/add", json=json_data)  ###data = and json =
print(r.headers)  ###response headers
print(r.text)


#/page/<int:num>   transfer to be int, or that will be str.  int to int, and if input is other type, that will be wrong
#/user/<username>/friends   save as str