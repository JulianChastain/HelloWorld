class nextWordHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(nextWord(""))

def make_app():
    return tornado.web.Application([
        (r"/(.*)", web.StaticFileHandler, {"path": "./Static"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
