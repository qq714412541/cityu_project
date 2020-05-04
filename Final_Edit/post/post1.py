#coding=utf-8
import requests, json, os
file = './new_data.xlsx'
file2 = './test2.pdf'
file3 = 'test1.xlsx'
url = 'http://127.0.0.1:5000/task_recieve'
data = {
    'taskid' : 3,
    'reportid'  : 3,
    'name' : '123洒'
}
files = {
     #'json': (None, json.dumps(data), 'application/json'),
     'file': (os.path.basename(file), open(file, 'rb'), 'application/octet-stream')
}

r = requests.post(url, files=files)
print(r.content)