from time import sleep

from tornado.gen import engine, Task
import tornado.httpserver
import tornado.ioloop
from tornado.locks import Lock
import tornado.web
from tornado.web import asynchronous
from tornado.log import enable_pretty_logging


enable_pretty_logging()

lock = Lock()


class Handler(tornado.web.RequestHandler):
    @asynchronous
    def get(self):
        print('start')
        tornado.ioloop.IOLoop.instance().add_callback_from_signal(self.loop)
        print('end')

    @asynchronous
    def loop(self):
        print('loop start')
        self.write_and_flush('Started! ')
        with (yield lock.acquire()):
            self.write_and_flush('Aquired, sleeping! ')
            sleep(5)
            self.write_and_flush('Releasing! ')
            sleep(1)
        self.write_and_flush('Released, end! ')
        self.finish()

    def write_and_flush(self, chunk):
        self.write(chunk)
        self.flush()


class MyHandler(tornado.web.RequestHandler):
    @asynchronous
    @engine
    def get(self):
        response = yield Task(lambda x, callback=None: print('callback: {}'.format(x)), 'argument')
        self.write(response)
        self.finish()

    def callback(self, callback, arg):
        print(arg)
        return callback(arg)


application = tornado.web.Application([
    (r"/", Handler),
    (r"/hu", MyHandler)
])

http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(8888)
tornado.ioloop.IOLoop.instance().start()