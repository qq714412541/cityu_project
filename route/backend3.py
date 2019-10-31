from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from route.app3 import app
from tornado.ioloop import IOLoop
s = HTTPServer(WSGIContainer(app))
s.listen(8080)
IOLoop.current().start()