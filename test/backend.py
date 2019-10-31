import tornado.ioloop
import tornado.web
from test.test_google import google_trends

test = google_trends()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        #test.collect()

    '''def get(self):
        #self.write("Hello, world")
        test.collect()'''
class google_trends_test(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        test.collect()
        self.write('done')



def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/test", google_trends_test),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()