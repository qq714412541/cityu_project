from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from test.app3 import app
from tornado.ioloop import IOLoop
s = HTTPServer(WSGIContainer(app))
s.listen(9900)
IOLoop.current().start()