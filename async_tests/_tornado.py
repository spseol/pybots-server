from time import sleep, time

import tornado.ioloop
import tornado.web
from tornado.web import asynchronous


class MainHandler(tornado.web.RequestHandler):
    @asynchronous
    def get(self):
        self.write("request {} started.\n".format(time()))
        self.flush()
        sleep(5)
        self.write('request {} end\n'.format(time()))
        self.flush()
        self.finish()


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()