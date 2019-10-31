from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)


@app.route('/11')
def get_arg_info():
    r = request.args.get('info','name')# the second means show for no info
    if r == None:
        return ''
    return r

@app.route('/')
def hello_world2():
    print(request.path)
    print(request.full_path)
    return 'hello world'

@app.route('/22')
def get_arg():
    print(request.path)
    print(request.full_path)
    return request.args.__str__()


@app.route('/getlist')
def get_list():
    r = request.args.getlist('p')  # for multiple value of p
    return str(r)


@app.route('/register', methods=['POST','GET'])
def register():
    #if method == 'POST'
    print(request.headers)
    print(request.stream.read())
    print(request)
    '''print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))'''
    return 'welcome'

@app.route('/add', methods=['POST'])
def add():
    result = {'sum': request.json['a'] + request.json['b']}
    resp = Response(json.dumps(result), mimetype='application/json')
    resp.headers.add('Server', 'python flask')
    return resp

@app.route('/page/<int:num1>-<int:num2>')
def page(num1, num2):
    print(num1)
    print(num2)
    return 'hello world'

if __name__ == '__main__':
    app.run(port=5000,debug = True)