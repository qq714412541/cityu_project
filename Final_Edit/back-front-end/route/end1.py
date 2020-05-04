from flask import Flask,request, jsonify, make_response,render_template
import os
import webbrowser
from werkzeug.utils import secure_filename
from task.NewData import NewData
from task.Graph import MyGraph
from task.CheckPath import CheckPath


app = Flask(__name__)
import time

import traceback,json

newdata = NewData()
newgraph = MyGraph()
checkpath = CheckPath()

SAVE_PATH = '../file'
ALLOWED_EXTENSIONS = set(['csv','xlsx','xls'])

def allowed_file(filename):
    #print(filename.rsplit('.', 1)[1].lower())
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def start():
    return 'hello flask'

@app.route('/test2')
def start2():
    return 'hello flask2'


@app.route('/apitest',methods=['GET'])
def api():
    response = {
        'code':0
    }
    return jsonify(response)

#@app.route('/test',methods=['GET'])
#def root():
    #app.send_static_file()
    #return app.send_static_file('../static/1_navigation.html')

@app.route('/check_result',methods=['GET'])
def check_result():
    res = checkpath.check()
    response = {
        'code':0,
        'path':res
    }

    #app.send_static_file()
    return jsonify(response)

@app.route('/task_recieve',methods=['POST'])
def task_recieve():
    print(request.files)
    if 'file' not in request.files:
        response = {
            'code':10003 # no file
        }
        print(10003)
    else:
        f = request.files['file']
        #print(f.rsplit('.', 1)[1].lower())
        #if allowed_file(f):
        if not allowed_file(secure_filename(f.filename)):
            response = {
                'code':10004 #file type is wrong
            }
        else:

            filepath = os.path.join(SAVE_PATH,secure_filename(f.filename))
            print(filepath)
            f.save(filepath)
            res = newdata.read_new(filepath)
            if res ==  0:
                res = newgraph.myg()
                response = {
                    'code': 0,
                    'reportPath':res
                }
            elif res == 11:
                response = {
                    'code': 10001 # date is wrong
                }
            else:
                response = {
                    'code':10002 # style is wrong
                }
    '''else:
        response={
            'code': 10001,#file is not in normal


        }'''
    return jsonify(response)

################player information

from datetime import timedelta

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True,host='0.0.0.0', port=5000)
    app.send_file_max_age_default = timedelta(seconds=1)



