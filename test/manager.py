from app import create_app
from flask_script import Manager


app = create_app()
# manager = Manager(app)

# @app.route('/')
# def index():
#     return '首页'


if __name__ == '__main__':
    app.run(debug=True)
