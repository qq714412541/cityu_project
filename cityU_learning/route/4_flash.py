from flask import Flask, flash, get_flashed_messages
import time

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return 'hi'


@app.route('/gen')
def gen():
    info = 'access at ' + time.time().__str__()
    flash(info)
    return info


@app.route('/show1')
def show1():
    return get_flashed_messages().__str__()


@app.route('/show2')
def show2():
    return get_flashed_messages().__str__()

###that means everytime you operate the method, the session will be deleted


if __name__ == "__main__":
    app.run(port=5000, debug=True)